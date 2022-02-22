
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Client(User):
    def __init__(self, name, surname, balance = 0):
        self.balance = balance

        User.__init__(self, name, surname)

    def check_balance(self):
        print('Клиент "' + self.name, self.surname + '". Баланс: ' + str(self.balance) + ' руб.\n')



if __name__ == '__main__':
    user1 = Client('Иван', 'Петров', 50)
    user2 = Client('Семён', 'Ветров', 130)
    users = [user1, user2]
    print('----------------------------------------')
    for user in users:
        Client.check_balance(user)

