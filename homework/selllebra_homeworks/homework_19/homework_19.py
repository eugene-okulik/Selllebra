import requests


def new_object():
    body = {
        "name": "August",
        "data": {"monday": 1, "tuesday": 2, "wednesday": 3}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )

    assert response.status_code == 200, 'Status code is incorrect'
    return response.json()['id']


def get_one_object(object_id):
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{object_id}'
    )
    return response


def clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def put_an_object():
    object_id = new_object()
    body = {
        "name": "August_2026",
        "data": {"monday": 3, "tuesday": 4, "wednesday": 5}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'August_2026'
    clear(object_id)


def patch_an_object():
    object_id = new_object()
    body = {
        "name": "August_2026_timetable"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'August_2026_timetable'
    clear(object_id)


def delete_an_object():
    object_id = new_object()
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{object_id}'
    )

    response = get_one_object(object_id)
    assert response.status_code == 404, 'Status code is incorrect'


new_object()
put_an_object()
patch_an_object()
delete_an_object()
