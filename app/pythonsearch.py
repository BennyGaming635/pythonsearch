import webbrowser
import subprocess
import sys

# Function to check if the requests library is installed
def check_and_install_requests():
    try:
        import requests
    except ImportError:
        print("The 'requests' library is not installed.")
        install_choice = input("Would you like to install it now? (y/n): ").lower()
        if install_choice == 'y':
            print("Installing 'requests'...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
            print("'requests' has been installed. Please restart the script.")
            sys.exit()
        else:
            print("Continuing without the 'requests' library. Limited functionality may be available.")
            return False
    return True

# Base URL for raw files on GitHub
GITHUB_RAW_URL = "https://raw.githubusercontent.com/BennyGaming635/pythonsearch/main/app/categories/"

# Display categories
def display_categories():
    print("Choose a category by entering the corresponding letter:")
    print("a - Search")
    print("b - Productivity")
    print("c - Hack Club")
    print("d - Entertainment")
    print("e - Gaming")
    print("z - Close")

# Fetch websites from a raw GitHub file
def read_websites_from_file(category):
    # Construct the URL for the raw .txt file from the GitHub repository
    url = f"{GITHUB_RAW_URL}{category}.txt"
    
    try:
        import requests
        response = requests.get(url)
        
        # Debugging: Print the status code and response text
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text[:200]}...")  # Print first 200 chars of the response for debugging
        
        # Check if the request was successful
        if response.status_code == 200:
            websites = response.text.strip().splitlines()
            if not websites:
                print("Warning: No websites found in the file.")
            return websites
        else:
            print(f"Failed to fetch category {category}.txt. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching category {category}.txt: {e}")
        return []

# Open the website based on user input
def open_website(website_index, websites):
    if 1 <= website_index <= len(websites):
        webbrowser.open(websites[website_index - 1])
        print(f"Opening {websites[website_index - 1]}...")
    else:
        print("Invalid choice. Please enter a valid number.")

# Main function
def main():
    # Check if requests library is installed
    if not check_and_install_requests():
        return

    while True:
        display_categories()
        
        category_choice = input("Enter your choice (a-e or z to close): ").lower()
        
        if category_choice == 'z':
            print("Closing the app.")
            break
        elif category_choice in ['a', 'b', 'c', 'd', 'e']:
            # Formulate category name, based on the user's choice
            category_map = {
                'a': 'a_search',
                'b': 'b_productivity',
                'c': 'c_hack_club',
                'd': 'd_entertainment',
                'e': 'e_gaming'
            }
            category_file = category_map[category_choice]
            
            websites = read_websites_from_file(category_file)
            
            if websites:
                print(f"\nList of websites for the {category_choice} category:")
                for idx, website in enumerate(websites, start=1):
                    print(f"{idx}. {website}")
                
                try:
                    website_choice = int(input("\nEnter the number of the website you want to visit: "))
                    open_website(website_choice, websites)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("No websites found for this category.")
        else:
            print("Invalid input. Please select a valid category.")

if __name__ == "__main__":
    main()
