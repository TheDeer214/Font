from fontTools.ttLib import TTFont
from fontTools.merge import Merger

print("Loading fonts...")
# Load both fonts in the workspace
sf_font = "SFMono-Regular.otf"
fira_font = "FiraCode-Regular.ttf"

print("Merging Fira Code ligatures and rules into SF Mono...")
merger = Merger()
merged_font = merger.merge([sf_font, fira_font])

print("Saving final custom font...")
merged_font.save("SFMono-Custom.otf")
print("Build complete!")
