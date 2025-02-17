class Herbivore(Creature):
    def __init__(self, name, health):
        super().__init__(name, health)
    def eat(self, food):
        if isinstance(food, Grass):
            self.health += 10
        else:
            print("I don't eat this!")