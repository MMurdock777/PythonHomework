class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Metal):
            return Mercury()
        else:
            return Empty()


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Metal):
            return Rust()
        else:
            return Empty()


class Earth:
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Metal):
            return Mineral()
        else:
            return Empty()


class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Metal):
            return Explosion()
        else:
            return Empty()


class Metal:
    def __add__(self, other):
        if isinstance(other, Air):
            return Explosion()
        elif isinstance(other, Fire):
            return Explosion()
        elif isinstance(other, Earth):
            return Mineral()
        elif isinstance(other, Water):
            return Rust()
        else:
            return Empty()


class Empty:
    answer = None


class Storm:
    answer = "Cложили два элемента и вывели Шторм"


class Steam:
    answer = "Cложили два элемента и вывели Пар"


class Dirt:
    nswer = "Cложили два элемента и вывели Грязь"


class Lightning:
    answer = "Cложили два элемента и вывели Молнию"


class Dust:
    answer = "Cложили два элемента и вывели Пыль"


class Lava:
    answer = "Cложили два элемента и вывели Лаву"


class Explosion:
    answer = "Cложили два элемента и вывели Взрыв"


class Rust:
    answer = "Cложили два элемента и вывели Ржавчину"


class Mineral:
    answer = "Cложили два элемента и вывели Минерал"


class Mercury:
    answer = "Cложили два элемента и вывели Ртуть"


a = Fire()
b = Metal()
c = a + b
print(c.answer)
c = b + b
print(c.answer)
