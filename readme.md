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
## Legal
This software was designed for usage in proper penetration testing. Under NO CIRCUMSTANCES must you use this software against non permitting targets, this is a cybercrime and can result in serious legal repurcussion.

## Acknowledgements
```Jwe0 - Lead Dev```