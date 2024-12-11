import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Chapters 1-708 - 1-497 is officially translated, 498 - 708 will be test data
# train_chapters = [chapter for chapter in range(1, 498)]
# test_chapters = [chapter for chapter in range(498, 709)]
chapters = [497]
base_url = "https://ncode.syosetu.com/"
index_url = base_url + "n2267be/"

# avoid webscraper detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

for chapter in chapters:
    url = index_url + str(chapter) + "/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Targeting specific part of the page, e.g., <div class="text-content">
        content_div = soup.find('div', {'class': 'js-novel-text p-novel__text'})

        # If content_div exists, extract paragraphs
        if content_div:
            paragraphs = soup.find_all("p")
            paragraphs_text = [p.get_text() for p in paragraphs]
            with open('paragraphs.json', 'w', encoding='utf-8') as json_file:
                json.dump(paragraphs_text[7:], json_file, ensure_ascii=False, indent=4)
        else:
            print(f"Failed to fetch chapter {chapter}, content_div not found")

    else:
        print(f"Failed to fetch chapter {chapter}, exited with status code {response.status_code}")
        break