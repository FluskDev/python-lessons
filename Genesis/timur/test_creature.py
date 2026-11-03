from andrey.creature import Creature


def test_position():
    c = Creature(x=3, y=4, genes={})
    assert c.x == 3
    assert c.y == 4


def test_genes():
    c = Creature(x=0, y=0, genes={"speed": 1.5, "size": 2.0})
    assert c.genes["size"] == 2.0


def test_energy_and_age():
    c = Creature(x=0, y=0, genes={})
    assert c.is_alive is True
    assert c.energy == 100.0
    assert c.age == 0


def test_tick():
    c = Creature(x=0, y=0, genes={"size": 2.0})
    c.tick()
    assert c.age == 1
    assert c.energy == 98.0  


def test_food():
    c = Creature(x=0, y=0, genes={})
    c.food(1.0)
    assert c.energy == 130.0  


def test_can_reproduce():
    c = Creature(x=0, y=0, genes={})
    c.energy = 200.0
    assert c.can_reproduce() is True
    c._alive = False
    assert c.can_reproduce() is False


def test_reproduce_with():
    a = Creature(x=1, y=1, genes={"size": 1.0})
    b = Creature(x=2, y=1, genes={"size": 1.0})
    child = a.reproduce_with(b)
    assert isinstance(child, Creature)
    assert child.is_alive is True