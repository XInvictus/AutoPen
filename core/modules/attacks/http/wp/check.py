import requests

def verify(target):
    page = requests.get(target)
    if 'meta name="generator" content="WordPress ' in page.text:
        return True
    return False