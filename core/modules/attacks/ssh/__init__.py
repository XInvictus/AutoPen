from core.modules.attacks.ssh import algorithms
from core.modules.utils.general import get_banner, FindCVE_NVD_NIST

def ssh(data):
    target = data["target"].replace("http://", "").split("/")[0]
    result = {}
    banner = get_banner(target, data["port"] if data["port"] else 22)
    print("[!] Banner: {}".format(banner))
    algo   = algorithms.algorithms(target)
    print("[!] Found {} algorithms".format(len(algo["hex"]) + len(algo["ciphers"])))

    cve = FindCVE_NVD_NIST(banner)

    result["banner"] = {
        "banner": banner,
        "cve": cve
    }
    result["algo"]   = algo

    return result