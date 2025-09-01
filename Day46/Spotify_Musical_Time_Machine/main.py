import bs4, os, requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

header = {'USER-AGENT': os.environ.get('MY_BROWSER_HEADER')}
date = input('Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ')
url = os.environ.get('BILLBOARD_ENDPOINT')+date

response = requests.get(url=url, headers=header)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
song_name_spans = soup.select('li ul li h3')
song_names = [song.getText().strip() for song in song_name_spans]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope='playlist-modify-private',
    redirect_uri='https://example.com',
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    show_dialog=True,
    cache_path='token.txt',
    username=os.environ.get('USERNAME'),
))

user_id = sp.current_user()['id']
song_uris = []
year = date.split('-')[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exists in spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)