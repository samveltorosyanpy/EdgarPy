import os, json


class UserClass:
    def __init__(self):
        self.path = os.getcwd() + "/db/users.json"
        with open(self.path, 'r') as file:
            text = file.read()
            self.data = json.loads(text)

    def get_user_logins(self):
        logins = []
        for user in self.data['users']:
            logins.append(user['login'])
        return logins

    def update(self):
        new_data = json.dumps(self.data)

        with open(self.path, 'w') as fail:
            fail.write(new_data)

    def get_user_by_id(self, user_id):
        for user in self.data['users']:
            if user['id'] == user_id:
                return user
        return False

    def get_user_by_login(self, user_login):
        for user in self.data['users']:
            if user['login'] == user_login:
                return user
        return False

    def get_user_password_by_login(self, login):
        for user in self.data['users']:
            if user['login'] == login:
                return user['password']

    def create_now_user(self, login, password, phone, user_date):
        new_id = self.data["users"][-1]['id'] + 1
        self.data['users'].append(
            {"id": new_id, "login": login, "password": password, "phone": phone, "date": user_date})
        self.update()

    def update_user_data(self, user_id, **kwargs):
        user = self.get_user_by_id(user_id=user_id)
        for kw in kwargs:
            if kw in list(user.keys()):
                user[kw] = kwargs[kw]
        self.update()

# user = UserClass()
# print(user.get_user_password_by_login("AAAAAA"))
# print(user.get_user_logins())
# user.update_user_data(user_id=2, password='Torosyan')
# user.create_now_user(login="Samvel001", password="Admin001", phone="99999999", user_date="2000-08-26")
# print(user.get_user_by_id(user_id=2))