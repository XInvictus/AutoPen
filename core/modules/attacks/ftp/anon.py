from ftplib import FTP

def anon(target):
    try:
        with FTP(target) as ftp:
            ftp.login("anonymous", "anonymous")
        return ftp.getwelcome()
    except:
        return None