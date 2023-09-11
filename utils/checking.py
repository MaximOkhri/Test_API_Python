import json

"""Методы для проверки ответов запросов"""
class Checking():

    """Проверка статус-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f"Успешно! Статус код: {result.status_code}")


    """Метод для проверки обязательных полей в теле запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")


    """Метод для проверки значения обязательных полей в теле запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert expected_value == check_info
        print(f'{field_name} верен.')


    """Метод для проверки значения обязательных полей в теле запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Слово {search_word} присутствует.')
        else:
            print(f'Слово {search_word} отсутствует.')