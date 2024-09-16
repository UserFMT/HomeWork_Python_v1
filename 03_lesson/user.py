class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_First_Name(self):
        return self.first_name

    def get_Last_Name(self):
        return self.last_name

    def get_All_Name(self):
        return f"First_name - {self.first_name} , Last_name - {self.last_name}"
