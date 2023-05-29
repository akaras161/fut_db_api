import requests
import json


def print_data(data):
    with open('clubs.csv', 'a', encoding='utf-8') as f:
        for i in range(len(data['items'])):
            if data['items'][i]['league'] == 13 or data['items'][i]['league'] == 31 or data['items'][i]['league'] == 19:
                club_id = data['items'][i]['id']
                club_name = data['items'][i]['name']
                club_league = data['items'][i]['league']
                print(club_id)
                print(club_name)
                print(club_league)
                f.write(str(club_id))
                f.write(',')
                f.write(club_name)
                f.write(',')
                f.write(str(club_league))
                f.write('\n')


def get_response(page_num, api_key):
    url = f'https://futdb.app/api/clubs?page={page_num}'
    return requests.get(url, headers=api_key)


def save_data(data_to_save):
    with open('clubs.csv', 'a', encoding='utf-8') as f:
        for i in range(len(data_to_save['items'])):
            print(data_to_save['items'][i])


if __name__ == '__main__':
    with open('clubs.csv', 'a', encoding='utf-8') as file:
        file.write('club_id,club_name,club_league\n')

    headers = {
        'accept': 'application/json',
        'X-AUTH-TOKEN': '7894bd21-64d7-4a97-95f5-4e41d4d7002f'
    }

    data = None
    for i in range(1, 36):
        response = get_response(i, headers)
        if response.status_code == 200:
            print("Dane zostały pobrane poprawnie!")
            print("==========================================================")
            data = json.loads(response.text)
            print_data(data)
        else:
            print('Błąd podczas wykonania żądania:', response.status_code)

