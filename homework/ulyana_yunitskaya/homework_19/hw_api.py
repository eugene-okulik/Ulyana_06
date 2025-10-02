import requests


def one_post():
    post_id = new_post()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}').json()
    assert response['id'] == post_id


def new_post():
    body = {
        "data":
            {
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
    return response.json()['id']


def put_a_post():
    post_id = new_post()
    body = {
        "data":
            {
                "color": "pink",
                "size": "small"
            },
        "name": "First object_20"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['data']['color'] == 'pink'
    assert response['data']['size'] == 'small'


put_a_post()


def patch_a_post():
    post_id = new_post()
    body = {
        "data":
            {
                "color": "green",
            },
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['data']['color'] == 'green'


patch_a_post()


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code in [200, 204]
    response_get = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response_get.status_code == 404
