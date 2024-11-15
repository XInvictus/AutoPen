from core.modules.attacks.ftp import anon, files
from core.modules.utils.general import get_banner, FindCVE_NVD_NIST
def ftp(data):
    target = data["target"].replace("http://", "").split("/")[0]
    result = {}
    banner = get_banner(target, data["port"] if data["port"] else 21)

    print("[!] Banner: {}".format(banner))
    anonl  = anon.anon(target)
    print("[!] Anonymous: {}".format(anonl))
    files_ = files.files(target)
    print("[!] Files: {}".format(len(files_)))

    cve = FindCVE_NVD_NIST(banner)

    result["banner"] = {
        "banner": banner,
        "cve": cve
    }
    result["anon"]   = anonl
    result["files"]  = files_

    return result  
