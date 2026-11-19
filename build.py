from fontTools.ttLib import TTFont
from fontTools.feaLib.builder import addOpenTypeFeatures

print("Loading fonts...")
sf_font = TTFont("SFMono-Regular.otf")
fira_font = TTFont("FiraCode-Regular.ttf")

def copy_glyph(source_font, target_font, glyph_name):
    """Copies a glyph's outline and metrics from source to target font if it exists."""
    if glyph_name in source_font.getGlyphOrder():
        # Add to glyph order if not already there
        if glyph_name not in target_font.getGlyphOrder():
            target_font.getGlyphOrder().append(glyph_name)
        
        # Copy glyph metrics (width, sidebearings)
        if glyph_name in source_font['hmtx']:
            target_font['hmtx'][glyph_name] = source_font['hmtx'][glyph_name]
            
        # Copy TrueType outline data
        if 'glyf' in source_font and 'glyf' in target_font:
            if glyph_name in source_font['glyf']:
                target_font['glyf'][glyph_name] = source_font['glyf'][glyph_name]
        print(f"Successfully copied glyph: {glyph_name}")
    else:
        print(f"Warning: Glyph '{glyph_name}' not found in source font.")

print("Copying ligature glyphs from Fira Code to SF Mono...")
# Fira Code typically uses 'hyphen_greater' for -> and 'notequal' for !=
copy_glyph(fira_font, sf_font, "hyphen_greater")
copy_glyph(fira_font, sf_font, "notequal")

# Define your OpenType rules
fea_code = """
feature calt {
    sub hyphen greater by hyphen_greater;
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
