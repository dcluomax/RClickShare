import winreg
import sys
import ctypes

# Request admin privileges
if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) != 42:
    print("Error: Failed to run with admin privileges.")
    sys.exit(1)

# Define the registry key to remove
key_path = r'*\shell\Share with Flask Server'

# Delete the registry key
try:
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, key_path)
except WindowsError as e:
    print(f"Error deleting registry key: {e}")
else:
    print("Registry key deleted successfully.")

sys.exit(1)