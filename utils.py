import requests
import urllib3

# Desactiva las advertencias de SSL inseguro
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://pokeapi.co/api/v2"

def get_json(url):
    """
    Realiza una petición GET a la PokeAPI y devuelve la respuesta en formato JSON.
    Desactiva la verificación SSL para evitar bloqueos en Windows.
    """
    try:
        resp = requests.get(url, timeout=10, verify=False)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")
        return None


