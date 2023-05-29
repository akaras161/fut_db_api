import requests
import json


def print_data(data):
    with open('players.csv', 'a', encoding='utf-8') as f:
        for i in range(len(data['items'])):
            player_name = data["items"][i]["name"]
            player_height = data["items"][i]["height"]
            player_weight = data["items"][i]["weight"]
            player_position = data["items"][i]["position"]
            player_league = data["items"][i]["league"]
            player_club = data["items"][i].get("club", None)  # Może być wartość None, jeśli pole "club" nie istnieje
            player_age = data['items'][i]['age']
            player_speed = data['items'][i]['pace']
            player_jumping = data['items'][i]['physicalityAttributes']['jumping']

            print("Imię:", player_name)
            print("Wzrost:", player_height)
            print("Waga:", player_weight)
            print("Wiek:", player_age)
            print("Pozycja:", player_position)
            print("Szybkość:", player_speed)
            print("Skok:", player_jumping)
            print("Liga:", player_league)
            print("Klub:", player_club)
            print("==========================================================")
            if player_league == 13 or player_league == 19 or player_league == 31:
                f.write(player_name)
                f.write(',')
                f.write(str(player_height))
                f.write(',')
                f.write(str(player_weight))
                f.write(',')
                f.write(str(player_age))
                f.write(',')
                f.write(player_position)
                f.write(',')
                f.write(str(player_speed))
                f.write(',')
                f.write(str(player_jumping))
                f.write(',')
                f.write(str(player_league))
                f.write(',')
                f.write(str(player_club))
                f.write('\n')


def get_response(page_num, api_key):
    url = f'https://futdb.app/api/players?page={page_num}'
    return requests.get(url, headers=api_key)


if __name__ == '__main__':
    with open('players.csv', 'a', encoding='utf-8') as file:
        file.write('name,height,weight,age,position,tempo,skok,league,club\n')

    headers = {
        'accept': 'application/json',
        'X-AUTH-TOKEN': '7894bd21-64d7-4a97-95f5-4e41d4d7002f'
    }

    #  all = 932

    data = None
    for i in range(1, 932):
        response = get_response(i, headers)
        if response.status_code == 200:
            print("Dane zostały pobrane poprawnie!")
            print("==========================================================")
            data = json.loads(response.text)
            print_data(data)
        else:
            print('Błąd podczas wykonania żądania:', response.status_code)

