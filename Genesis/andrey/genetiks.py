import random
import json

GENERANGES = {
    "speed":(0.5,3.0),
    "size":(1.0,3.0),
    "vision":(1.0,5.0),
    "agression":(0.0,1.0)
}

def random_genom() -> dict:
    return {
        gene: random.uniform(lo, hi)
        for gene,(lo,hi) in GENERANGES.items()
    }

def save_genom(genome: dict, path: str) ->None:
    with open(path,"w",encoding="utf-8") as f:
        json.dump(genome,f,ensure_ascii=False,indent=2)

def load_genom(path: str) -> dict:
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)
    