import os
import requests
from bs4 import BeautifulSoup

PAGES = {
    "seamoth": "https://wiki.subnautica.com/sn/Seamoth",
    "reaper_leviathan": "https://wiki.subnautica.com/sn/Reaper_Leviathan",
    "magnetite": "https://wiki.subnautica.com/sn/Magnetite"
}

os.makedirs("data", exist_ok=True)

# Loop through each page from the list
for name, url in PAGES.items():
    print(f"Scraping {name}...")

    # Fetch the raw webpage
    response = requests.get(url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Isolate the main content box
    content = soup.find("div", {"class": "mw-parser-output"})

    if content:
        # Extract the text and save it
        text = content.get_text(separator="\n", strip=True)

        with open(f"data/{name}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(f" --> Saved data/{name}.txt")
    else:
        print(f" --> No content found for {name}.")

print("\nScraping complete!")