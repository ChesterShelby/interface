class Person:

    def __init__(self, name,  last_name, age, num_class, level):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.num_class = num_class
        self.level = level

    def do_homework(self):
        print('Делаю уроки')

    def answer_in_class(self):
        print('Отвечаю на уроке')


person1 = Person('Иван', 'Иванов', 15, '7A', 'Excellent student')
person1.do_homework()
print(person1.name)
person2 = Person('Vadim', 'Nazarov', 20, '13A', 'Excellent student')
print(person2.name)