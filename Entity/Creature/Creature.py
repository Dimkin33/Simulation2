class Creature(Entity):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.velocity = 1
    def make_move(self, direction):
        ...
    def eat(self, food):
        ...