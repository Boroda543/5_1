class Hause:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не сущуствует")

h1 = Hause('ЖК Горский', 18)
h2 = Hause('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
