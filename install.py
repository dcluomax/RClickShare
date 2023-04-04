import os
import winreg
import sys
import ctypes

# Request admin privileges
if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) != 42:
    print("Error: Failed to run with admin privileges.")
    sys.exit(1)

# Get the path to the Python interpreter
python_exe = os.path.join(sys.exec_prefix, 'python.exe')

# Get the path to the Python script
script_path = os.path.abspath('share_file.py')

# Define the registry key
key_path = r'*\shell\Share with Flask Server'
key_name = 'Share with Flask Server'
command = f'"{python_exe}" "{script_path}" "%1"'
key_value = {'MUIVerb': key_name, 'command': command}

# Create the registry key
key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
winreg.SetValueEx(key, None, 0, winreg.REG_SZ, key_name)

# Create the "command" subkey
subkey = winreg.CreateKey(key, 'command')
winreg.SetValueEx(subkey, None, 0, winreg.REG_SZ, command)

# Close the registry key handles
winreg.CloseKey(subkey)
winreg.CloseKey(key)