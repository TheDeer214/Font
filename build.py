from fontTools.ttLib import TTFont

print("Loading FiraCode-Regular.ttf...")
font = TTFont("FiraCode-Regular.ttf")

# Get character map and available glyphs
cmap = font['cmap'].getBestCmap()
glyph_order = font.getGlyphOrder()
glyph_set = set(glyph_order)

# Map of default characters/glyphs to their full alternate variant glyph names
# This covers cv01..cv32 and ss01..ss10 from Fira Code v6
variant_overrides = {
    'a': 'a.cv01',                  # Alternate 'a'
    'g': 'g.cv02',                  # Alternate 'g'
    'i': 'i.cv03',                  # Alternate 'i' (serif/curved)
    'l': 'l.cv07',                  # Alternate 'l' (curved tail)
    'r': 'r.ss01',                  # Alternate 'r'
    'zero': 'zero.cv11',            # Dotted zero
    'three': 'three.cv14',          # Flat top '3'
    'asterisk': 'asterisk.cv15',    # High-positioned asterisk
    'asciitilde': 'asciitilde.cv17',# Centered tilde ~
    'percent': 'percent.cv18',      # Alternate %
    'at': 'at.ss05',                # Compact @
    'dollar': 'dollar.ss04',        # Open dollar $
    'ampersand': 'ampersand.ss03',  # Alternate &
    'bar': 'bar.cv30',              # Dotted/broken pipe |
    'bracketleft': 'bracketleft.cv27',   # Alternate [
    'bracketright': 'bracketright.cv27', # Alternate ]
    'braceleft': 'braceleft.cv29',       # Alternate {
    'braceright': 'braceright.cv29',     # Alternate }
    'parenleft': 'parenleft.cv31',       # Alternate (
    'parenright': 'parenright.cv31',     # Alternate )
}

print("Baking all character variants into primary character map...")
remapped_count = 0

# Apply overrides to cmap
for char_code, current_glyph in list(cmap.items()):
    if current_glyph in variant_overrides:
        target_glyph = variant_overrides[current_glyph]
        if target_glyph in glyph_set:
            cmap[char_code] = target_glyph
            remapped_count += 1
            print(f"Baked variant: {current_glyph} -> {target_glyph}")

print(f"Total glyph variants permanently activated: {remapped_count}")

# Save output TTF file
output_filename = "FiraCode-AllVariants.ttf"
print(f"Saving modified font to {output_filename}...")
font.save(output_filename)
print("Build finished successfully!")
