import pypdf
import os
import time
import itertools
import string
import sys

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
    print(f"{R}This tool is locked 🔐{W}")
    print(f"{G}To unlock this tool like subscribe n click on the bell 🔔{W}\n")
    print(f"{R}Redirecting you to Youtube app...{W}")
    
    # Visual Countdown (9.8.7.6.5.4.3.2.1)
    countdown_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for num in countdown_numbers:
        sys.stdout.write(f"{R}{num}... {W}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")
    
    # Redirecting directly to your channel link
    os.system("xdg-open https://youtube.com/@hackers_colony_termux?si=ARLURAWczQOy2mtC") 
    
    print(f"{G}-------------------------------------------------------{W}")
    input(f"{G}Then come back hit enter to unlock 🔓 : {W}")
    print(f"{G}-------------------------------------------------------{W}")

def brute_force_auto(pdf_file):
    print(f"{G}[*] Generating combinations for Auto-Attack...{W}")
    chars = string.ascii_lowercase + string.digits
    
    try:
        reader = pypdf.PdfReader(pdf_file)
    except Exception as e:
        print(f"{R}[!] Error reading PDF: {e}{W}")
        return

    for length in range(1, 5): 
        print(f"\n{R}[*] Testing passwords with length: {length}{W}")
        for p in itertools.product(chars, repeat=length):
            password = ''.join(p)
            
            sys.stdout.write(f"\r{R}[~] Trying: {password:<15}{W}")
            sys.stdout.flush()
            
            try:
                if reader.decrypt(password) > 0:
                    print(f"\n\n{G}[!!!] SUCCESS! Password Found: {password}{W}")
                    return
            except:
                continue
                
    print(f"\n{R}[-] Auto-Attack finished. Password not found.{W}")

def cracker():
    banner()
    start_training()
    banner() 
    
    pdf_file = input(f"{G}[?] Enter Path to Locked PDF: {W}")
    if not os.path.exists(pdf_file):
        print(f"{R}[!] File not found! Check the path again.{W}")
        return

    # Exact customized options format
    print(f"\n{G}[1] Add Your Passlist")
    print(f"[2] Use Auto Passlist{W}")
    choice = input(f"{G}Select Mode: {W}")
    
    if choice == '1':
        wordlist = input(f"{G}Enter Path to Wordlist: {W}")
        if not os.path.exists(wordlist):
            print(f"{R}[!] Wordlist file not found!{W}")
            return
            
        try:
            reader = pypdf.PdfReader(pdf_file)
            print(f"\n{G}[*] Scanning through custom wordlist...{W}")
            with open(wordlist, 'r', errors='ignore') as file:
                for password in file:
                    password = password.strip()
                    sys.stdout.write(f"\r{R}[~] Trying: {password:<15}{W}")
                    sys.stdout.flush()
                    try:
                        if reader.decrypt(password) > 0:
                            print(f"\n\n{G}[!!!] SUCCESS! Password Found: {password}{W}")
                            return
                    except: 
                        continue
            print(f"\n{R}[-] Password not found in your passlist.{W}")
        except Exception as e:
            print(f"{R}[!] Error: {e}{W}")
    else:
        brute_force_auto(pdf_file)

if __name__ == "__main__":
    cracker()
