import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
	import os
	import sys
	import winreg as reg
	# Get path of current working directory and python.exe
	cwd = os.getcwd()
	python_exe = sys.executable
	
	# Set the path of the context menu (right-click menu)
	key_path = r'*\\shell\\Scanner\\'

	# Create outer key
	key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
	reg.SetValue(key, '', reg.REG_SZ, '&WCMS Scan')  

	# create inner key
	key1 = reg.CreateKey(key, r"command")
	reg.SetValue(key1, '', reg.REG_SZ,"C:\\ProgramData\\WCMS Scanner\\Scan.exe"+ " " f'"%1"') 
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)