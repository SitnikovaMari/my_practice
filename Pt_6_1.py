import requests
from bs4 import BeautifulSoup


def get_top_songs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Ошибка при запросе к серверу")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        songs = soup.find_all('div', class_='d-track__name')[:10]
    except AttributeError:
        print("Ошибка при поиске песен")
        return

    top_songs = []
    for song in songs:
        try:
            song_title = song.get_text(strip=True)
            top_songs.append(song_title)
        except AttributeError:
            print("Ошибка при извлечении названия песни")

    return top_songs


artist_url = input("Вставьте ссылку на исполнителя в сервисе Yandex Music: ")
top_songs = get_top_songs(artist_url)
if top_songs:
    print("Топ 10 песен:")
    count = 1
    for song in top_songs:
        print(f"{count:2}. {song}")
        count += 1
