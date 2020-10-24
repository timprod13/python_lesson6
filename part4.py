class Cars:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"{self.name} went."

    def stop(self):
        return f"{self.name} has stopped."

    def turn(self, direction):
        return f"{self.name} has turned " + direction + "."

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}.'

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


class TownCar(Cars):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car!!!'
        else:
            return f'Speed of {self.name} is normal for town car.'


class SportCar(Cars):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color, is_police)


class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car!!!'
        else:
            return f'Speed of {self.name} is normal for work car.'


class PoliceCar(Cars):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


towncar = TownCar('Toyota Carina', 60, 'black')
print(f"Now we follow to {towncar.color} {towncar.name}")
print(towncar.go(), towncar.show_speed(), towncar.turn('backwards'), towncar.stop())
sportcar = SportCar('Porsche Panamera', 180, 'red')
print(f"Now we follow to {sportcar.color} {sportcar.name}")
print(sportcar.go(),
      sportcar.show_speed(),
      sportcar.turn("right to Market"),
      sportcar.stop(),
      sportcar.go(),
      sportcar.turn('left to Garage'),
      sportcar.stop())
workcar = WorkCar('Gazelle', 30, 'white')
print(f"Now we follow to {workcar.color} {workcar.name}")
print(workcar.police())
print(workcar.go(), workcar.show_speed(), workcar.stop())
policecar = PoliceCar('BMW m5', 180, 'red')
print(policecar.police())
print(policecar.show_speed())
