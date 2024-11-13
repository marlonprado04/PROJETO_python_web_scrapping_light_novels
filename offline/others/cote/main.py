from Scrapper import Scrapper
from bs4 import BeautifulSoup

def main():
    # Instancia classe
    scrapper = Scrapper()

    html_content = scrapper.list_elements_by_css_selector("post-text-content")

    soup = BeautifulSoup(html_content, "html.parser")

    for title in soup.find_all("h2"):
        print(title)

    scrapper.close_driver()

if __name__ == "__main__":
    main()
