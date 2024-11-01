import requests


class Project:

    def __init__(self, url):
        self.url = url

    def create_project(self, project, headers):
        resp = requests.post(
            self.url, json=project, headers=headers)
        return resp

    def get_list_projects(self, headers):
        resp = requests.get(self.url, headers=headers)
        return resp

    def get_id_project(self, headers, id):
        resp = requests.get(
            self.url + "/" + id, headers=headers)
        return resp

    def edit_id_project(self, headers, id, json):
        resp = requests.put(
            self.url + "/" + id, headers=headers, json=json)
        return resp.json()
