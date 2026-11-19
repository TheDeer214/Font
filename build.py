from fontTools.ttLib import TTFont

print("Loading fonts...")
fira_font = TTFont("FiraCode-Regular.ttf")

print("\n--- Searching Fira Code for arrow/hyphen glyphs ---")
for glyph_name in fira_font.getGlyphOrder():
    if any(keyword in glyph_name.lower() for keyword in ["arrow", "hyphen", "greater", "equal", "notequal"]):
        print(f"Found glyph: {glyph_name}")
print("--------------------------------------------------\n")
