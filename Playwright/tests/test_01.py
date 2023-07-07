import requests
from config import *

def test_get_users():
    r = requests.get(url_create_user)
    assert r.status_code == 200, 'Error: wrong status code'
    req = r.json()
    assert(req['data'][0]['last_name']) == 'Lawson'


def test_get_user():
    r = requests.get(url_create_user)
    assert r.status_code == 200
    req = r.json()
    assert(req['data']['first_name']) == 'Janet'

def single_user_not_found():
    r = requests.get(url_single_user_not_found)
    assert r.status_code == 404
    req = r.json()
    assert(req()) == {}

def list_resource():
    r = requests.get(url_list_resource)
    assert r.status_code == 200
    req = r.json()
    assert(req['data'][2]['name']) == 'true red'

def single_resource_not_found():
    r = requests.get(url_single_resource_not_found)
    assert r.status_code == 404
    req = r.json()
    assert(req()) == {}


    