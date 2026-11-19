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
    'l': 'l.cv10',                  # l
    'r': 'r.ss01',                  # r
    'three': 'three.cv14',          # 3
    'asterisk': 'asterisk.cv16',    # *
    'at': 'at.ss05',                # @
    'ampersand': 'ampersand.ss03',  # &
    'bar': 'bar.cv30',              # |
    'bracketleft': 'bracketleft.cv27',   # [
    'bracketright': 'bracketright.cv27', # ]
    'braceleft': 'braceleft.cv29',       # {
    'braceright': 'braceright.cv29',     # }
    'lessequal': 'lessequal.ss02',          # ss02: slanted <=, >=
    'exclam_equal': 'exclam_equal.ss08',    # ss08: slanted ==, ===, !=
    'period_hyphen': 'period_hyphen.cv25',  # cv25: lowered .- ligature
    'colon_hyphen': 'colon_hyphen.cv26',    # cv26: lowered :- ligature
    'period_equal': 'period_equal.cv32',    # cv32: lowered .= ligature
    'bracket_square': 'bracket_square.cv27',# cv27: solid box brackets []
    'brace_dots': 'brace_dots.cv28',        # cv28: dotted curly braces {..}
    'backslash_double': 'backslash_double.ss06', # ss06: parallel backslashes \\
    'equal_tilde': 'equal_tilde.ss07',      # ss07: approximate / not-approximate =~/!~
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
output_filename = "FiraCode-Variant.ttf"
print(f"Saving modified font to {output_filename}...")
font.save(output_filename)
print("Build finished successfully!")
