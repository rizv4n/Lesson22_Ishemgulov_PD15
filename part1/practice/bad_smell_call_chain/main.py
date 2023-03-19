# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, population, room_numb):
        self.population = population
        self.room_numb = room_numb

    def get_person_room(self):
        return self.room_numb

    def get_city_population(self):
        return self.population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(220000, 23)

print(person.population)
print(person.room_numb)