import json

def test_get_user_profile(app, client):
    response = client.get('/user/49e1b6ab-c38a-43ab-a5d6-ee7cd6a6693e')
    assert response.status_code == 200
    expected = {
        "id": "49e1b6ab-c38a-43ab-a5d6-ee7cd6a6693e",
        "isActive": True,
        "name": {
        "first": "Young",
        "last": "Parsons"
        },
        "email": "young.parsons@undefined.me"
    }
    assert expected == json.loads(response.get_data(as_text=True))
