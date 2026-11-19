from fontTools.ttLib import TTFont
from fontTools.feaLib.builder import addOpenTypeFeatures

print("Loading fonts...")
sf_font = TTFont("SFMono-Regular.otf")
fira_font = TTFont("FiraCode-Regular.ttf")

def safe_copy_glyph(source_font, target_font, source_name, target_name):
    """Safely copies a glyph from source to target by name, with fallback options."""
    # Find which name exists in the source font
    actual_name = None
    for name in [source_name, target_name, f"uni{ord('≠'):04X}" if source_name == "notequal" else None]:
        if name and name in source_font.getGlyphOrder():
            actual_name = name
            break
            
    if not actual_name:
        print(f"Skipping: Could not find glyph matching '{source_name}' in source font.")
        return

    print(f"Found source glyph '{actual_name}', copying as '{target_name}'...")
    
    # Ensure target has the glyph order entry
    if target_name not in target_font.getGlyphOrder():
        target_font.getGlyphOrder().append(target_name)
        
    # Copy metrics safely
    try:
        source_hmtx = source_font['hmtx'].metrics
        if actual_name in source_hmtx:
            target_font['hmtx'].metrics[target_name] = source_hmtx[actual_name]
    except Exception as e:
        print(f"Note on metrics for {target_name}: {e}")
        
    # Copy outline data safely
    try:
        if 'glyf' in source_font and 'glyf' in target_font:
            if actual_name in source_font['glyf']:
                target_font['glyf'][target_name] = source_font['glyf'][target_name]
        print(f"Successfully injected: {target_name}")
    except Exception as e:
        print(f"Error copying outline for {target_name}: {e}")

print("Copying ligature glyphs...")
# Try copying notequal (checking both 'notequal' and unicode name 'uni2260')
safe_copy_glyph(fira_font, sf_font, "notequal", "notequal")
# Try copying arrow/hyphen-greater variants
safe_copy_glyph(fira_font, sf_font, "hyphen_greater", "hyphen_greater")

# Define your OpenType rules
fea_code = """
feature calt {
    sub exclam equal by notequal;
} calt;
"""

with open("rules.fea", "w") as f:
    f.write(fea_code)

print("Adding OpenType features...")
addOpenTypeFeatures(sf_font, "rules.fea")

print("Saving custom font...")
sf_font.save("SFMono-Custom.otf")
print("Build successful!")
