import requests
from core.modules.utils.general import load_file

def lfie(target):
    result = []

    params = load_file("core/assets/inclusion/params.txt")
    files  = load_file("core/assets/inclusion/files.txt")

    for param in params:
        for file in files:
            url = f"{target}{param}{file}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    result.append(url)
            except requests.exceptions.RequestException:
                pass
    return result