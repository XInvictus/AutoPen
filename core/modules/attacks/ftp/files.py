from ftplib import FTP

def files(target):
    try:
        with FTP(target) as ftp:
            ftp.login("anonymous", "anonymous")
            return ftp.nlst()
    except:
        return None