class User:
    def __init__(self, id, username, password, name, email, phone, city):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city

    def __repr__(self):
        return f'<User: {self.username}>'
