import pytest
import random
import string
import Parametrs

from Project import Project


def generate_string(length):
    all_symbols = string.ascii_uppercase + string.ascii_lowercase
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    return result


project_api = Project(Parametrs.URL)

headers = {
    "Authorization": f"Bearer {Parametrs.Token}",
    "Content-Type": "application/json"
}

project = {
        "title": f"{generate_string(10)}",
        "users": {f"{Parametrs.users}": "admin"}
}


@pytest.mark.parametrize('project, headers',
                         [(project, headers)])
def test_create_project(project, headers):
    project_new = project_api.create_project(project, headers)
    Parametrs.id_project_new = project_new["id"]
    assert project_new["id"] is not None


@pytest.mark.parametrize('headers', [headers])
def test_get_list_project(headers):
    list_projects = project_api.get_list_projects(headers)
    assert len(list_projects) > 0, "У данной компании отсутствуют проекты."


@pytest.mark.parametrize('headers, id ', [(headers, Parametrs.id_project_new)])
def test_get_id_project(headers, id):
    get_project = project_api.get_id_project(headers, id)
    assert get_project["id"] == id


def test_edit_id_project():
    project = {
        "title": f"{generate_string(10)}",
        "users": {f"{Parametrs.users}": "admin"}
    }
    get_project = project_api.create_project(project, headers)
    id_project = get_project["id"]

    get_project = project_api.get_id_project(headers, id_project)
    project = {
        "title": f"{get_project['title']}+_New",
        "users": {f"{Parametrs.users}": "admin"}
    }
    project_api.edit_id_project(headers, id_project, project)
    get_project = project_api.get_id_project(headers, id_project)
    assert get_project["title"] == project["title"]


@pytest.mark.parametrize('project, headers', [(None, headers),
                                              (None, ""),
                                              (project, "")])
def test_create_project_negative(project, headers):
    if (project is None) or (project == ""):
        print("В запросе создания проекта отсутствует обязательный атрибут, "
              "определяющий параметры проекта(Json)")
    elif ((headers is None) or (headers == "")):
        print("В запросе создания проекта отсутствует информация "
              "об авторизации клиента(headers)")
    else:
        project_new = project_api.create_project(project, headers)
        Parametrs.id_project_new = project_new["id"]
        assert project_new["id"] is not None


@pytest.mark.parametrize('headers',
                         [""])
def test_get_list_project_negarive(headers):
    if (headers is None) or (headers == ''):
        print("В запросе получения списка проектов отсутствует информация"
              "об авторизации клиента(headers)")
    else:
        list_projects = project_api.get_list_projects(headers)
        assert len(list_projects) > 0, \
            "У данной компании отсутствуют проекты."


@pytest.mark.parametrize('headers, id', [(headers, Parametrs.id_project_new)])
def test_get_id_project_negative(headers, id):
    if (headers is None) or (headers == ''):
        print("В запросе получения списка проектов отсутствует информация"
              "об авторизации клиента(headers)")
    elif (id is None) or (id == ''):
        print("В запросе получения списка проектов отсутствует информация"
              "об  идентификаторе проекта(id)")
    else:
        get_project = project_api.get_id_project(headers, id)
    assert get_project["id"] == id
