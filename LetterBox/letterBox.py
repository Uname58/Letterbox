import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def show_menu():
    print("=" * 30)
    print("        LetterBox")
    print("=" * 30)
    print("1. Latest AI news")
    print("-" * 30)

def main():
    choice = input("Select an option (1-9): ")
    print("-"*70)
    if choice == "1":
        Latest_AI()

def Latest_AI():
    url = "https://www.worldjournal.com/search/word/8877/ai"
    base = "https://www.worldjournal.com"
    headers = {"User-Agent": "Mozilla/5.0", "Referer": base + "/"}

    html = requests.get(url, headers=headers, timeout=15).text
    soup = BeautifulSoup(html, "html.parser")

    results, seen = [], set()
    for tag in soup.find_all(attrs={"href": re.compile(r"/wj/story/")}):
        href = tag.get("href", "").strip()
        article_url = urljoin(base, href)
        title = (tag.get("title") or tag.get_text(" ", strip=True)).strip()
        if title and article_url and article_url not in seen:
            seen.add(article_url)
            results.append((title, article_url))

    for i, (title, article_url) in enumerate(results[2:12], 1):
        print(f"{i}. {title}\n   {article_url}")
    


if __name__ == "__main__":
    
    while True:
        print("-"*70)
        show_menu()
        main()