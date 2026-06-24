import pikepdf
import os
import time
import itertools
import string

# ANSI Colours
R = '\033[31m' # Red
G = '\033[32m' # Green
W = '\033[0m'  # White/Reset

def banner():
    os.system('clear')
    print(f"{R}")
    print("  _    _  _____  ____    _____                     _        _   _  ")
    print(" | |  | |/ ____|/ __ \\  |  __ \\                   | |      | | (_) | ")
    print(" | |__| | |    | |  | | | |__) | __ ___  _ __  ___| |_ ___ | |_ _| |_ ___  ")
    print(" |  __  | |    | |  | | |  _  / '__/ _ \\| '_ \\/ __| __/ _ \\| __| | __/ _ \\ ")
    print(" | |  | | |____| |__| | | | \\ \\ | | (_) | | | \\__ \\ || (_) | |_| | ||  __/ ")
    print(" |_|  |_|\\_____|\\____/  |_|  \\_|_|  \\___/|_| |_|___/\\__\\___/\\__|_|\\__\\___| ")
    print(f"                                   {G}--- Coded by Azhar ---{W}")
    print(f"{G}==========================================================================={W}")
    print(f"{R}          [!] HCO-BRUTEFORCE-X | VAULT BREAKER v1.0 [!]{W}")
    print(f"{G}==========================================================================={W}\n")

def start_training():
    print(f"{R}[!] Security Protocol: Mandatory Training Required.{W}")
    time.sleep(2)
    os.system("xdg-open youtube://channel/YOUR_CHANNEL_ID") 
    input(f"\n{G}[!] Watch the tutorial and hit ENTER to unlock the vault...{W}")

def brute_force_auto(pdf_file):
    print(f"{G}[*] Generating combinations for Auto-Attack...{W}")
    chars = string.ascii_lowercase + string.digits
    for length in range(1, 5): 
        for p in itertools.product(chars, repeat=length):
            password = ''.join(p)
            try:
                with pikepdf.open(pdf_file, password=password) as pdf:
                    print(f"\n{G}[!!!] SUCCESS! Password Found: {password}{W}")
                    return
            except:
                continue
    print(f"{R}[-] Auto-Attack failed.{W}")

def cracker():
    banner()
    start_training()
    banner()
    
    pdf_file = input(f"{G}[?] Enter Path to Locked PDF: {W}")
    if not os.path.exists(pdf_file):
        print(f"{R}[!] File not found!{W}")
        return

    print(f"\n{G}[1] Use Custom Wordlist")
    print(f"[2] Run Auto-Attack{W}")
    choice = input(f"{G}Select Mode: {W}")
    
    if choice == '1':
        wordlist = input(f"{G}Enter Path to Wordlist: {W}")
        if not os.path.exists(wordlist):
            print(f"{R}[!] Wordlist file not found!{W}")
            return
        with open(wordlist, 'r', errors='ignore') as file:
            for password in file:
                password = password.strip()
                try:
                    with pikepdf.open(pdf_file, password=password) as pdf:
                        print(f"\n{G}[!!!] SUCCESS! Password Found: {password}{W}")
                        return
                except: continue
    else:
        brute_force_auto(pdf_file)

if __name__ == "__main__":
    cracker()
