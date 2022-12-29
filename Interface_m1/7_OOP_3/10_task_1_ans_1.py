class Animal:
    def __init__(self, name, breed='Без породы') -> None:
        self.name = name
        self.breed = breed

    @property
    def __say_breed(self):
        print(self.breed)


cat = Animal('Барсик', 'Сибирский')
cat.__say_breed
dog = Animal('Тузик')
dog.__say_breed
