import socket
from core.modules.utils.general import load_file

def domains(target):
    result = []
    target = target.replace("http://", "").split("/")[0]
    
    subdomains = load_file("core/assets/domains/subdomains.txt")

    for subdomain in subdomains:
        url = f"{subdomain}.{target}"
        try:
            socket.gethostbyname(url)
            result.append(url)
        except socket.gaierror:
            pass
    return result