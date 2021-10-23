import requests
from colorama import Fore
from os import *
token = input(Fore.GREEN + "Insert A Token: ")

req = requests.get("https://discord.com/api/v9/users/@me", headers = {"authorization": token})

user = req.json()

if not 'message' in user:
    print(Fore.BLUE, f"""
[USERNAME]: {user["username"]}#{user["discriminator"]}
[ID]: {user["id"]}
[AVATAR URL]: https://cdn.discordapp.com/avatars/{user["id"]}/{user["avatar"]}
[Public FLAGS]: {user["public_flags"]}
[EMAIL]: {user["email"]}
[Phone ?]: {user["phone"]}
[Biographie]: {user["bio"]}
[Token]: {token}
[By Not.Fubukii]""", Fore.WHITE)
else: print(Fore.RED,"INVALID TOKEN", Fore.WHITE)
