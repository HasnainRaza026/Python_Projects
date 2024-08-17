import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

try:
    with requests.get(url) as resp:
        resp.raise_for_status()  # Check for HTTP request errors
        soup = BeautifulSoup(resp.content, "html.parser")

        # Select movie titles directly in the correct order
        name_tag = [title.getText() for title in soup.select("h3.title")]

        with open("top_100_movies.txt", "w", encoding="UFT-8") as f:
            f.writelines(f"{name}\n" for name in name_tag)

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
