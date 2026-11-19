from fontTools.ttLib import TTFont

# Load standard Fira Code
font = TTFont("FiraCode-Regular.ttf")

# Example: Swap standard 'l' with the 'cv07' variant shape
# Map the character 'l' (Unicode 0x006C) directly to the variant glyph name
cmap = font['cmap'].getBestCmap()

# Replace with the exact variant glyph name (e.g., 'l.cv07' or 'locl_l')
if 'l.cv07' in font.getGlyphOrder():
    cmap[ord('l')] = 'l.cv07'
    print("Successfully mapped 'l' to cv07 variant!")

# Save as your custom permanent variant font
font.save("FiraCode-CustomVariant.ttf")
