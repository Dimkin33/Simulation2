class Simulation():
    def __init__(self, width, height):
        self.map = Map(width, height)
    def add_entity(self, entity, x, y):
        self.map.add_entity(entity, x, y)
    def render_map(self):
        self.map.print_map()