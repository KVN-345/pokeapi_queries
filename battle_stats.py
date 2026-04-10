from utils import get_json, BASE_URL

def strongest_attack_johto():
    max_poke, max_attack = None, 0
    for i in range(152, 252):
        poke = get_json(f"{BASE_URL}/pokemon/{i}")
        if poke:
            attack = next(stat["base_stat"] for stat in poke["stats"] if stat["stat"]["name"] == "attack")
            if attack > max_attack:
                max_attack, max_poke = attack, poke["name"]
    return max_poke, max_attack
