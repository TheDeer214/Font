from fontTools.ttLib import TTFont

print("Loading Fira Code...")
# Load the official Fira Code TTF you uploaded to the repo
font = TTFont("FiraCode-Regular.ttf")

# Choose your favorite lowercase 'l' variant code here:
# 'cv07', 'cv08', 'cv09', or 'cv10'
chosen_variant = "cv07"  # Change this if you want a different style!

target_glyph_name = f"l.{chosen_variant}"
glyph_order = font.getGlyphOrder()

if target_glyph_name in glyph_order:
    print(f"Found variant {target_glyph_name}! Baking it into default 'l'...")
    
    # Get the character map (Unicode -> Glyph Name)
    cmap = font['cmap'].getBestCmap()
    
    # Unicode for lowercase 'l' is U+006C
    unicode_l = ord('l')
    
    if unicode_l in cmap:
        old_glyph = cmap[unicode_l]
        print(f"Replacing default '{old_glyph}' with '{target_glyph_name}' for 'l'")
        
        # Point the 'l' unicode slot directly to your chosen variant glyph
        cmap[unicode_l] = target_glyph_name
        
        # Also copy its metrics to ensure spacing is correct
        if target_glyph_name in font['hmtx'].metrics:
            font['hmtx'].metrics['l'] = font['hmtx'].metrics[target_glyph_name]
            
        print("Successfully baked variant into default slot!")
    else:
        print("Error: Could not find Unicode mapping for lowercase 'l'.")
else:
print(f"Warning: Variant '{target_glyph_name}' not found in this font file.")

print("Saving final custom Fira Code variant...")
font.save("SFMono-Custom.otf") # Kept as SFMono-Custom.otf so your existing workflow artifact uploader finds it instantly!
print("Build complete!")
