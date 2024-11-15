import socket, requests, urllib
from bs4 import BeautifulSoup

def format_target(target):
    if target.startswith("http://"):
        return target
    else:
        return f"http://{target}"
    
def get_banner(target, port):
    s = socket.socket()
    s.settimeout(5)
    s.connect((target, int(port)))
    banner = s.recv(1024).decode().strip()
    s.close()

    return banner

def load_file(file):
    return [line.strip() for line in open(file)]

def FindCVE_NVD_NIST(search):
    vulns = []
    dist = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={}&search_type=all&isCpeNameSearch=false".format(urllib.parse.quote(search))
    r = requests.get(dist)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        vulns.append(a['href'] if "detail" in a['href'] else None)
    exploits = [vuln for vuln in vulns if vuln is not None]

    return exploits