import os
import subprocess
import requests

# Apni cookies yahan update karein
COOKIES = {
    'sessionid': 'e30:1xDGkh:yXSNMXuSFowlWfb2Ex4-uZ-xuh3xBYY...', # Apni sessionid ki value yahan dalein
    'gfgUserName': 'dushyantcht7h5%2F...'                         # Apni gfgUserName ki value yahan dalein
}

def fetch_and_sync():
    print("GeeksforGeeks se submissions fetch karne ki koshish ki ja rahi hai...")
    
    # Languages ke folders ensure karein
    languages = ["Python", "Cpp", "Java"]
    for lang in languages:
        os.makedirs(lang, exist_ok=True)
        
    # Git commit aur push
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Sync GFG submissions via cookie script"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Successfully GitHub par push ho gaya!")
    except Exception as e:
        print(f"Error aayi: {e}")

if __name__ == "__main__":
    fetch_and_sync()