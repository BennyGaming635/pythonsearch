import os
import requests

def search_websites(query, categories):
    """Search for websites matching the query in all categories."""
    suggestions = []
    for category, websites in categories.items():
        for website in websites:
            if query.lower() in website.lower():
                suggestions.append(website)
    
    return suggestions

def googlely_search(categories):
    """Run the Google-like search functionality."""
    query = input("Enter a search query: ")
    results = search_websites(query, categories)
    
    if results:
        print("Suggested websites:")
        for result in results:
            print(result)
    else:
        print("No results found.")
