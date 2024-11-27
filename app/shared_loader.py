import requests

# URL to load category data
CATEGORIES_URL = "https://raw.githubusercontent.com/BennyGaming635/pythonsearch/main/app/categories/"

def load_categories():
    """Load categories dynamically from a GitHub repository."""
    category_files = {
        'a': 'a_search.txt',
        'b': 'b_productivity.txt',
        'c': 'c_hack_club.txt',
        'd': 'd_entertainment.txt',
        'e': 'e_gaming.txt'
    }
    
    categories = {}
    
    for category, filename in category_files.items():
        try:
            url = f"{CATEGORIES_URL}{filename}"
            response = requests.get(url)
            if response.status_code == 200:
                categories[category] = response.text.strip().split('\n')
            else:
                print(f"Failed to load {category}: {filename}")
        except Exception as e:
            print(f"Error loading {category}: {filename} - {e}")
    
    return categories
