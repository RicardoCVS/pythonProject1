import requests
import json
import base64

#Instalamos Requests 'pip install requests'
BASE_URL = 'https://petstore.swagger.io/v2'
USERNAME = 'your-username'
PASSWORD = 'your-password'

def main():
    # create user
    user_data = {'id': 0, 'username': USERNAME, 'firstName': 'John', 'lastName': 'Doe', 'email': 'johndoe@example.com', 'password': PASSWORD, 'phone': '1234567890', 'userStatus': 0}
    create_user_response = send_post_request(f'{BASE_URL}/user', user_data)
    print(f'Create User Response: {create_user_response}')

    # retrieve user data
    user_data_response = send_get_request(f'{BASE_URL}/user/{USERNAME}')
    print(f'User Data Response: {user_data_response}')

    # get pets by status
    pets_json = send_get_request(f'{BASE_URL}/pet/findByStatus?status=sold')
    pets_list = json.loads(pets_json)

    # list pet names and ids
    pet_names_list = [{'id': pet['id'], 'name': pet.get('name', '')} for pet in pets_list]
    print(f'Pet Names and IDs List: {pet_names_list}')

    # count pet names
    pet_names_count = {}
    for pet in pet_names_list:
        name = pet['name']
        if name in pet_names_count:
            pet_names_count[name] += 1
        else:
            pet_names_count[name] = 1
    print(f'Pet Names Count: {pet_names_count}')

def send_get_request(url):
    headers = {'Content-Type': 'application/json', 'Authorization': get_authorization_header()}
    response = requests.get(url, headers=headers)
    return response.text

def send_post_request(url, data):
    headers = {'Content-Type': 'application/json', 'Authorization': get_authorization_header()}
    response = requests.post(url, json=data, headers=headers)
    return response.text

def get_authorization_header():
    return 'Basic ' + base64.b64encode((USERNAME + ':' + PASSWORD).encode('ascii')).decode('ascii')


if __name__ == '__main__':
    main()
