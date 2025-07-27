import requests

base_url = "https://ru.yougile.com"
key = 'E6sX+kQ12uAs+TRRLGNkvZnCFRck7XP-1F60G8O00VukpMUTnDLX84E4YBBA1eCP'
id = '3352c644-97d1-4bc6-8dea-1557d08230f6'


# Позитив_получение списка проектов
def test_positive_get_list_project():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    resp = requests.get(base_url + '/api-v2/projects', headers=headers)
    assert resp.status_code == 200


# Негатив_получение списка проектов с пустым значением ключа
def test_negative_get_list_project():
    headers = {
        'Authorization': '',
        'Content-Type': 'application/json'
    }
    resp = requests.get(base_url + '/api-v2/projects', headers=headers)
    assert resp.status_code == 401


# Позитив_изменение наименования проекта
def test_positive_change_name():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }

    body = {
        "title": "New name project"
    }
    resp = requests.put(f'{base_url}/api-v2/projects/{id}', headers=headers, json=body)
    assert resp.status_code == 200


# Негатив_пустое значение наименования проекта
def test_negative_change_name():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }

    body = {
        "title": ""
    }
    resp = requests.put(f'{base_url}/api-v2/projects/{id}', headers=headers, json=body)
    assert resp.status_code == 400


# Негатив_изменение наименования проекта с неправильным токеном
def test_negative_incorrect_token():
    headers = {
        'Authorization': f'Bearer H6HngIA816fpIhY7tBvWx/it3YbVvEt/33Sk8afA39MCR9a',
        'Content-Type': 'application/json'
    }

    body = {
        "title": "New name project"
    }
    resp = requests.put(f'{base_url}/api-v2/projects/{id}', headers=headers, json=body)
    assert resp.status_code == 401


# Позитив_получение проекта по ID
def test_positive_get_project_ID():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    resp = requests.get(f'{base_url}/api-v2/projects/{id}', headers=headers)
    assert resp.status_code == 200


# Негатив_получение проекта по некорректному ID
def test_negative_get_project():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    resp = requests.get(f'{base_url}/api-v2/projects/1234c567-89d1-0bc6-8dea-1112d13140f6', headers=headers)
    assert resp.status_code == 404


# Позитив_создание нового проекта
def test_positive_create_project():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    body = {
        "title": "My new project"
    }
    resp = requests.post(f'{base_url}/api-v2/projects', headers=headers, json=body)
    assert resp.status_code == 201


# Негатив_создание нового проекта с пустым значением наименования
def test_negative_no_name_project():
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    body = {
        "title": None
    }
    resp = requests.post(f'{base_url}/api-v2/projects', headers=headers, json=body)
    assert resp.status_code == 400