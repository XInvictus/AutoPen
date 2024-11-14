import requests
from core.modules.utils.general import load_file

def logins(target):
    result = []
    
    file_types = load_file("core/assets/logins/file_types.txt") 
    paths      = load_file("core/assets/logins/paths.txt")

    for path in paths:
        for file_type in file_types:
            url = f"{target}/{path}.{file_type}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    result.append(url)
            except requests.exceptions.RequestException:
                pass
    return result