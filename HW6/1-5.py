from typing import List
from faker import Faker
from random import randint

class Man:

    def __init__(
            self,
            name: str,
            second_name: str,
            age: int,
            grades: List[int],
    ):
        self.set_name(name)
        self.set_sec_name(second_name)
        self.set_age(age)
        self.set_grades(grades)

    def str(self) -> str:
        return f'С именем {self.__name} и фамилией {self.__second_name} и ' \
               f'возрастом {self.__age}'

    def set_name(self, name: str):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Имя может быть только строкой")
            self.__name = ''

    def set_sec_name(self, second_name: str):
        self.__second_name = second_name

    def set_age(self, age: int):
        self.__age = age

    def set_grades(self, grades: List[int]):
        if isinstance(grades, list):
            self.__grades = grades
        else:
            print("Оценки могут быть только списком")
            self.__grades = []

    def get_name(self):
        return self.__name

    def get_second_name(self):
        return self.__second_name

    def get_age(self):
        return self.__age

    def get_grades(self):
        return self.__grades

    def get_average_grade(self):
        return sum(self.__grades)/len(self.__grades)

    def greet(self) -> str:
        return f'Привет! Меня зовут {self.__second_name} {self.__name}, ' \
               f'мне {self.__age} лет. Мои оценки {self.__grades}'


list_students = []
fake = Faker()

for i in range(10):
    f_name = fake.name().split()
    list_students.append(Man(f_name[0], f_name[1], i, list(range(randint(1, 5), 10))))
for i in list_students:
    print(i.greet())
list_students.sort(key= lambda x: x.get_average_grade(), reverse=True)
for i in list_students:
    print(f"Имя {i.get_second_name()} {i.get_name()}. Возраст: {i.get_age()} Оценки: {i.get_grades()} Средний балл: "
          f"{i.get_average_grade()}")
