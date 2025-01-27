import tkinter as tk
from tkinter import filedialog
import numpy as np

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

class TilemapEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Tilemap Editor")

        # Default grid settings
        self.grid_size = 128
        self.cell_size = 5  # Initial size of each cell
        self.current_color = define_colors[0]
        self.grid_data = np.full((self.grid_size, self.grid_size), self.current_color, dtype=object)

        # Create canvas
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.paint_cell)
        self.root.bind("<Configure>", self.resize_canvas)

        # Create color selector
        self.color_selector = tk.Frame(root)
        self.color_selector.pack()
        self.create_color_buttons()

        # Save button
        self.save_button = tk.Button(root, text="Save as Text Array", command=self.save_to_file)
        self.save_button.pack(pady=10)

        self.draw_grid()

    def create_color_buttons(self):
        """Create buttons for each of the colors."""
        for i, color in enumerate(define_colors):
            button = tk.Button(self.color_selector, bg=color, width=2, height=1, command=lambda c=color: self.set_current_color(c))
            button.grid(row=i // 7, column=i % 7, padx=1, pady=1)

    def set_current_color(self, color):
        """Set the current drawing color."""
        self.current_color = color

    def paint_cell(self, event):
        """Paint a cell with the current color."""
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            self.grid_data[y, x] = self.current_color
            self.canvas.create_rectangle(
                x * self.cell_size, y * self.cell_size,
                (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                fill=self.current_color, outline=self.current_color
            )

    def save_to_file(self):
        """Save the grid data to a text file as a tile-based array."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for row in self.grid_data:
                    row_tiles = [color_to_tile[color] for color in row]
                    f.write(" ".join(row_tiles) + "\n")
            print(f"Saved to {file_path}")

    def draw_grid(self):
        """Draw the grid based on the current cell size."""
        self.canvas.delete("grid")
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                color = self.grid_data[y, x]
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    fill=color, outline=color, tags="grid"
                )

    def resize_canvas(self, event):
        """Resize the canvas dynamically based on window size."""
        new_width = self.canvas.winfo_width()
        new_height = self.canvas.winfo_height()
        self.cell_size = min(new_width // self.grid_size, new_height // self.grid_size)
        self.draw_grid()

# Run the editor
if __name__ == "__main__":
    root = tk.Tk()
    editor = TilemapEditor(root)
    root.mainloop()
