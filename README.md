# REST API for team management

## Installing Dependencies

    pip install -r requirements.txt

## making migrations
    
    python manage.py makemigrations
    
## applying migrations

    python manage.py migrate

## Run the app

    python manage.py runserver


# REST API

The REST API to the example app is described below.

## Get list of all users in JSON format

### Request

`GET /users/`

    curl -X GET http://127.0.0.1:8000/users 

## Create a new user

### Request

`POST /users/`

    curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/users/ -d "{\"firstName\":\"Udbhav\",\"lastName\":\"Agarwal\",\"email\":\"udbhav.agarwal7@gmail.com\",\"role\":\"Regular\",\"number\":\"250-891-8441\"}"

### Response

    {"message": "New User Udbhav Agarwal with email:udbhav.agarwal7@gmail.com created successfully"}

## Get a specific User by ID

### Request

`GET /user/id`

    curl -X GET http://127.0.0.1:8000/user/1

### Response

    {"id":"1", "firstName": "Udbhav", "lastName": "Agarwal", "email": "udbhav.agarwal7@gmail.com", "role":"Regular"}



## Change a Users's details

### Request

`PATCH /update-user/id`

    curl -X PATCH -H "Content-Type: application/json" http://127.0.0.1:8000/update-user/1 -d "{\"firstName\":\"Udbhav\",\"lastName\":\"agarwal\",\"email\":\"udbhav.agarwal7@gmail.com\",\"role\":\"Regular\",\"number\":\"250-891-8441\"}"

### Response

            {'message':"User Udbhav Agarwal with email:udbhav.agarwal7@gmail.com updated successfully"}


## Delete a User

### Request

`DELETE /update-user/id`

  curl -X DELETE http://127.0.0.1:8000/update-user/1

### Response

   {'message':"User Udbhav Agarwal  with email:udbhav.agarwal7@gmail.com deleted successfully"}


