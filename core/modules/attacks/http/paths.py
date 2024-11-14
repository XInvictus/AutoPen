import requests
from core.modules.utils.general import load_file

def paths(target):
    result = []

    paths = load_file("core/assets/paths/paths.txt")

    for path in paths:
        url = f"{target}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                result.append(url)
        except requests.exceptions.RequestException:
            pass
    return result