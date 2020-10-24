class Road:
    weight: int
    thickness: int

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self):
        self.weight = 25
        self.thickness = 5
        return (self._length * self._width * self.weight * self.thickness) / 1000


my_road = Road(20, 5000)
print(int(my_road.asphalt_mass()))
