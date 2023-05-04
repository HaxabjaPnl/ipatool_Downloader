import re
import urllib.request
import subprocess

def get_bundle_id(store_id):
    """Gets the bundle ID of an iOS app from the App Store.

    Args:
        store_id (str): The store ID of the app.

    Returns:
        str: The bundle ID of the app.
    """

    url = "https://itunes.apple.com/lookup?id=" + store_id

    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')

        result = re.search(r'"bundleId"\s*:\s*"([^"]+)"', data)
        if result:
            return result.group(1)
        else:
            return None
    except urllib.error.URLError as e:
        print(e)
        return None

def download_ipa(bundle_id):
    """Downloads the IPA file for an iOS app.

    Args:
        bundle_id (str): The bundle ID of the app.
    """
    email = input("input your Apple ID: ")
    auth_login_proc = subprocess.Popen(["ipatool", "auth", "login", "--email", email])
    auth_login_proc.wait()

    download_proc = subprocess.Popen(["ipatool", "download", "-b", bundle_id])
    download_proc.wait()

if __name__ == "__main__":
    store_id = input("input store id: ")
    bundle_id = get_bundle_id(store_id)
    print(f"bundleId: {bundle_id}")

    download_ipa(bundle_id)
