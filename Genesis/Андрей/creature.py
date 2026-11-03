class Creature:
    def __init__(self, x: int, y: int, genes: dict):
        self.x = x
        self.y = y
        self.genes = genes
        self.energy = 100.0
        self.age = 0
        self._alive = True

    @property
    def is_alive(self) -> bool:
        return self._alive

    def __repr__(self):
        return(
            f"Creature(pos=({self.x},{self.y})),"
            f"energy={self.energy:.1f}, age{self.age})"
        )
    
    def tick(self) -> None:
        self.age += 1
        size = self.genes.get("size",1.0)
        self.energy -= size
        if self.energy < 0:
            self._alive = False

    def food(self,food_value:float) -> None:
        gain = food_value * 30
        self.energy = min(200.0, self.energy+gain)
        