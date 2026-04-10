from utils import get_json, BASE_URL

def evolution_chain(pokemon_name):
    species = get_json(f"{BASE_URL}/pokemon-species/{pokemon_name}")
    evo_chain_url = species["evolution_chain"]["url"]
    chain = get_json(evo_chain_url)["chain"]

    def traverse(chain):
        names = [chain["species"]["name"]]
        for evo in chain["evolves_to"]:
            names.extend(traverse(evo))
        return names

    return traverse(chain)
