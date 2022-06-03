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
        return f'<Username: {self.username}, ID: {self.id}, Password: {self.password}, Name: {self.name}, Email: {self.email}, Phone-Number: {self.phone}, City: {self.city}>'
