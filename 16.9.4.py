
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Guest(User):
    def __init__(self, name, surname, town, status):
        self.town = town
        self.status = status

        User.__init__(self, name, surname)

    # def check_guest_name(self):
    #     print('Клиент - ' + self.name, self.surname)



if __name__ == '__main__':
    guest1 = Guest('Иван', 'Петров', 'Москва', 'Наставник')
    guest2 = Guest('Семён', 'Ветров', 'Рязань', 'Волонтёр')
    guest3 = Guest('Валентин', 'Земеля', 'Казань', 'Стажёр')
    guests = [guest1, guest2, guest3]

    print('---------------Список гостей----------------\n')
    for visitor in guests:
         print(visitor.name, visitor.surname + ', г.' + visitor.town + ', статус "' + visitor.status + '"\n')