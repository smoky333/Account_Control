#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет
# сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID),
# имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
#Требования:
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).
#2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._access_level = "user"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__access_level = "admin"

    def add_user(self, user):
        user_list.append(user)
        print(f"User {user.get_name()} added to the list")

    def remove_user(self, user):
        user_list.remove(user)
        print(f"User {user.get_name()} removed from the list")


user_list = []
admin = Admin(1, "Admin")

user1 = User(2, "John")
user2 = User(3, "Natalie")

admin.add_user(user1)
admin.add_user(user2)
admin.remove_user(user1)









