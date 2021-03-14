# Context-Menu-Scanner
Windows Context Menu Scanner[WCMS] helps you scan suspicious files for malware with just a right-click.The scanner is integrated right into the Windows Context Menu so you can Scan the file quickly.

## How will it be helpful?
Anti-virus softwares are great but at the same time are complicated to use and they hog a lot of memory.An average user wants something faster and lighter.WCMS is capable of scanning over 500 files types(Be it an executable,a zip file,torrents or even an Image that you downloaded today) without slowing you down.Just right-click and the results appear instantly.

## How it Works?
Currently the scanner uses virustotal API to identify malware.When you right-click to Scan a file a lot is going on under the hood.The flowchart shown below puts it in simple words.
![Under The Hood Flowchart](https://github.com/Rutuj-Runwal/Context-Menu-Scanner/raw/main/WCMS%20Images/Under%20The%20Hood.jpg)

## Take a look
#### Scanning a File<br><br>
![Scanning A File](https://github.com/Rutuj-Runwal/Context-Menu-Scanner/raw/main/WCMS%20Images/ScanningAFile.jpg)
<br><br>
#### <b>*If the file Turns out to be Malicious it will be detected*</b><br>
![Result1](https://github.com/Rutuj-Runwal/Context-Menu-Scanner/raw/main/WCMS%20Images/ScanResult.jpg)
<br>
#### <b>And it will be Removed</b><br>
![File Delete](https://github.com/Rutuj-Runwal/Context-Menu-Scanner/raw/main/WCMS%20Images/AutoRemove.jpg)


### Resources
Virustotal API: [API Docs V3.0](https://developers.virustotal.com/v3.0/reference)<br>
Vt-py Python Library: [Vt-py](https://github.com/VirusTotal/vt-py)<br>
Generating md5 Checksum: [Get MD5 using Python](https://www.kite.com/python/answers/how-to-generate-an-md5-checksum-of-a-file-in-python)<br>
Adding a script to Context Menu: [Add to ContextMenu](https://www.youtube.com/watch?v=jS2LuG1p8Vw)<br>
cxFreeze: [Cx Freeze](https://pypi.org/project/cx-Freeze/)

## Future Development
- Adding Robust Offline Detection.
- Using Datasets to Predict never-before-seen Samples: [Kaggle Dataset](https://www.kaggle.com/nsaravana/malware-detection)
- Adding better offline Analysis techniques: [Techniques](https://storage.googleapis.com/kaggle-forum-message-attachments/1028064/17136/description.pdf)
- Further building the system using predictions via SKlearn

### How to Use?
Using the scanner is really simplified as this repo already contain ready to use Setups(created using [Cx Freeze](https://pypi.org/project/cx-Freeze/)) to deploy directly on your windows machines. Just [Click Here](https://github.com/Rutuj-Runwal/Context-Menu-Scanner/tree/main/Ready%20to%20use%20Binaries) and download both the files.Install the installer(Make sure to install it in the default path) then extract the RAR and run the executable present inside it(This executable adds the program to windows context menu).Done!,now right click on any file and you should now be able to see the "WCSM Scan" option there.
Feel free to start a new issue for this repo in case any problems are encountered.
