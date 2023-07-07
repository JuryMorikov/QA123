import requests

def test_get_list():
    request = requests.get('https://reqres.in/api/users?page=2')
    assert request.status_code == 200
    r = request.json()
    return (r)

print(test_get_list())