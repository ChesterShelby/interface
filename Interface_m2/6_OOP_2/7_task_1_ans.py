class Person:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

    def say_name(self):
        print(f'Привет меня зовут {self.lname} {self.name}')

    def say_age(self):
        print(f'Мой возраст {self.age}')


class Student(Person):
    def __init__(self, name, lname, age, class_num):
        super().__init__(name, lname, age)
        self.class_num = class_num

    def say_class_num(self):
        print(f'Я учюсь в {self.class_num} классе')


student1 = Student('Иван', 'Петров', 14, 9)
student1.say_class_num()
