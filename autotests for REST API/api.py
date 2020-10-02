import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder



class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/'

    def get_api_key(self, email, password):

        headers = {
             'email': email,
             'password': password
         }
        res = requests.get(self.base_url + 'api/key', headers = headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params = filter)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    #Методы POST, DELETE, PUT

    def add_information_about_new_pet_without_photo(self, auth_key, name, animal_type, age, pet_photo):
        """Запрос на добавление нового питомца без фото, основные параметры имя питомца, вид и возвраст"""
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age, 'pet_photo': pet_photo}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_pet_only_with_photo(self, auth_key, name, animal_type, age, pet_photo):
        """Метод отправляем запрос на добавления только фотографии для нового питомца с пустыми данными имени, вида
        и возраста"""

        data = MultipartEncoder({'name': name, 'animal_type': animal_type, 'age': age,
                                 'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')})
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def add_new_pet(self, auth_key, name, animal_type, age, pet_photo):
        """Запрос на добавление нового питомца с фото и валидными данными, для данного теста установили
        requests_toolbelt библиотеку"""

        data = MultipartEncoder({'name': name, 'animal_type': animal_type, 'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')})
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_photo_of_pet(self, auth_key, pet_id, pet_photo):
        """Метод отправляем запрос на добавления фотографии к питомцу по id"""

        data = MultipartEncoder({'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')})
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo' + pet_id, headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet_from_database(self, auth_key, pet_id):
        """Метод отправляет запрос на удаление питомца по ID и возвращает
        статус запроса и результат с текстом уведомления об успешном удалении питомца."""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_information(self, auth_key, pet_id, name, animal_type, age):
        #Метод отправляет запрос на сервер о обновлении данных питомца по указанному ID

        headers = {'auth_key': auth_key['key']}
        data = {'name': name,'age': age, 'animal_type': animal_type}

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result