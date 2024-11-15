from core.modules.attacks.http import domains, logins, inclusion, paths
from core.modules.attacks.http.wp import check

def http(data):
    result = {}
    target = data["target"][:-1] if target[-1] == "/" else target
    if check.verify(target):
        result["wp"] = True
    else:
        result["wp"] = False
    subdomains = domains.domains(target)
    print("[!] Discovered {} subdomains".format(len(subdomains)))
    login      = logins.logins(target)
    print("[!] Discovered {} login pages".format(len(login)))
    lfie       = inclusion.lfie(target)
    print("[!] Discovered {} lfie pages".format(len(lfie)))
    paths_      = paths.paths(target)
    print("[!] Discovered {} paths".format(len(paths_)))

    result["subdomains"] = subdomains
    result["login"]      = login
    result["lfie"]       = lfie
    result["paths"]      = paths_

    return result    