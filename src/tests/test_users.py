import json
from datetime import datetime as dt
from faker import Faker

fake = Faker()

def test_create_user(test_app):
    test_create_user_payload = {
        "email": fake.email(),
        "username": fake.user_name()
    }

    response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    assert response.status_code == 201

    created_user = response.json()

    assert created_user is not None
    assert created_user["id"] is not None

    assert test_create_user_payload["email"] == created_user["email"]
    assert test_create_user_payload["username"] == created_user["username"]
    assert created_user["created_at"] is not None

def test_get_user(test_app):
    test_create_user_payload = {
        "email": fake.email(),
        "username": fake.user_name()
    }

    creation_response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    assert creation_response.status_code == 201

    created_user = creation_response.json()
    assert created_user is not None

    found_user_response = test_app.get("/v1/users/{}".format(created_user["id"]))
    found_user = found_user_response.json()

    assert found_user is not None
    assert created_user["id"] is not None

    assert test_create_user_payload["email"] == found_user["email"]
    assert test_create_user_payload["username"] == found_user["username"]
    assert found_user["created_at"] == created_user["created_at"]

def test_get_users(test_app):
    test_create_user_payload = {
        "email": fake.email(),
        "username": fake.user_name()
    }

    creation_response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    created_user = creation_response.json()

    found_user_response = test_app.get("/v1/users")
    found_users = found_user_response.json()

    assert found_users is not None
    assert len(found_users) > 0

    found_created_user = None
    for found_user in found_users:
        if found_user["id"] == created_user["id"]:
            found_created_user = found_user
            break
    
    assert found_created_user is not None
    assert found_created_user["id"] is not None

    assert found_created_user["email"] == created_user["email"]
    assert found_created_user["username"] == created_user["username"]
    assert found_created_user["created_at"] == created_user["created_at"]

def test_update_user(test_app):
    test_create_user_payload = {
        "email": fake.email(),
        "username": fake.user_name()
    }

    creation_response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    assert creation_response.status_code == 201

    created_user = creation_response.json()
    assert created_user is not None

    test_new_email = fake.email()
    test_create_user_payload["email"] = test_new_email

    updated_user_response = test_app.put("/v1/users/{}".format(created_user["id"]), data=json.dumps(test_create_user_payload))
    updated_user = updated_user_response.json()

    assert updated_user is not None
    assert updated_user["id"] is not None

    assert updated_user["email"] == test_new_email 
    assert updated_user["username"] == test_create_user_payload["username"]
    assert updated_user["created_at"] == created_user["created_at"]

def test_destroy_user(test_app):
    test_create_user_payload = {
        "email": fake.email(),
        "username": fake.user_name()
    }

    creation_response = test_app.post("/v1/users", data=json.dumps(test_create_user_payload))
    assert creation_response.status_code == 201

    created_user = creation_response.json()
    assert created_user is not None

    deletion_response = test_app.delete("/v1/users/{}".format(created_user["id"]))
    deleted_user = deletion_response.json()

    assert deleted_user is not None
    assert deleted_user["id"] is not None

    assert deleted_user["email"] == created_user["email"]
    assert deleted_user["username"] == created_user["username"]
    assert deleted_user["created_at"] == created_user["created_at"]

    found_deleted_user_response = test_app.get("/v1/users/{}".format(deleted_user["id"]))
    found_deleted_user = found_deleted_user_response.json()

    # make sure the user record was actually deleted
    assert found_deleted_user is None
