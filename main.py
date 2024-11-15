import argparse, json
from core.modules.utils import general
from core.modules.attacks import http, ftp, ssh

class Main:
    def __init__(self):
        self.attacks = {
            "http": http.http,
            "ftp": ftp.ftp,
            "ssh": ssh.ssh
        }
        
        self.args = argparse.ArgumentParser()

        self.args.add_argument("-t", "--target", help="Target host")
        self.args.add_argument("-p", "--port", help="Target port", type=int)
        self.args.add_argument("-a", "--attack", help="Attack type", choices=["http", "ftp", "ssh"])

        self.args = self.args.parse_args()

        if not self.args.attack or not self.args.target:
            exit(1)
        
        self.target = general.format_target(self.args.target)
        self.attack = self.args.attack
        self.port   = self.args.port


    def main(self):
        print(f"Attacking {self.target} with {self.attack}")
        args = {
            "target": self.target,
            "port": int(self.port) if self.port else None
        }
        result = self.attacks[self.attack](args)

        print(json.dumps(result, indent=4))

if __name__ == '__main__':
    main = Main()
    main.main()