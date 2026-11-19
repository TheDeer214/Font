from fontTools.ttLib import TTFont
from fontTools.feaLib.builder import addOpenTypeFeatures

print("Loading fonts...")
sf_font = TTFont("SFMono-Regular.otf")
fira_font = TTFont("FiraCode-Regular.ttf")

def safe_copy_glyph(source_font, target_font, glyph_name):
    """Safely copies a glyph from source to target by name if it exists."""
    if glyph_name in source_font.getGlyphOrder():
        if glyph_name not in target_font.getGlyphOrder():
            target_font.getGlyphOrder().append(glyph_name)
        
        try:
            if glyph_name in source_font['hmtx'].metrics:
                target_font['hmtx'].metrics[glyph_name] = source_font['hmtx'].metrics[glyph_name]
        except Exception as e:
            print(f"Metrics note for {glyph_name}: {e}")
            
        try:
            if 'glyf' in source_font and 'glyf' in target_font:
                if glyph_name in source_font['glyf']:
                    target_font['glyf'][glyph_name] = source_font['glyf'][glyph_name]
            print(f"Successfully injected: {glyph_name}")
        except Exception as e:
            print(f"Error copying outline for {glyph_name}: {e}")
    else:
        print(f"Skipping: '{glyph_name}' not found in Fira Code.")

print("Copying Fira Code ligatures...")
# Copy the exact ligature glyphs found in your log
safe_copy_glyph(fira_font, sf_font, "exclam_equal.liga")      # !=
safe_copy_glyph(fira_font, sf_font, "hyphen_hyphen.liga")    # --
safe_copy_glyph(fira_font, sf_font, "hyphen_start.seq")      # Arrow parts
safe_copy_glyph(fira_font, sf_font, "hyphen_middle.seq")
safe_copy_glyph(fira_font, sf_font, "hyphen_end.seq")

# Write the rules linking the keys to these exact glyphs
fea_code = """
feature calt {
    sub exclam equal by exclam_equal.liga;
    sub hyphen hyphen by hyphen_hyphen.liga;
} calt;
"""

with open("rules.fea", "w") as f:
    f.write(fea_code)

print("Adding OpenType features...")
addOpenTypeFeatures(sf_font, "rules.fea")

print("Saving custom font...")
sf_font.save("SFMono-Custom.otf")
print("Build successful!")
