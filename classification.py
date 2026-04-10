from utils import get_json, BASE_URL

def fire_pokemon_kanto():
    """
    Devuelve la lista de Pokémon de tipo fuego que pertenecen a la región Kanto (ID <= 151).
    """
    fire_pokemon = [
        "charmander", "charmeleon", "charizard",
        "vulpix", "ninetales",
        "growlithe", "arcanine",
        "ponyta", "rapidash",
        "magmar", "flareon", "moltres"
    ]
    result = []
    for name in fire_pokemon:
        data = get_json(f"{BASE_URL}/pokemon/{name}")
        if data and data.get("id", 9999) <= 151:
            result.append(f"{data['id']} - {data['name']}")
    return result
