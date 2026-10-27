from colorama import Fore, Style

def show_banner():
    print(Fore.MAGENTA + r"""
 _     _       _     _____                    
| |   (_)_ __ | | __|  ___|__  _ __ __ _  ___ 
| |   | | '_ \| |/ /| |_ / _ \| '__/ _` |/ _ \
| |___| | | | |   < |  _| (_) | | | (_| |  __/
|_____|_|_| |_|_|\_\_|  \___/|_|  \__, |\___|
                                  |___/
""" + Style.RESET_ALL)
    print(Fore.CYAN + "       URL SHORTENER • TERMUX CLI" + Style.RESET_ALL)
    print(Fore.WHITE + "-" * 45 + Style.RESET_ALL)
