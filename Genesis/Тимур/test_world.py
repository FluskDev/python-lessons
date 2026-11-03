from andrey.creature import Creature
from timur.world import World


def test_world_creation():
    w = World(10, 5)
    assert w.width == 10
    assert w.height == 5
    assert w.creatures == []
    assert w.food == {}


def test_add_food_in_bounds():
    w = World(10, 10)
    w.add_food(3, 5, value=2.0)
    assert w.food[(3, 5)] == 2.0


def test_add_food_out_of_bounds_ignored():
    w = World(10, 10)
    w.add_food(100, 100, value=99.0)
    assert w.food == {}


def test_add_creature():
    w = World(10, 10)
    c = Creature(x=3, y=4, genes={"size": 1.0})
    w.add_creature(c)
    assert len(w.creatures) == 1
    assert w.creatures[0] is c


def test_add_creature_out_of_bounds_ignored():
    w = World(10, 10)
    c = Creature(x=100, y=100, genes={})
    w.add_creature(c)
    assert w.creatures == []


def test_alive_creatures_filter():
    w = World(10, 10)
    alive = Creature(x=0, y=0, genes={})
    dead = Creature(x=1, y=1, genes={})
    dead._alive = False
    w.add_creature(alive)
    w.add_creature(dead)
    assert w.alive_creatures == [alive]