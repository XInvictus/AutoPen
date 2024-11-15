# Auto Pen
> An automatic penetration testing tool

## Installation guide
1. Ensure you have python3+ for this to work
2. Clone the repo locally with `git clone https://github.com/XInvictus/AutoPen`
3. Change your directory to the folder with `cd AutoPen`
4. Run `pip install -r requrements.txt` to install the requirements
5. You have succesfully installed this software !!

## Usage

### Help
```
usage: main.py [-h] [-t TARGET] [-a {http,ftp,ssh}]

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target host
  -a {http,ftp,ssh}, --attack {http,ftp,ssh}
                        Attack type
```
### HTTP
This is a mode for testing http applications
```
(env) jwe0@ubuntu:~/Desktop/Side/AutomaticPenetration$ python3 main.py --target blog.thm --attack http
Attacking http://blog.thm with http
[!] Discovered 0 subdomains
[!] Discovered 3 login pages
[!] Discovered 1 lfie pages
[!] Discovered 2 paths
{
  "subdomains": [],
  "login": [
    "http://blog.thm/admin..",
    "http://blog.thm/login..",
    "http://blog.thm/wp-admin.."
  ],
  "lfie": [
    "http://blog.thm?file=/etc/passwd"
  ],
  "paths": [
    "http://blog.thm/robots.txt",
    "http://blog.thm//wp-json/wp/v2/users"
  ]
}
```
### FTP
Mode for testing FTP servers
```
(env) jwe0@ubuntu:~/Desktop/Side/AutomaticPenetration$ python3 main.py --target test.rebex.net --attack ftp
Attacking http://test.rebex.net with ftp
{
    "banner": "220-Welcome to test.rebex.net!\r\n    See https://test.rebex.net/ for more information and terms of use.\r\n220 If you don't have an account, log in as 'anonymous' or 'ftp'.",
    "anon": "220-Welcome to test.rebex.net!\n    See https://test.rebex.net/ for more information and terms of use.\n220 If you don't have an account, log in as 'anonymous' or 'ftp'.",
    "files": [
        "pub",
        "readme.txt"
    ]
}
```
### SSH
Mode for testing SSH servers
```
(env) jwe0@ubuntu:~/Desktop/Side/AutomaticPenetration$ python3 main.py --target 192.168.1.92 --attack ssh
Attacking http://192.168.1.92 with ssh
[!] Banner: SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u3
[!] Found 19 algorithms
{
    "banner": {
        "banner": "SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u3",
        "cve": []
    },
    "algo": {
        "hex": [
            "curve25519-sha256@libssh.org",
            "ecdh-sha2-nistp256",
            "ecdh-sha2-nistp384",
            "ecdh-sha2-nistp521",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group-exchange-sha256",
            "diffie-hellman-group14-sha256",
            "diffie-hellman-group-exchange-sha1",
            "diffie-hellman-group14-sha1",
            "diffie-hellman-group1-sha1"
        ],
        "ciphers": [
            "aes128-ctr",
            "aes192-ctr",
            "aes256-ctr",
            "aes128-cbc",
            "aes192-cbc",
            "aes256-cbc",
            "3des-cbc",
            "aes128-gcm@openssh.com",
            "aes256-gcm@openssh.com"
        ]
    }
}
```

## Legal
This software was designed for usage in proper penetration testing. Under NO CIRCUMSTANCES must you use this software against non permitting targets, this is a cybercrime and can result in serious legal repurcussion.

## Acknowledgements
```Jwe0 - Lead Dev```