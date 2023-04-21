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

    os.system("ipatool auth login --email=your apple id email address here")
    os.system("ipatool download -b " + bundle_id)
else:
    print("bundleId not found.")
