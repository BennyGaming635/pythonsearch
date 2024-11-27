import os
import requests
import webbrowser
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Constants
EXTENSION_URL_BASE = "https://raw.githubusercontent.com/BennyGaming635/pythonsearch/main/app/addons/"
EXTENSIONS = {
    "googlely": "googlely.py",
    "gui": "gui.py"
}
SHARED_LOADER_URL = "https://raw.githubusercontent.com/BennyGaming635/pythonsearch/main/app/shared_loader.py"
CATEGORIES_URL_BASE = "https://raw.githubusercontent.com/BennyGaming635/pythonsearch/main/app/categories/"
CATEGORY_FILES = {
    'a': 'a_search.txt',
    'b': 'b_productivity.txt',
    'c': 'c_hack_club.txt',
    'd': 'd_entertainment.txt',
    'e': 'e_gaming.txt'
}

ASCII_ART = f"""
{Fore.GREEN}
$$$$$$$\              $$\     $$\                            $$$$$$\                                          $$\       
$$  __$$\             $$ |    $$ |                          $$  __$$\                                         $$ |      
$$ |  $$ |$$\   $$\ $$$$$$\   $$$$$$$\   $$$$$$\  $$$$$$$\  $$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\  
$$$$$$$  |$$ |  $$ |\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ \$$$$$$\  $$  __$$\  \____$$\ $$  __$$\ $$  _____|$$  __$$\ 
$$  ____/ $$ |  $$ |  $$ |    $$ |  $$ |$$ /  $$ |$$ |  $$ | \____$$\ $$$$$$$$ | $$$$$$$ |$$ |  \__|$$ /      $$ |  $$ |
$$ |      $$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |$$   ____|$$  __$$ |$$ |      $$ |      $$ |  $$ |
$$ |      \$$$$$$$ |  \$$$$  |$$ |  $$ |\$$$$$$  |$$ |  $$ |\$$$$$$  |\$$$$$$$\ \$$$$$$$ |$$ |      \$$$$$$$\ $$ |  $$ |
\__|       \____$$ |   \____/ \__|  \__| \______/ \__|  \__| \______/  \_______| \_______|\__|       \_______|\__|  \__|
          $$\   $$ |                                                                                                    
          \$$$$$$  |                                                                                                    
           \______/                                                                                                     
{Style.RESET_ALL}
{Fore.YELLOW}{Style.BRIGHT}Now in {Fore.CYAN}C{Fore.MAGENTA}O{Fore.BLUE}L{Fore.GREEN}O{Fore.RED}U{Fore.YELLOW}R!
"""

# Function to load categories
def load_categories():
    """Load categories and websites from the GitHub repository."""
    categories = {}
    for key, filename in CATEGORY_FILES.items():
        try:
            url = f"{CATEGORIES_URL_BASE}{filename}"
            response = requests.get(url)
            if response.status_code == 200:
                categories[key] = response.text.strip().split('\n')
            else:
                print(Fore.RED + f"Failed to load category {key}: {filename}.")
        except Exception as e:
            print(Fore.RED + f"Error loading category {key}: {filename}. {e}")
    return categories

# Function to check and install shared_loader.py if missing
def check_and_download_shared_loader():
    """Check if shared_loader.py exists, download if missing."""
    if not os.path.exists('shared_loader.py'):
        print(Fore.YELLOW + "shared_loader.py not found. Downloading now...")
        try:
            response = requests.get(SHARED_LOADER_URL)
            with open('shared_loader.py', 'w') as file:
                file.write(response.text)
            print(Fore.GREEN + "shared_loader.py downloaded successfully!")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Failed to download shared_loader.py: {e}")
            exit()

# Check if the `requests` library is installed
def check_and_install_requests():
    """Check if requests is installed, if not, prompt for installation."""
    try:
        import requests
    except ImportError:
        user_input = input(Fore.RED + "The 'requests' library is missing. Would you like to install it? (y/n): ")
        if user_input.lower() == 'y':
            os.system("pip install requests")
            print(Fore.GREEN + "requests library installed successfully!")
        else:
            print(Fore.YELLOW + "Skipping requests installation. The app may not work without it.")
            
# Main App Logic
def main():
    print(ASCII_ART)
    print(Fore.YELLOW + "Welcome to the Web Launcher!")
    
    # Check for requests library
    check_and_install_requests()
    
    # Check and download shared_loader if missing
    check_and_download_shared_loader()
    
    # Load categories
    categories = load_categories()

    # Menu loop
    while True:
        print(Fore.YELLOW + "\nSelect a category:")
        print(Fore.CYAN + "a - Search\nb - Productivity\nc - Hack Club\nd - Entertainment\ne - Gaming\nz - Close")
        
        user_input = input(Fore.GREEN + "Enter choice: ").lower()
        
        if user_input == 'z':
            print(Fore.YELLOW + "Goodbye!")
            break
        
        if user_input in categories:
            print(Fore.CYAN + f"\nOpening websites in category '{user_input}':")
            for index, website in enumerate(categories[user_input], start=1):
                print(Fore.YELLOW + f"{index}. {website}")
            
            site_choice = input(Fore.GREEN + "\nEnter the number of the site to visit (or press Enter to exit): ")
            if site_choice.isdigit() and 1 <= int(site_choice) <= len(categories[user_input]):
                webbrowser.open(categories[user_input][int(site_choice) - 1])
            else:
                print(Fore.RED + "Invalid choice. Returning to menu.")
        else:
            print(Fore.RED + "Invalid category selection. Please try again.")

# Run the main function
if __name__ == '__main__':
    main()
