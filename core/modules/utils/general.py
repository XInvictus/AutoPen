import socket

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