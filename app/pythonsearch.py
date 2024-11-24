import webbrowser
import requests

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
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            websites = response.text.strip().splitlines()
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
    while True:
        display_categories()
        
        category_choice = input("Enter your choice (a-e or z to close): ").lower()
        
        if category_choice == 'z':
            print("Closing the app.")
            break
        elif category_choice in ['a', 'b', 'c', 'd', 'e']:
            websites = read_websites_from_file(f"{category_choice}_search" if category_choice == 'a' else f"{category_choice}_productivity" if category_choice == 'b' else f"{category_choice}_hack_club" if category_choice == 'c' else f"{category_choice}_entertainment" if category_choice == 'd' else f"{category_choice}_gaming")
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
