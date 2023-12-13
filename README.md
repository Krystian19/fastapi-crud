## Demo Fast API web server

Simple demo CRUD web server implementation using Fast API

### Requirements

```sh
$ python3 --version
Python 3.11.4 # Or later
```

### How to setup

```sh
# install dependencies
pip3 install -r ./src/requirements.txt
```

```sh
# run the web server
python3 ./src/main.py
```

And voilà, your web server should be running @ http://localhost:3000

### Notes:

These are the existing endpoints:

```sh
# returns a list of all the existing users
GET /v1/users

# response
{
    "email": "john.doe@gmail.com",
    "username": "john.doe",
    "created_at": "Y-M-D H:M"
} # Or null in case the user was not found
```

```sh
# find a user with id
GET /v1/users/{user_id}

# response
[
    {
        "email": "john.doe@gmail.com",
        "username": "john.doe",
        "created_at": "Y-M-D H:M"
    }
]
```

```sh
# deletes a user with id
DELETE /v1/users/{user_id}

# response
{
    "email": "john.doe@gmail.com",
    "username": "john.doe",
    "created_at": "Y-M-D H:M"
} # Or null in case the user was not found
```
