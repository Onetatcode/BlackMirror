import requests
import webbrowser
from config import base_urls
import logging
import threading

# Setup Logging for OSINT operations
logging.basicConfig(filename="osint_buddy.log", level=logging.INFO)

def log_action(action):
    logging.info(action)

def username_search():
    username = input("Enter username to search: ")
    platforms = [
        f"{base_urls['github']}{username}",
        f"{base_urls['reddit']}{username}",
        f"{base_urls['twitter']}{username}",
        f"{base_urls['instagram']}{username}/",
        f"{base_urls['tiktok']}{username}"
    ]
    def search_platform(url):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"[+] Found: {url}")
                log_action(f"Found username {username} on {url}")
            else:
                print(f"[-] Not Found: {url}")
        except Exception as e:
            print(f"[!] Error checking: {url}")
            log_action(f"Error checking {url}: {str(e)}")
    
    threads = []
    for url in platforms:
        t = threading.Thread(target=search_platform, args=(url,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def email_lookup():
    email = input("Enter email to lookup: ")
    print(f"[*] Checking with haveibeenpwned... Link: https://haveibeenpwned.com/unifiedsearch/{email}")
    log_action(f"Checked email {email} on haveibeenpwned")

def phone_lookup():
    number = input("Enter phone number (with country code): ")
    print(f"[*] Try Google dork: \"intext:{number}\"")
    print(f"Link: https://www.google.com/search?q=intext:{number}")
    log_action(f"Checked phone number {number}")

def domain_info():
    domain = input("Enter domain: ")
    print(f"[*] WHOIS Info: https://who.is/whois/{domain}")
    print(f"[*] DNS Records: https://dnsdumpster.com")
    print(f"[*] Tech Stack: https://builtwith.com/{domain}")
    log_action(f"Checked domain info for {domain}")

def ip_lookup():
    ip = input("Enter IP address: ")
    print(f"[*] Geo Info: https://ipinfo.io/{ip}")
    print(f"[*] Abuse Check: https://www.abuseipdb.com/check/{ip}")
    log_action(f"Checked IP {ip}")

def social_discovery():
    name = input("Enter name or alias: ")
    print(f"[*] Try this Google dork: \"{name}\" site:linkedin.com OR site:facebook.com OR site:twitter.com")
    log_action(f"Searched social media for {name}")

def reverse_image():
    url = input("Paste image URL: ")
    print(f"[*] Reverse Search Options:")
    print(f"Google: https://lens.google.com/uploadbyurl?url={url}")
    print(f"TinEye: https://tineye.com/search?url={url}")
    print(f"Yandex: https://yandex.com/images/search?rpt=imageview&url={url}")
    log_action(f"Reverse image search for {url}")

def dork_generator():
    target = input("Enter target keyword (e.g., example.com): ")
    print(f"[*] Example Dorks:")
    print(f"site:{target} ext:pdf")
    print(f"site:{target} inurl:admin")
    print(f"site:{target} intitle:index.of")
    print(f"site:{target} intext:password")
    log_action(f"Generated Google dorks for {target}")

def geolocation_lookup():
    ip = input("Enter IP address for geolocation lookup: ")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print(f"[*] Geolocation Info for {ip}: {data}")
        log_action(f"Geolocation lookup for IP {ip}: {data}")
    except Exception as e:
        print(f"[!] Error: {str(e)}")
