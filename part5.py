class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Starting rendering {self.title}'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Starting drawing with a pen'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Starting drawing with a pencil'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Starting drawing with a handle'


pen = Pen('a pen')
pencil = Pencil('a pencil')
handle = Handle('a handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
