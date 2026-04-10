from utils import get_json, BASE_URL
from classification import fire_pokemon_kanto

def main():
    # Prueba rápida con Ditto
    ditto = get_json(BASE_URL + "/pokemon/ditto")
    if ditto:
        print("Ditto cargado:", ditto["name"], "ID:", ditto["id"])
    else:
        print("No se pudo cargar Ditto")

    # Consulta de Pokémon de tipo fuego en Kanto
    fire_kanto = fire_pokemon_kanto()
    print("\nPokémon de tipo fuego en Kanto:")
    for pk in fire_kanto:
        print(" -", pk)

if __name__ == "__main__":
    main()
