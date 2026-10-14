from andrey.creature import Creature

def test_creature_starts_alive():
    genes = {"speed": 1.5, "size": 2.0, "vision": 3.0, "agression": 0.1}
    c = Creature(x = 0, y = 0, genes = genes)
    assert c.is_alive
    assert c.energy == 100.0
    assert c.age == 0

def test_creature_has_position():
    c = Creature(x = 5, y = 7, genes = {})
    assert c.x == 5
    assert c.y == 7

def test_creature_has_genes():
    genes = {"speed": 2.0, "size": 1.5, "vision": 4.0, "agression": 0.5}
    c = Creature(x = 0, y = 7, genes = genes)
    assert c.genes["speed"] == 2.0
    assert c.genes["agression"] == 0.5


