import requests

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json",
    "X-Authentication": AUTH_TOKEN
}

def test_articulos():
    print("Probando /data/articulos...")
    try:
        response = requests.get(f"{API_URL}/data/articulos", headers=HEADERS)
        print(f"Status Code: {response.status_code}")
        print("Headers:", response.headers)
        print("Response:", response.text[:200] + "..." if len(response.text) > 200 else response.text)
    except Exception as e:
        print("Error:", e)

def test_vendedores():
    print("\nProbando /data/vendedores...")
    try:
        response = requests.get(f"{API_URL}/data/vendedores", headers=HEADERS)
        print(f"Status Code: {response.status_code}")
        print("Headers:", response.headers)
        print("Response:", response.text[:200] + "..." if len(response.text) > 200 else response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_articulos()
    test_vendedores() 