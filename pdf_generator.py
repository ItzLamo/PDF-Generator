"""PDF file generation and structure"""
from datetime import datetime

class PDFGenerator:
    def __init__(self, pdf_object):
        self.pdf_object = pdf_object
        
    def generate_pdf(self, filename):
        """Generate the PDF file with proper structure"""
        pdf = [
            "%PDF-1.4",
            # Catalog
            "1 0 obj",
            "<<",
            "/Type /Catalog",
            "/Pages 2 0 R",
            ">>",
            "endobj",
            
            # Pages
            "2 0 obj",
            "<<",
            "/Type /Pages",
            "/Kids [3 0 R]",
            "/Count 1",
            ">>",
            "endobj",
            
            # Page
            "3 0 obj",
            "<<",
            "/Type /Page",
            "/Parent 2 0 R",
            "/Resources <<",
            "    /Font <<",
            "        /Helvetica <<",
            "            /Type /Font",
            "            /Subtype /Type1",
            "            /BaseFont /Helvetica",
            "        >>",
            "        /Helvetica-Bold <<",
            "            /Type /Font",
            "            /Subtype /Type1",
            "            /BaseFont /Helvetica-Bold",
            "        >>",
            "    >>",
            ">>",
            f"/MediaBox [0 0 {self.pdf_object.page_width} {self.pdf_object.page_height}]",
            "/Contents 4 0 R",
            ">>",
            "endobj",
            
            # Content
            "4 0 obj",
            "<<",
            "/Length " + str(len('\n'.join(self.pdf_object.content))),
            ">>",
            "stream",
            *self.pdf_object.content,
            "endstream",
            "endobj",
            
            # Cross-reference table
            "xref",
            "0 5",
            "0000000000 65535 f",
            "0000000010 00000 n",
            "0000000079 00000 n",
            "0000000173 00000 n",
            "0000000457 00000 n",
            
            # Trailer
            "trailer",
            "<<",
            "/Size 5",
            "/Root 1 0 R",
            ">>",
            "startxref",
            "565",
            "%%EOF"
        ]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(pdf))