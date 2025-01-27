from PIL import Image
import numpy as np
from tkinter import filedialog

# Predefined distinct colors for 42 tiles
define_colors = [
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#800000", "#808000",
    "#008000", "#800080", "#008080", "#000080", "#FFA500", "#A52A2A", "#5F9EA0", "#7FFF00",
    "#D2691E", "#FF7F50", "#6495ED", "#DC143C", "#00FA9A", "#FFD700", "#ADFF2F", "#4B0082",
    "#FF69B4", "#CD5C5C", "#BA55D3", "#7B68EE", "#48D1CC", "#C71585", "#191970", "#F4A460",
    "#2E8B57", "#4682B4", "#D2B48C", "#008B8B", "#BDB76B", "#556B2F", "#8B4513", "#9932CC",
    "#8B0000", "#E9967A"
]

# Map colors to tile names
color_to_tile = {color: f"Tile{i}" for i, color in enumerate(define_colors)}

# Convert HEX color to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Precompute RGB values for predefined colors
predefined_rgb_colors = [hex_to_rgb(color) for color in define_colors]

def closest_color(rgb_color):
    """Find the closest predefined color to the given RGB color."""
    distances = [np.linalg.norm(np.array(rgb_color) - np.array(pre_color)) for pre_color in predefined_rgb_colors]
    return define_colors[np.argmin(distances)]

def image_to_tilemap(image_path, grid_size=128):
    """Convert an image to a tilemap array."""
    # Open image and resize it to the grid size
    img = Image.open(image_path).convert("RGB")
    img.thumbnail((grid_size, grid_size), Image.Resampling.LANCZOS)
    img_width, img_height = img.size

    # Create a grid filled with tile names
    tilemap = []
    for y in range(img_height):
        row = []
        for x in range(img_width):
            rgb_color = img.getpixel((x, y))
            closest = closest_color(rgb_color)
            row.append(color_to_tile[closest])
        tilemap.append(row)
    
    return tilemap

def save_tilemap(tilemap, file_path):
    """Save the tilemap array to a text file."""
    with open(file_path, "w") as f:
        for row in tilemap:
            f.write(" ".join(row) + "\n")
    print(f"Tilemap saved to {file_path}")

def main():
    # Ask user to open an image file
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not image_path:
        print("No image selected.")
        return

    # Convert image to tilemap
    print("Processing image...")
    tilemap = image_to_tilemap(image_path)

    # Save the tilemap to a text file
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if save_path:
        save_tilemap(tilemap, save_path)

if __name__ == "__main__":
    main()
