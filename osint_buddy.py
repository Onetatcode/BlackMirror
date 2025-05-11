import os
import logging
from core import username_search, email_lookup, phone_lookup, domain_info, ip_lookup, social_discovery, reverse_image, dork_generator
from utils import banner, menu, handle_error
from logger import log_error

def main():
    while True:
        banner()
        menu()
        choice = input("Select an option (1-9): ")
        
        try:
            if choice == '1':
                username_search()
            elif choice == '2':
                email_lookup()
            elif choice == '3':
                phone_lookup()
            elif choice == '4':
                domain_info()
            elif choice == '5':
                ip_lookup()
            elif choice == '6':
                social_discovery()
            elif choice == '7':
                reverse_image()
            elif choice == '8':
                dork_generator()
            elif choice == '9':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        except Exception as e:
            log_error(f"Error in main loop: {str(e)}")
            handle_error()
        
        input("\nPress Enter to continue...")
        os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == '__main__':
    main()
