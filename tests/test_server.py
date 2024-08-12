import requests


def test_connection():
    try:
        r = requests.get("http://localhost:5000/get_data/Janey%20Jackay")
        if r.status_code == 200:
            print("Connection successful")
        else:
            print(f"Failed with status code: {r.status_code}")
    except requests.ConnectionError:
        raise ValueError("Connection couldn't be made. Is `app.py` running?")


def test_results():
    # Send a GET request to the endpoint with an author's name
    author = "Janey Jackay"  # Change this to a valid author name you want to test
    r = requests.get(f"http://localhost:5000/get_data/{author}")

    assert r.status_code == 200, f"Request failed with status code {r.status_code}"

    # Get the JSON response
    result = r.json().get("result", [])

    assert isinstance(result, list), "Result should be a list"
    assert len(result) > 0, "Result should not be empty"

    print("Test results passed")
