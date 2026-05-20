from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def parse_amazon_data():
    print("Starting the smart scraper...")
    
    try:
        print("Reading the local HTML file...")
        with open("amazon_page.html", "r", encoding="utf-8") as file:
            html_content = file.read()
    except FileNotFoundError:
        print("Error: Could not find 'amazon_page.html'.")
        return

    print("File loaded. Parsing the data...")
    soup = BeautifulSoup(html_content, 'html.parser')
    
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    if len(product_containers) == 0:
        product_containers = soup.find_all('div', class_='s-result-item')
    
    scraped_laptops = []
    
    for product in product_containers:
        title_tag = product.find('h2')
        title = title_tag.text.strip() if title_tag else "Title not found"
            
        price_box = product.find('span', {'class': 'a-price-whole'})
        price = price_box.text.strip() if price_box else "Price not found"
            
        rating_box = product.find('span', {'class': 'a-icon-alt'})
        rating = rating_box.text.strip() if rating_box else "Rating not found"
            
        if title != "Title not found" and len(title) > 5:
            scraped_laptops.append({
                "Laptop Name": title,
                "Price (INR)": price,
                "Rating": rating
            })
            
    print(f"Found {len(scraped_laptops)} laptops in the file.")
    
    if len(scraped_laptops) > 0:
        print("Saving data to a CSV file...")
        df = pd.DataFrame(scraped_laptops)
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"amazon_laptops_{current_time}.csv"
        df.to_csv(filename, index=False)
        print(f"All done! Your file is saved as: {filename}")
    else:
        print("Still 0 laptops. Amazon's HTML structure on your saved page is entirely different.")

if __name__ == "__main__":
    parse_amazon_data()
