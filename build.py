from fontTools.ttLib import TTFont
from fontTools.feaLib.builder import addOpenTypeFeatures

# Load font
font = TTFont("SFMono-Regular.otf")

# Apply your OpenType feature file
addOpenTypeFeatures(font, "rules.fea")

# Save the output
font.save("SFMono-Custom.otf")
print("Custom font built successfully!")
