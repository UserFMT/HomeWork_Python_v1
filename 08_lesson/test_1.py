import pytest
import random
import string
import Parametrs

from Project import Project

project_api = Project(Parametrs.URL)


def generate_string(length):
    all_symbols = string.ascii_uppercase + string.ascii_lowercase
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    return result


headers = {
        "Authorization": f"Bearer {Parametrs.Token}",
        "Content-Type": "application/json"
    }
project = {
        "title": f"{generate_string(10)}",
        "users": {f"{Parametrs.users}": "admin"}
    }



@pytest.fixture(scope = "session", autouse = True)
def project_new():
    project_n= {
        "title": f"{generate_string(10)}",
        "users": {f"{Parametrs.users}": "admin"}
    }
    project_new = project_api.create_project(project_n, headers)
    return project_new.json()["id"]



@pytest.mark.parametrize('project, headers',
                         [(project, headers)])
def test_create_project(project, headers):
    project_new = project_api.create_project(project, headers)
    assert project_new.status_code == 201
    assert project_new.json()["id"] is not None
    project = {
        "deleted": True
    }
    del_project = project_api.edit_id_project(headers, project_new.json()["id"], project)
    assert del_project["id"] is not None


@pytest.mark.parametrize('headers', [headers])
def test_get_list_project(headers):
    list_projects = project_api.get_list_projects(headers)
    assert list_projects.status_code == 200
    count_after = list_projects.json()["paging"]["count"]
    project_add = {
        "title": "Autotest_add_list",
        "users": {f"{Parametrs.users}": "admin"}
    }
    add_project = project_api.create_project(project_add,headers)
    assert  add_project.json()["id"] is not None

    list_projects = project_api.get_list_projects(headers)
    count_before = list_projects.json()["paging"]["count"]
    assert count_after < count_before , "Кол-во проектов не изменилось после добавления."
    project_add = {
        "deleted": True
    }
    del_project = project_api.edit_id_project(headers, add_project.json()["id"], project_add)
    assert del_project["id"] is not None


def test_get_id_project(project_new):
    get_project = project_api.get_id_project(headers, project_new)
    assert get_project.status_code == 200
    assert get_project.json()["id"]  is not None
    project_del = {
        "deleted": True
        }
    del_project = project_api.edit_id_project(headers, get_project.json()["id"], project_del)
    assert del_project["id"]  is not None


def test_edit_id_project():
    project = {
        "title": f"{generate_string(10)}",
        "users": {f"{Parametrs.users}": "admin"}
    }
    get_project = project_api.create_project(project, headers)
    assert get_project.status_code == 201
    assert get_project.json()["id"] is not None

    get_project = project_api.get_id_project(headers, get_project.json()["id"])
    assert get_project.status_code == 200
    assert get_project.json()["id"] is not None

    project = {
        "title": f"{get_project.json()['title']}+_New"
    }
    project_n = project_api.edit_id_project(headers, get_project.json()["id"], project)
    assert project_n["id"] is not None

    project_n = project_api.get_id_project(headers, project_n["id"])
    assert get_project.json()["title"] != project_n.json()["title"], \
        "Название проекта не изменилось"
    project = {
        "deleted": True
        }
    del_project = project_api.edit_id_project(headers, project_n.json()["id"], project)
    assert del_project["id"] is not None


@pytest.mark.parametrize('project, headers', [(None, headers),
                                              (None, ""),
                                              (project, "")])
def test_create_project_negative(project, headers):
    if (project is None) or (project == ""):
        print("В запросе создания проекта отсутствует обязательный атрибут,"
              " определяющий параметры проекта(Json)")
    elif ((headers is None) or (headers == "")):
        print("В запросе создания проекта отсутствует информация"
              " об авторизации клиента(headers)")
    else:
        project_new = project_api.create_project(project, headers)
        assert project_new.status_code == 201
        assert project_new.json()["id"] is not None


@pytest.mark.parametrize('headers',
                         [""])
def test_get_list_project_negarive(headers):
    if (headers is None) or (headers == ''):
        print("В запросе получения списка проектов отсутствует информация"
              " об авторизации клиента(headers)")
    else:
        list_projects = project_api.get_list_projects(headers)
        assert  list_projects.status_code == 200
        assert  list_projects.json()["paging"]["count"] != 0,\
            "У данной компании отсутствуют проекты."


@pytest.mark.parametrize('headers, project',
                         [(headers, None),
                          (None, project)
                          ])
def test_get_id_project_negative(headers, project):
    if (headers is None) or (headers == ''):
        print("В запросе получения списка проектов отсутствует информация"
              " об авторизации клиента(headers)")
    elif (project is None) or (project == ''):
        print("В запросе получения списка проектов отсутствует информация"
              " об  идентификаторе проекта(id)")
    else:
        create_project =  project_api.create_project(project, headers)
        get_project = project_api.get_id_project(headers, create_project.json()["id"])
        assert get_project.json()["id"] is not None
