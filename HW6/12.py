from random import randint


class Grass:

    def __init__(
            self,
    ):
        self.nutrition = randint(2, 7)


class GrassEater:

    def __init__(
            self,
    ):
        self.hunger_level = randint(5, 10)

    def eat_grass(self, grass: Grass()):
        if self.hunger_level <= 0:
            print("Зверь не голоден")
        else:
            self.hunger_level -= grass.nutrition

    def state_hunger_level(self):
        print(f"Уровень голода: {self.hunger_level}")


giraffe = GrassEater()
good_grass = Grass()
giraffe.state_hunger_level()
giraffe.eat_grass(good_grass)
giraffe.state_hunger_level()
