"""Constants and configuration for the PDF generator"""

# PDF dimensions
PAGE_WIDTH = 612
PAGE_HEIGHT = 792

# Default margins
MARGIN_LEFT = 50
MARGIN_RIGHT = 50
MARGIN_TOP = 50
MARGIN_BOTTOM = 50

# Font configurations
FONTS = {
    "Helvetica": {
        "regular": "Helvetica",
        "bold": "Helvetica-Bold",
        "italic": "Helvetica-Oblique",
        "bold-italic": "Helvetica-BoldOblique"
    },
    "Times": {
        "regular": "Times-Roman",
        "bold": "Times-Bold",
        "italic": "Times-Italic",
        "bold-italic": "Times-BoldItalic"
    },
    "Courier": {
        "regular": "Courier",
        "bold": "Courier-Bold",
        "italic": "Courier-Oblique",
        "bold-italic": "Courier-BoldOblique"
    }
}

# Default styles
DEFAULT_FONT_SIZE = 12
DEFAULT_FONT = "Helvetica"
DEFAULT_LINE_WIDTH = 1

# Colors (RGB)
COLORS = {
    "black": (0, 0, 0),
    "red": (1, 0, 0),
    "green": (0, 1, 0),
    "blue": (0, 0, 1),
    "gray": (0.5, 0.5, 0.5)
}