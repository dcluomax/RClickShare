# RClickShare
`RClickShare` is a Python script that adds a context menu item to the Windows Explorer right-click menu, allowing you to easily share a selected file via a Flask server. The script creates a registry key that adds a "Share with Flask Server" option to the context menu, which, when selected, starts a Flask server and copies the URL of the selected file to the clipboard.

# Prerequisites
Before you can use RClickShare, you need to have the following installed on your system:

# Python 3.x
- The Flask module for Python (pip install flask)
- The pyperclip module for Python (pip install pyperclip)
- (Optional) Admin privileges on Windows to add a new context menu item to the registry

# Install / Uninstall
The `install.py` script is a Python script that adds a context menu item to the Windows Explorer right-click menu.
The `uninstall.py` script removes the context menu item.
