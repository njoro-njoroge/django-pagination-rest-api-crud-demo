Django REST API with Pagination and CRUD Operations

This project demonstrates how to implement basic CRUD (Create, Read, Update, Delete) operations with pagination using
Django Rest Framework (DRF). The API provides endpoints to manage a simple fruit inventory, allowing users to add, view,
update, delete, and paginate through fruit records.

Features
CRUD operations: Easily manage fruit records with create, read, update, and delete capabilities.
Pagination: Retrieve fruit records in a paginated format, making it easier to manage large datasets.

Setup
Clone the repository:

bash

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    Create a virtual environment:

bash

    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install dependencies:
bash

    pip install -r requirements.txt
    Apply migrations:

bash

    python manage.py makemigrations
    python manage.py migrate

Create a superuser (for accessing the admin panel):
bash

    python manage.py createsuperuser

Follow the prompts to set up the username, email, and password for the admin account. Once created, you can access the
Django admin interface to manage fruits.

Start the development server:

bash

    python manage.py runserver

API Endpoints

The API provides the following endpoints for managing fruits.

1. Get List of Fruits (with Pagination)
   Endpoint: http://localhost:8000/api/fruits/
   Method: GET

Returns a paginated list of fruits, with a default of 5 items per page.

Example response

        {
            "count": 21,
            "next": "http://127.0.0.1:8000/api/fruits/?page=2",
            "previous": null,
            "results": [
                {
                    "url": "http://127.0.0.1:8000/api/fruits/1/",
                    "id": 1,
                    "fruit_name": "Bananas",
                    "stock": 300
                },
                ...
            ]
        }

2. Create a New Fruit
   Endpoint: http://localhost:8000/api/fruits/create/
   Method: POST
   Request Body:

json

    {
        "fruit_name": "Fig",
        "stock": 500
    }

Response:

Returns the created fruit data.

3. Retrieve, Update, or Delete a Fruit by ID
   Endpoint: http://localhost:8000/api/fruits/<int:pk>/
   Methods:

GET: Retrieves details of a specific fruit.

Response:
json

        {
            "results": {
                "url": "http://127.0.0.1:8000/api/fruits/10/",
                "id": 10,
                "fruit_name": "Fig",
                "stock": 500
            }
        }

PUT: Updates details of a specific fruit.

Request Body:
json

        {
            "fruit_name": "Fig",
            "stock": 600
        }

Response:
json

        {
            "message": "Update successful",
            "results": {
                "url": "http://127.0.0.1:8000/api/fruits/10/",
                "id": 10,
                "fruit_name": "Fig",
                "stock": 600
            }
        }

DELETE: Deletes a specific fruit.

Response:
json

        {
            "message": "Fruit deleted successfully"
        }

Admin Interface
The Django admin interface can be accessed at http://127.0.0.1:8000/admin/. Log in with the superuser credentials you
created during setup to manage Fruit entries directly.