import paramiko

def algorithms(target):
    transort = paramiko.Transport((target, 22))
    transort.start_client()

    hex = transort.get_security_options().kex
    ciphers = transort.get_security_options().ciphers

    transort.close()

    return {
        "hex": hex,
        "ciphers": ciphers
    }