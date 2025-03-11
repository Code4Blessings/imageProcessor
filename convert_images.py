import os
import subprocess
from pathlib import Path
from PIL import Image

# Set Input and Output Folders
input_folder = Path("svg_folder")
output_folder = Path("png_folder")

# Ensure Output Folder Exists
output_folder.mkdir(parents=True, exist_ok=True)

# Function to Convert SVG to PNG
def convert_svg_to_png(svg_file, png_file):
    try:
        # Run Inkscape command for conversion
        subprocess.run([
            "/Applications/Inkscape.app/Contents/MacOS/inkscape",
            str(svg_file),
            "--export-type=png",
            "--export-filename=" + str(png_file),
            "--export-width=2550",
            "--export-height=2550"
        ], check=True)
        print(f"Converted: {svg_file} → {png_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {svg_file}: {e}")

# Process all SVGs in the Input Folder
for svg_file in input_folder.glob("*.svg"):
    png_file = output_folder / (svg_file.stem + ".png")
    convert_svg_to_png(svg_file, png_file)

print("✅ Batch conversion complete!")

