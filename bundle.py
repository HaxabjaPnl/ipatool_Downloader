import re
import urllib.request
import os

url = "https://itunes.apple.com/lookup?id="
number = input("input store id: ")

full_url = url + number

response = urllib.request.urlopen(full_url)
data = response.read().decode('utf-8')

result = re.search(r'"bundleId"\s*:\s*"([^"]+)"', data)
if result:
    bundle_id = result.group(1)
    print(f"bundleId: {bundle_id}")

    auth_login_proc = subprocess.Popen(["ipatool", "auth", "login", "--email=your apple id email address here"])
    auth_login_proc.wait()

    download_proc = subprocess.Popen(["ipatool", "download", "-b", bundle_id])
    download_proc.wait()
else:
    print("bundleId not found.")
