import requests
import json

client_id = '3245bb1c8db3b331738e'
client_secret = 'a347c217e362abfebe19b8b6ab0551c3'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

headers = {"X-Xapp-Token": json.loads(r.text)["token"]}

with open("data/artists_data.txt", encoding="UTF-8") as data, \
        open("data/artists_names.txt", "w", encoding="UTF-8") as names:
    artists = []
    for i in data:
        r = requests.get(f"https://api.artsy.net/api/artists/{i[:-1]}", headers=headers)
        artists.append((json.loads(r.text)["sortable_name"], json.loads(r.text)["birthday"]))
    for artist in sorted(artists, key=lambda x: (x[1], x[0])):
        names.write(artist[0] + "\n")
