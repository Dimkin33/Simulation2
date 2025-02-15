class Entity():
    ...

class Grass(Entity):
    ...

class Rock(Entity):
    pass

class Tree(Entity):
    pass

class Creature(Entity):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.velocity = 1
    def make_move(self, direction):
        ...
    def eat(self, food):
        ...
class Herbivore(Creature):
    def __init__(self, name, health):
        super().__init__(name, health)
    def eat(self, food):
        if isinstance(food, Grass):
            self.health += 10
        else:
            print("I don't eat this!")

class Predator(Creature):
    def __init__(self, name, health):
        super().__init__(name, health)
    def eat(self, food):
        if isinstance(food, Herbivore):
            self.health += 20
        else:
            print("I don't eat this!")
class Map():
    world = {}
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def add_entity(self, entity, x, y):
        self.world[(x, y)] = entity
    def remove_entity(self, x, y):
        del self.world[(x, y)]
    def get_entity(self, x, y):
        return self.world.get((x, y))
    def move_entity(self, x, y, new_x, new_y):
        entity = self.get_entity(x, y)
        if entity:
            self.remove_entity(x, y)
            self.add_entity(entity, new_x, new_y)
        else:
            print("No entity at this position!")
    def print_map(self):
        for y in range(self.height):
            for x in range(self.width):
                entity = self.get_entity(x, y)
                if entity:
                    print(entity, end="")
                else:
                    print(".", end="")
            print()

class Simulation():
    def __init__(self, width, height):
        self.map = Map(width, height)
    def add_entity(self, entity, x, y):
        self.map.add_entity(entity, x, y)
    def render_map(self):
        self.map.print_map()
        
class Action():
    def __init__(self, entity, action):
        self.entity = entity
        self.action = action
    def execute(self):
        self.action(self.entity)
    def init_action(self):
        print("Initializing action...")
    def turn_action(self):
        print("Turning action...")
