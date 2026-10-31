class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.food = {}

        self.creatures = []

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def add_food(self, x: int, y: int, value: float = 1.0) -> None:
        if not self.in_bounds(x, y):
            return
        self.food[(x, y)] = self.food.get((x, y), 0.0) + value

    def add_creature(self, creature) -> None:

        if self.in_bounds(creature.x, creature.y):
            self.creatures.append(creature)

    @property
    def alive_creatures(self):
        return [c for c in self.creatures if c.is_alive]

    