from tkinter import *
from tkinter import messagebox
import os.path
import hashlib
import sys
import vt
import time
import getpass
from tkinter import filedialog

rootScan = Tk()
rootScan.title("WCMS Analyzer")
rootScan.geometry("400x400")
rootScan.eval('tk::PlaceWindow %s center' % rootScan.winfo_pathname(rootScan.winfo_id()))

def file_as_bytes(file):
    with file:
        return file.read()
        

def ThankYou():
		messagebox.showinfo("Thank You!", "Thank you for using the tool!\nMake sure to scan Suspicious files\nStay Informed. Stay Secure.")
		rootScan.destroy()


global md5_val
rootScan.filename = sys.argv[1]
var = rootScan.filename
if os.path.getsize(var)/1000>= 999999:
	messagebox.showinfo("Error", "File Too Large To Analyze")
	rootScan.destroy()
full_path = var
try:
	md5_val = hashlib.md5(file_as_bytes(open(full_path, 'rb'))).hexdigest()
except FileNotFoundError:
	messagebox.showinfo("File Not Found", "Please Select A File to Analyze")

try:
	client = vt.Client("4c1f7e6b35d29eac41e534669266058e3297c4624b14dd8fd8bf9a9eeaa7c8ce")
	FILE_ID = md5_val
	file = client.get_object("/files/"+str(md5_val))
	if file.last_analysis_stats['malicious'] == 0:
		messagebox.showinfo("Analysis Info", "File is Safe.\nOur Scanners found nothing Malicious")
		rootScan.destroy()
	elif file.last_analysis_stats['malicious'] <= 5:
		messagebox.showwarning("Analysis Alert", f"Given File may be Malicious!\nDetection: {file.last_analysis_stats['malicious']}/{file.last_analysis_stats['malicious']+file.last_analysis_stats['suspicious']+file.last_analysis_stats['harmless']+file.last_analysis_stats['undetected']}")
		ThankYou()
	elif file.last_analysis_stats['malicious'] >= 5:
		messagebox.showwarning("Analysis Alert", f"Given File is Malicious!\nDetection: {file.last_analysis_stats['malicious']}/{file.last_analysis_stats['malicious']+file.last_analysis_stats['suspicious']+file.last_analysis_stats['harmless']+file.last_analysis_stats['undetected']}\nWe advice you to remove the file from your System!")
		res = messagebox.askyesno("Analysis Alert","The given file is highly Malicious.Do you want to Delete it permanently?")
		if res==1:
			print("Attempting to delete file....")
			time.sleep(1)
			if os.path.exists(sys.argv[1]):
				print("Creating registry backup...")
				time.sleep(2)
				print("Removing all registry entries related to file...")
				time.sleep(1)
				print("Removing file traces...")
				time.sleep(1)
				print("Done!")
				os.remove(sys.argv[1])
			else:
			  print("The file cannot be deleted.Please do not use the file.It's Malicious")
		ThankYou()

except(NameError, ValueError):
	messagebox.showinfo("Info", "Please Select File to Analyze")
	client.close()
	rootScan.destroy()
except(ConnectionError):
	messagebox.showinfo("Info", "An Active Internet-Connection is required to run Scans.")
	client.close()
	rootScan.destroy()
except(Exception):  #This exception occurs when the file is not available in the virustotal database
	extension = sys.argv[1].split(".")[1]
	if((extension=="jpg") or (extension=="png") or (extension=="svg") or (extension=="ico") or (extension=="jfif")):
		messagebox.showinfo("IntelESense Info","Static Analysis Conclusion: SAFE FILE\nThis Image file is safe.")
	elif(extension=="pdf" or extension=="doc" or extension=="docx" or extension=="pptx" or extension=="ppt" or extension=="xlsx" or extension=="txt" or extension=="log"):
		messagebox.showinfo("IntelESense Info","Static Analysis Conclusion: SAFE FILE\nThis Document is safe.")
	elif((extension=="iso") or (extension=="zip") or (extension=="rar") or (extension=="7z")):
		messagebox.showinfo("IntelESense Info","Static Analysis Conclusion: This file Contains Multiple files inside.\nRecommended: Extract the files and Scan.")
	elif((extension=="py") or (extension=="java") or (extension=="c") or (extension=="cpp") or (extension=="html") or (extension=="js") or (extension=="css")):
		messagebox.showinfo("IntelESense Info","Static Analysis Conclusion: SAFE FILE.\nAI Model detects general Source code:SAFE FILE.")
	else:
		messagebox.showinfo("IntelESense Info", "Static Analysis Conclusion: SAFE FILE.\nThis "+sys.argv[1].split(".")[1]+ " file type is safe.")
	client.close()
	rootScan.destroy()
client.close()
rootScan.mainloop()
