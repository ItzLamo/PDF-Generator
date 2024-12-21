import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from pdf_core import PDFObject
from pdf_generator import PDFGenerator
from widgets import ColorPicker, FontSelector, ShapeControls
from constants import *

class PDFGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Generator")
        self.root.geometry("800x900")
        
        # Create main frame with scrollbar
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title section
        self.create_title_section()
        
        # Style section
        self.create_style_section()
        
        # Content section
        self.create_content_section()
        
        # Shape section
        self.create_shape_section()
        
        # Header/Footer section
        self.create_header_footer_section()
        
        # Buttons section
        self.create_buttons_section()
        
        # Preview canvas
        self.create_preview_section()
    
    def create_title_section(self):
        title_frame = ttk.LabelFrame(self.main_frame, text="Document Information", padding=10)
        title_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(title_frame, text="Title:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.title_entry = ttk.Entry(title_frame, width=50)
        self.title_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        self.title_entry.insert(0, "New Document")
        
        ttk.Label(title_frame, text="Author:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.author_entry = ttk.Entry(title_frame, width=50)
        self.author_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
    
    def create_style_section(self):
        style_frame = ttk.LabelFrame(self.main_frame, text="Text Style", padding=10)
        style_frame.pack(fill=tk.X, pady=5)
        
        # Font selector
        self.font_selector = FontSelector(style_frame)
        self.font_selector.pack(fill=tk.X, pady=5)
        
        # Font size
        size_frame = ttk.Frame(style_frame)
        size_frame.pack(fill=tk.X, pady=5)
        ttk.Label(size_frame, text="Size:").pack(side=tk.LEFT, padx=5)
        self.font_size = ttk.Spinbox(size_frame, from_=8, to=72, width=5)
        self.font_size.pack(side=tk.LEFT, padx=5)
        self.font_size.set(DEFAULT_FONT_SIZE)
        
        # Color picker
        self.color_picker = ColorPicker(style_frame)
        self.color_picker.pack(fill=tk.X, pady=5)
    
    def create_content_section(self):
        content_frame = ttk.LabelFrame(self.main_frame, text="Content", padding=10)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.content_text = tk.Text(content_frame, height=10, width=70)
        self.content_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=self.content_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.content_text['yscrollcommand'] = scrollbar.set
    
    def create_shape_section(self):
        self.shape_controls = ShapeControls(self.main_frame, padding=10)
        self.shape_controls.pack(fill=tk.X, pady=5)
    
    def create_header_footer_section(self):
        hf_frame = ttk.LabelFrame(self.main_frame, text="Header & Footer", padding=10)
        hf_frame.pack(fill=tk.X, pady=5)
        
        # Page numbers
        self.page_numbers = tk.BooleanVar(value=True)
        ttk.Checkbutton(hf_frame, text="Include page numbers", variable=self.page_numbers).pack(anchor=tk.W)
        
        # Date
        self.include_date = tk.BooleanVar(value=True)
        ttk.Checkbutton(hf_frame, text="Include date", variable=self.include_date).pack(anchor=tk.W)
    
    def create_buttons_section(self):
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(buttons_frame, text="Preview", command=self.preview_pdf).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Generate PDF", command=self.generate_pdf).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Clear All", command=self.clear_all).pack(side=tk.RIGHT, padx=5)
    
    def create_preview_section(self):
        preview_frame = ttk.LabelFrame(self.main_frame, text="Preview", padding=10)
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.preview_canvas = tk.Canvas(preview_frame, bg='white', width=400, height=200)
        self.preview_canvas.pack(fill=tk.BOTH, expand=True)
    
    def preview_pdf(self):
        # Clear canvas
        self.preview_canvas.delete("all")
        
        # Scale factor for preview
        scale = 0.4
        
        # Draw page outline
        self.preview_canvas.create_rectangle(
            10, 10,
            10 + PAGE_WIDTH * scale,
            10 + PAGE_HEIGHT * scale,
            outline="gray"
        )
        
        # Preview text
        title = self.title_entry.get()
        self.preview_canvas.create_text(
            20, 20,
            text=title,
            anchor=tk.NW,
            font=("Helvetica", int(12 * scale))
        )
    
    def generate_pdf(self):
        try:
            # Create PDF object
            pdf_obj = PDFObject()
            
            # Add title
            font_family, font_style = self.font_selector.get()
            font = FONTS[font_family][font_style]
            pdf_obj.add_text(
                self.title_entry.get(),
                MARGIN_LEFT,
                PAGE_HEIGHT - MARGIN_TOP,
                font_size=int(self.font_size.get()),
                font=font,
                color=self.color_picker.get()
            )
            
            # Add date if enabled
            if self.include_date.get():
                current_date = datetime.now().strftime("%Y-%m-%d")
                pdf_obj.add_text(
                    f"Generated on: {current_date}",
                    MARGIN_LEFT,
                    PAGE_HEIGHT - MARGIN_TOP - 30
                )
            
            # Add content
            content = self.content_text.get("1.0", tk.END).strip()
            y_pos = PAGE_HEIGHT - MARGIN_TOP - 60
            for line in content.split('\n'):
                pdf_obj.add_text(line, MARGIN_LEFT, y_pos)
                y_pos -= 20
            
            # Add shape if selected
            shape_props = self.shape_controls.get()
            if shape_props["type"] != "none":
                if shape_props["type"] == "line":
                    pdf_obj.add_line(
                        MARGIN_LEFT, y_pos - 20,
                        PAGE_WIDTH - MARGIN_RIGHT, y_pos - 20,
                        width=shape_props["width"]
                    )
                elif shape_props["type"] == "rectangle":
                    pdf_obj.add_rectangle(
                        MARGIN_LEFT, y_pos - 70,
                        100, 50,
                        fill=shape_props["fill"]
                    )
                elif shape_props["type"] == "circle":
                    pdf_obj.add_circle(300, y_pos - 45, 25)
            
            # Add page numbers if enabled
            if self.page_numbers.get():
                pdf_obj.add_text(
                    "Page 1",
                    PAGE_WIDTH // 2,
                    MARGIN_BOTTOM,
                    font_size=10
                )
            
            # Save dialog
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            
            if filename:
                PDFGenerator(pdf_obj).generate_pdf(filename)
                messagebox.showinfo("Success", f"PDF has been generated: {filename}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")
    
    def clear_all(self):
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, "New Document")
        self.author_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        self.font_size.set(DEFAULT_FONT_SIZE)
        self.preview_canvas.delete("all")

def main():
    root = tk.Tk()
    app = PDFGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()