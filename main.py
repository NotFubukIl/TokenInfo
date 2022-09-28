import requests
from pystyle import Colors, Colorate

class Allah:
    def main():
        token = input("> Token: ")
        al = Allah.getMainInfos(token)
        if al == False: return print(Colorate.Horizontal(Colors.yellow_to_red, f"Token Isn't Valid", 1))
        Settings = Allah.GetSettingsInfos(token)
        Connections = Allah.GetConnections(token)
        kdo = Allah.GetKdo(token)
        for p, f in al.items(): 
            if not f: f = None
            print(Colorate.Horizontal(Colors.yellow_to_red, f"[{p}]: {f}", 1))
        print(" ")  
        for p, f in Settings.items(): 
            if not f: f = None
            print(Colorate.Horizontal(Colors.yellow_to_red, f"[{p}]: {f}", 1))
        print(" ") 
        for p in Connections: 
            if not f: f = None
            for n, z in p.items():
                print(Colorate.Horizontal(Colors.yellow_to_red, f"[{n}]: {z}", 1))
        print(" ")
        for p in kdo: 
            if not f: f = None
            for n, z in p.items():
                print(Colorate.Horizontal(Colors.yellow_to_red, f"[{n}]: {z}", 1))
        print(" ")
    def getMainInfos(token):
        j = requests.get("https://discord.com/api/v9/users/@me", headers = {"authorization": token}).json()
        if "message" in j: return False
        else: return j
    def GetSettingsInfos(token):
        j = requests.get("https://discord.com/api/v9/users/@me/settings", headers = {"authorization": token}).json()
        if "message" in j: return False
        else: return j
    def GetConnections(token):
        j = requests.get("https://discordapp.com/api/v9/users/@me/connections", headers = {"authorization": token}).json()
        if "message" in j: return False
        else: return j
    def GetKdo(token):
        j = requests.get("https://discord.com/api/v8/users/@me/entitlements/gifts", headers = {"authorization": token}).json()
        if "message" in j: return False
        else: return j

if __name__ == "__main__": 
    Allah.main()
    input("")
