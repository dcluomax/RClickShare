import os
import sys
import subprocess
import pyperclip
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        # Get the path of the selected file from the command-line argument
        file_path = sys.argv[1]

        # Copy the URL to the clipboard
        url = f'http://127.0.0.1:8833/{os.path.basename(file_path)}'
        pyperclip.copy(url)
        print(f"URL '{url}' copied to clipboard.")

        # Start the Flask server on port 8833 with debug=False
        app.run(port=8833, debug=False)

    else:
        print("Usage: python share_file.py <file_path>")
