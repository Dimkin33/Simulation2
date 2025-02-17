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