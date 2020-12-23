def test_get(client):
    response = client.get("movies")
    assert response.status_code == 200


def test_post(client):
    headers = {"content-type": "application/json"}
    data = {
        "name": "The Dark Knight",
        "casts": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
        "genres": ["Action", "Crime", "Drama"]
    }
    response = client.post("movies",
                           headers=headers,
                           json=data)
    assert response.status_code == 200


def test_put(client):
    headers = {"content-type": "application/json"}
    data = {
        "name": "The Dark Knight",
        "casts": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
        "genres": ["Action", "Crime", "Drama"]
    }
    response = client.put("movies/1",
                          headers=headers,
                          json=data)
    assert response.status_code == 200


def test_delete(client):
    response = client.delete("movies/1")
    assert response.status_code == 200
