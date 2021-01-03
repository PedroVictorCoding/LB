import os, sys

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



if __name__ == "__main__":
    os.system("clear")
    os.system("curl ifconfig.me")
    print(" - " + bc.WARNING + "Current IP" + bc.ENDC)
    print("Running TOR")
    os.system("torsocks python SearchLibGen.py")
