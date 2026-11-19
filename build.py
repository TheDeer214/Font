from fontTools.ttLib import TTFont
from fontTools.feaLib.builder import addOpenTypeFeatures

print("Loading fonts...")
sf_font = TTFont("SFMono-Regular.otf")
fira_font = TTFont("FiraCode-Regular.ttf")

# Example: If you want to pull a specific glyph or write custom rules, 
# you can define your feature file explicitly or copy glyph tables.
# Let's create a robust rules.fea file programmatically or use a file:

fea_code = """
feature calt {
    # Test standard arrow and notequal substitutions
    sub hyphen greater by hyphen_greater;
    sub exclam equal by notequal;
} calt;
"""

with open("rules.fea", "w") as f:
    f.write(fea_code)

print("Adding OpenType features to SF Mono...")
addOpenTypeFeatures(sf_font, "rules.fea")

print("Saving custom font...")
sf_font.save("SFMono-Custom.otf")
print("Build successful!")
