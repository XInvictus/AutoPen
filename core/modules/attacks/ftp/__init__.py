from core.modules.attacks.ftp import anon, files
from core.modules.utils.general import get_banner
def ftp(target):
    target = target.replace("http://", "").split("/")[0]
    result = {}
    banner = get_banner(target, 21)

    print("[!] Banner: {}".format(banner))
    anonl  = anon.anon(target)
    print("[!] Anonymous: {}".format(anonl))
    files_ = files.files(target)
    print("[!] Files: {}".format(len(files_)))

    result["banner"] = banner
    result["anon"]   = anonl
    result["files"]  = files_

    return result  
