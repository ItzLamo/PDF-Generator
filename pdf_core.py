"""Enhanced core PDF generation functionality"""
from constants import *

class PDFObject:
    def __init__(self):
        self.content = []
        self.page_width = PAGE_WIDTH
        self.page_height = PAGE_HEIGHT
    
    def add_text(self, text, x, y, font_size=DEFAULT_FONT_SIZE, font=DEFAULT_FONT, color="black"):
        """Add text with custom font, size and color"""
        r, g, b = COLORS[color]
        self.content.extend([
            f"{r} {g} {b} rg",  # Set color
            "BT",
            f"/{font} {font_size} Tf",
            f"{x} {y} Td",
            f"({text}) Tj",
            "ET"
        ])
    
    def add_line(self, x1, y1, x2, y2, width=DEFAULT_LINE_WIDTH, color="black"):
        """Draw a line with custom width and color"""
        r, g, b = COLORS[color]
        self.content.extend([
            f"{r} {g} {b} RG",  # Set stroke color
            f"{width} w",
            f"{x1} {y1} m",
            f"{x2} {y2} l",
            "S"
        ])
    
    def add_rectangle(self, x, y, width, height, fill=False, color="black"):
        """Draw a rectangle with option to fill"""
        r, g, b = COLORS[color]
        self.content.extend([
            f"{r} {g} {b} {('rg' if fill else 'RG')}",  # Set fill or stroke color
            f"{x} {y} {width} {height} re",
            f"{'f' if fill else 's'}"
        ])
    
    def add_circle(self, x, y, radius, fill=False, color="black"):
        """Draw a circle using Bezier curves"""
        r, g, b = COLORS[color]
        self.content.extend([
            f"{r} {g} {b} {('rg' if fill else 'RG')}",  # Set fill or stroke color
        ])
        
        k = 0.552284749831  # Magic number for circle approximation
        rx = radius
        ry = radius
        
        # Move to start point
        path = f"{x-rx} {y} m\n"
        
        # Add four Bezier curves to create the circle
        path += f"{x-rx} {y+ry*k} {x-rx*k} {y+ry} {x} {y+ry} c\n"
        path += f"{x+rx*k} {y+ry} {x+rx} {y+ry*k} {x+rx} {y} c\n"
        path += f"{x+rx} {y-ry*k} {x+rx*k} {y-ry} {x} {y-ry} c\n"
        path += f"{x-rx*k} {y-ry} {x-rx} {y-ry*k} {x-rx} {y} c\n"
        
        self.content.append(f"{path}{'f' if fill else 's'}")