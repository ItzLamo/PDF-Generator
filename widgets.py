"""Custom widgets for the PDF generator GUI"""
import tkinter as tk
from tkinter import ttk

class ColorPicker(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.color_var = tk.StringVar(value="black")
        
        ttk.Label(self, text="Color:").pack(side=tk.LEFT, padx=5)
        colors = ["black", "red", "green", "blue", "gray"]
        self.combo = ttk.Combobox(self, values=colors, textvariable=self.color_var, width=10)
        self.combo.pack(side=tk.LEFT, padx=5)
        
    def get(self):
        return self.color_var.get()

class FontSelector(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.font_var = tk.StringVar(value="Helvetica")
        self.style_var = tk.StringVar(value="regular")
        
        # Font family
        ttk.Label(self, text="Font:").pack(side=tk.LEFT, padx=5)
        fonts = ["Helvetica", "Times", "Courier"]
        self.font_combo = ttk.Combobox(self, values=fonts, textvariable=self.font_var, width=15)
        self.font_combo.pack(side=tk.LEFT, padx=5)
        
        # Font style
        ttk.Label(self, text="Style:").pack(side=tk.LEFT, padx=5)
        styles = ["regular", "bold", "italic", "bold-italic"]
        self.style_combo = ttk.Combobox(self, values=styles, textvariable=self.style_var, width=10)
        self.style_combo.pack(side=tk.LEFT, padx=5)
    
    def get(self):
        return self.font_var.get(), self.style_var.get()

class ShapeControls(ttk.LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="Shape Properties", **kwargs)
        
        # Shape type
        self.shape_var = tk.StringVar(value="none")
        shapes_frame = ttk.Frame(self)
        shapes_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Radiobutton(shapes_frame, text="None", variable=self.shape_var, value="none").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(shapes_frame, text="Line", variable=self.shape_var, value="line").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(shapes_frame, text="Rectangle", variable=self.shape_var, value="rectangle").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(shapes_frame, text="Circle", variable=self.shape_var, value="circle").pack(side=tk.LEFT, padx=5)
        
        # Line width
        width_frame = ttk.Frame(self)
        width_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(width_frame, text="Line Width:").pack(side=tk.LEFT, padx=5)
        self.width_var = tk.StringVar(value="1")
        self.width_spin = ttk.Spinbox(width_frame, from_=1, to=10, width=5, textvariable=self.width_var)
        self.width_spin.pack(side=tk.LEFT, padx=5)
        
        # Fill option
        self.fill_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, text="Fill Shape", variable=self.fill_var).pack(padx=5, pady=5)
    
    def get(self):
        return {
            "type": self.shape_var.get(),
            "width": int(self.width_var.get()),
            "fill": self.fill_var.get()
        }