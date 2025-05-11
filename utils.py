import os
import logging
from colorama import Fore, Style

def banner():
    print(Fore.CYAN + """
    =========================
         OSINT-Buddy
    =========================
    """ + Style.RESET_ALL)

def menu():
    print("""
1. Username Search
2. Email Lookup
3. Phone Number Info
4. Domain Info
5. IP Address Lookup
6. Social Media Discovery
7. Reverse Image Search
8. Google Dork Generator
9. Geolocation Lookup
10. Exit
""")

def setup_logging():
    logging.info("OSINT-Buddy started")
