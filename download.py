import os
import json 
from urllib.request import urlretrieve

def download(url, filename):
    # Download the file and save it in the current directory
    try:
        # Remove the file if it exists
        if os.path.exists(filename):
            os.remove(filename)
        # Download and save the file
        urlretrieve(url, filename)
        print(f"File '{filename}' downloaded successfully.")
    except Exception as e:
        print(f"An error occurred during downloading file {filename}: {e}")

url = "https://raw.githubusercontent.com/me2d09/LongHCPulse/refs/heads/master/LongHCPulse.py"
file = "LongHCPulse.py"
download(url,file)

