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