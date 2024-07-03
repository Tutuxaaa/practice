import requests

def parse_vacancies():
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "python",  # Пример поискового запроса
        "area": 1,  # Пример кода региона (Москва)
        "per_page": 10  # Количество вакансий на одной странице
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            vacancy_id = item['id']
            vacancy_title = item['name']
            print(f"ID: {vacancy_id}, Title: {vacancy_title}")
    else:
        print("Ошибка при выполнении запроса")

parse_vacancies()
