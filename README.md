# Random Restaurant

This is a simple Django app that makes a request to the random-data-api.com API, using the Food resource. When a logged in user enters the menu screen, they are presented with five randomly provided food dishes, and asked to choose their meal. Once their order has been placed, Django grabs the form fields “dish” and “description” and uses them as well as the logged in user and current time to create a new Order model instance. You are then taken to the order pending screen, which has a five second countdown timer, while the order is “prepared”. After this 5 second delay, the Javascript frontend makes a request to the Django Rest Framework API to update the order fulfilled field for the order, and updates the status on the page to fulfilled. The application utilizes the django User model, and some built- in forms to handle user registration and logins.


### Requirements:
- Python 3.8+
- pip or pipenv

## Installation Instructions:

1. git clone https://github.com/imasnyper/RandomRestaurant.git
2. cd into RandomRestaurant
3. Use pip or pipenv to install the requirements
    - `pip install -r requirements.txt`
    - Or, `pipenv install`
5. (Pipenv) Activate virtual environment environment `pipenv shell`
6. Add .env file to RandomRestaurant/RandomRestaurant folder(same folder as settings.py)
6. Add `UNSPLASH_TOKEN=<token>`
7. Add `DRF_TOKEN=` to .env file as a placeholder for the settings file
8. Run `python manage.py makemigrations users orders`
9. Run `python manage.py migrate`
10. Create API superuser for Django Rest Framework frontend authentication
    - `python manage.py createsuperuser --username api --email <any email>`
    - Follow instructions to add password for user
    - `python manage.py drf_create_token api`
    - Add `DRF_TOKEN=<generated-token>` to the .env file

## Running Instructions:
1. python manage.py runserver
