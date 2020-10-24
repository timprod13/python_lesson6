class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.__income = {'wage': self.wage, 'bonus': self.bonus}

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_full_profit(self):
        return self.__income


boss = Position('Justin', 'Bieber', 'boss', 50000, 100)
print(boss.get_full_name(), boss.get_full_profit())

headhunter = Position('Boba', 'Fett', 'HH', 10000, 50000)
print(headhunter.get_full_name(), headhunter.get_full_profit())

worker = Position('Armen', 'Jigarkhanyan', 'worker', 100, 10)
print(worker.get_full_name(), worker.get_full_profit())
