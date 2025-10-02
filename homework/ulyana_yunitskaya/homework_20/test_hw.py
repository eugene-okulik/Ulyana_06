import requests
import pytest


@pytest.fixture(scope='session', autouse=True)
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def say_test():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def play_yield():
    body = {
        "data": {
            "color": "blue",
            "size": "biggest"
        },
        "name": "First object_20"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')


@pytest.mark.parametrize('name', ['^&*', 'P', ' '])
@pytest.mark.medium
def test_one_obj(play_yield, name):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{play_yield}').json()
    assert response['id'] == play_yield


@pytest.mark.critical
def test_put_a_obj(play_yield):
    body = {
        "data": {
            "color": "pink",
            "size": "small"
        },
        "name": "First object_20"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{play_yield}',
        json=body,
        headers=headers
    ).json()
    assert response['data']['color'] == 'pink'
    assert response['data']['size'] == 'small'


def test_patch_a_obj(play_yield):
    body = {
        "data": {
            "color": "green",
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{play_yield}',
        json=body,
        headers=headers
    ).json()
    assert response['data']['color'] == 'green'


def test_delete_a_obj(play_yield):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{play_yield}')
    assert response.status_code in [200, 204]
    response_get = requests.get(f'http://objapi.course.qa-practice.com/object/{play_yield}')
    assert response_get.status_code == 404
