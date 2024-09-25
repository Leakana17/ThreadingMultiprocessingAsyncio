import threading
import time
import requests
from bs4 import BeautifulSoup

def simulate_io_task(url):
    response = requests.get(url)

    # Parse the HTML to find the title
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip() if soup.title else 'default_title'

    # Save the HTML file using the title
    filename = f"{title}.html"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

def run_io_tasks():
    url_list = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Photovoltaics",
    "https://en.wikipedia.org/wiki/Time_management",
    "https://en.wikipedia.org/wiki/Healthy_diet",
    "https://en.wikipedia.org/wiki/History_of_video_games",
    "https://en.wikipedia.org/wiki/Space_exploration",
    "https://en.wikipedia.org/wiki/Color_theory",
    "https://en.wikipedia.org/wiki/Sustainable_energy",
    "https://en.wikipedia.org/wiki/Cognitive_dissonance",

]

    
    threads = []
    for url in url_list:
        thread = threading.Thread(target=simulate_io_task, args=(url,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
