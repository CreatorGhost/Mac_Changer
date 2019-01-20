import subprocess
import re
import optparse
def get_mac():
    prs = optparse.OptionParser()
    prs.add_option("-i", "--interface", dest="intr", help="Iterface")
    prs.add_option("-m", "--mac", dest="mac", help="Mac Address ")
    return prs.parse_args()

def check_mac(intr):
    output = subprocess.check_output("ifconfig " + intr, shell=True)
    new = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    return new


def change_mac(intr,mac):
   subprocess.call(["ifconfig", intr, "down"])
   subprocess.call(["ifconfig", intr, "hw", "ether", mac])
   subprocess.call(["ifconfig", intr, "up"])

print ('''
.___  ___.      ___       ______ 
|   \/   |     /   \     /      |
|  \  /  |    /  ^  \   |  ,----'
|  |\/|  |   /  /_\  \  |  |     
|  |  |  |  /  _____  \ |  `----.
|__|  |__| /__/     \__\ \______|
                                 
  ______  __    __       ___      .__   __.   _______  _______ .______      
 /      ||  |  |  |     /   \     |  \ |  |  /  _____||   ____||   _  \     
|  ,----'|  |__|  |    /  ^  \    |   \|  | |  |  __  |  |__   |  |_)  |    
|  |     |   __   |   /  /_\  \   |  . `  | |  | |_ | |   __|  |      /     
|  `----.|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |____ |  |\  \----.
 \______||__|  |__| /__/     \__\ |__| \__|  \______| |_______|| _| `._____|
''')
try :
    (opn, arg) = get_mac()
    intr = opn.intr
    mac = opn.mac
    current = check_mac(intr)
    print ("[+] The current mac address is " + current.group(0))
    ck = mac
    print("[+] Changing mac of " + intr + " to " + mac)
    change_mac(intr, mac)
    current = check_mac(intr)
    newmac = current.group(0)
    if ck == newmac:
        print ("[+] Mac Successfully changed ...")
    else:
        print ("[-] Error Changing The MAC....")

    print ("[+] The current mac address is " + newmac)
except Exception:
    print ("[+] Usage 'python mac_changer.py --help '")
