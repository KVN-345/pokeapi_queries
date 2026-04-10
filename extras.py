from utils import get_json, BASE_URL

def common_habitat_grass():
    data = get_json(f"{BASE_URL}/type/grass")
    habitats = {}
    for entry in data["pokemon"]:
        species = get_json(f"{BASE_URL}/pokemon-species/{entry['pokemon']['name']}")
        if species and species["habitat"]:
            hab = species["habitat"]["name"]
            habitats[hab] = habitats.get(hab, 0) + 1
    return max(habitats, key=habitats.get)

def lightest_pokemon():
    min_poke, min_weight = None, float("inf")
    for i in range(1, 1026):
        poke = get_json(f"{BASE_URL}/pokemon/{i}")
        if poke and poke["weight"] < min_weight:
            min_weight, min_poke = poke["weight"], poke["name"]
    return min_poke, min_weight
