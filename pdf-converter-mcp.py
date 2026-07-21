import asyncio
import subprocess
import json
import sys
from mcp.server import Server
from mcp.types import Tool, TextContent

app = Server("pdf-converter")

@app.call_tool()
def convert_pdf_to_md(pdf_path: str, output_path: str):
    """Convert PDF to Markdown using your local converter"""
    try:
        # Replace this with your actual converter command
        result = subprocess.run(
            ["markitdown", pdf_path, "-o", output_path],
            capture_output=True,
            text=True
        )
        return TextContent(text=f"Converted {pdf_path} to {output_path}")
    except Exception as e:
        return TextContent(text=f"Error: {str(e)}")

if __name__ == "__main__":
    try:
        initialization_options = app.create_initialization_options()
    except AttributeError:
        initialization_options = {}
    asyncio.run(app.run(sys.stdin, sys.stdout, initialization_options))


