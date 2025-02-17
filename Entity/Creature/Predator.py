class Predator(Creature):
    def __init__(self, name, health):
        super().__init__(name, health)
    def eat(self, food):
        if isinstance(food, Herbivore):
            self.health += 20
        else:
            print("I don't eat this!")