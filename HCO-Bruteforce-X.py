import pypdf
import os
import time
import itertools
import string
import sys

# Advanced Hacker ANSI Colours
R = '\033[31m'   # Bright Red
G = '\033[32m'   # Bright Green
Y = '\033[33m'   # Bright Yellow
B = '\033[34m'   # Bright Blue
CY = '\033[36m'  # Cyan
W = '\033[0m'    # Reset

def lock_screen():
    os.system('clear')
    print(f"{R}======================================================={W}")
    print(f"{R}[!] THIS TOOL IS LOCKED 🔐{W}")
    print(f"{Y}[+] To unlock this tool: Like, Subscribe & click on the Bell icon 🔔{W}")
    print(f"{R}======================================================={W}\n")
    print(f"{B}[*] Redirecting you to YouTube app...{W}")
    
    # Precise Countdown: 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
    for num in range(9, -1, -1):
        sys.stdout.write(f"{R}{num}.{W}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")
    
    # Open YouTube channel link
    os.system("xdg-open 'https://youtube.com/@hackers_colony_termux?si=ARLURAWczQOy2mtC'") 
    
    print(f"{CY}-------------------------------------------------------{W}")
    input(f"{Y}[🔓] Then come back and hit ENTER to unlock the tool... {W}")
    print(f"{CY}-------------------------------------------------------{W}")

def bold_hacker_banner():
    os.system('clear')
    print(f"{R}")
    print("  _    _  _____  ____    _____                     _        _   _  ")
    print(" | |  | |/ ____|/ __ \\  |  __ \\                   | |      | | (_) | ")
    print(" | |__| | |    | |  | | | |__) | __ ___  _ __  ___| |_ ___ | |_ _| |_ ___  ")
    print(" |  __  | |    | |  | | |  _  / '__/ _ \\| '_ \\/ __| __/ _ \\| __| | __/ _ \\ ")
    print(" | |  | | |____| |__| | | | \\ \\ | | (_) | | | \\__ \\ || (_) | |_| | ||  __/ ")
    print(" |_|  |_|\\_____|\\____/  |_|  \\_|_|  \\___/|_| |_|___/\\__\\___/\\__|_|\\__\\___| ")
    print(f"                                   {Y}--- Coded by Azhar ---{W}")
    print(f"{B}==========================================================================={W}")
    print(f"{Y}          [!] HCO-BRUTEFORCE-X | VAULT BREAKER v1.0 [!]{W}")
    print(f"{B}==========================================================================={W}\n")

def fix_path(path_input):
    # Agar path direct 'storage/' se shuru ho raha hai, toh aage '/' add karega
    path = path_input.strip()
    if path.startswith("storage/"):
        path = "/" + path
    # Windows ke quotes (") ko clean karega agar copy-paste mein aa gaya ho
    path = path.replace('"', '').replace("'", "")
    return path

def brute_force_auto(pdf_file):
    print(f"\n{B}[*] Generating combinations for Auto Passlist...{W}")
    chars = string.ascii_lowercase + string.digits
    
    try:
        reader = pypdf.PdfReader(pdf_file)
    except Exception as e:
        print(f"{R}[!] Error reading PDF file structure: {e}{W}")
        return

    for length in range(1, 5): 
        print(f"\n{Y}[*] Active Bruteforce Layer -> Length: {length}{W}")
        for p in itertools.product(chars, repeat=length):
            password = ''.join(p)
            sys.stdout.write(f"\r{R}[~] Blasting: {password:<15}{W}")
            sys.stdout.flush()
            try:
                if reader.decrypt(password) > 0:
                    print(f"\n\n{G}[!!!] SUCCESS! UNLOCKED WITH PASSWORD: {password}{W}")
                    return
            except:
                continue
    print(f"\n{R}[-] Auto Passlist processing finished. Password not found.{W}")

def main_menu():
    lock_screen()   # 1. Pehle validation aur redirect lock chalega
    bold_hacker_banner()  # 2. Unlock hone ke baad hi bada bold text aur menu aayega
    
    print(f"{Y}============= MENU ============="{W})
    print(f"{B}[1] Add Your Passlist")
    print(f"[2] Use Auto Passlist{W}")
    print(f"{Y}================================{W}")
    choice = input(f"{CY}Select Mode (1/2): {W}").strip()
    
    if choice not in ['1', '2']:
        print(f"{R}[!] Invalid selection! Exiting...{W}")
        return
        
    # Option select hone ke baad hi file path maangega
    raw_path = input(f"\n{CY}[?] Enter Path to Locked PDF: {W}")
    pdf_file = fix_path(raw_path)
    
    if not os.path.exists(pdf_file):
        print(f"{R}[!] File not found! Path check karein: {pdf_file}{W}")
        print(f"{Y}[Tip] Ensure Termux has storage permission: run 'termux-setup-storage' first.{W}")
        return

    if choice == '1':
        raw_wl_path = input(f"{CY}[?] Enter Path to Wordlist: {W}")
        wordlist = fix_path(raw_wl_path)
        if not os.path.exists(wordlist):
            print(f"{R}[!] Passlist file not found at: {wordlist}{W}")
            return
            
        try:
            reader = pypdf.PdfReader(pdf_file)
            print(f"\n{B}[*] Processing Custom Passlist...{W}")
            with open(wordlist, 'r', errors='ignore') as file:
                for password in file:
                    password = password.strip()
                    sys.stdout.write(f"\r{R}[~] Testing: {password:<15}{W}")
                    sys.stdout.flush()
                    try:
                        if reader.decrypt(password) > 0:
                            print(f"\n\n{G}[!!!] SUCCESS! Password Found: {password}{W}")
                            return
                    except: 
                        continue
            print(f"\n{R}[-] Attack finished. Password not matching your list.{W}")
        except Exception as e:
            print(f"{R}[!] Error: {e}{W}")
    else:
        brute_force_auto(pdf_file)

if __name__ == "__main__":
    main_menu()
