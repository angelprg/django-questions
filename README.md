[![Build Status](https://www.travis-ci.com/angelprg/django-questions.svg?branch=main)](https://www.travis-ci.com/angelprg/django-questions)
# django-questions
Simple system of questions and answers.

## Rules
Registered users can:
- Ask a new question.
- Respond other user's questions. (Users can't respond to him/her selves)

Anybody can:
- See questions and answers.
- See some statistic information about the questions.

## Technologies
- Django
- Docker
- Docker-compose
- Travis-ci
- D3.js

## Demo Page:
`http://104.197.84.217`
Deploy on Compute Engine (Google Cloud Platform)

## Local Setup:
You can replace `SomeStrongPassword` for an environment variable locally or use as in examples, defining it in every call.

Download git repsitory
`https://github.com/angelprg/django-questions.git`

Create docker-compose image
`DBPASSWORD=SomeStrongPassword docker-compose build`

Apply migrations to database
`DBPASSWORD=SomeStrongPassword docker-compose run app sh -c "python manage.py migrate"`

Creating a superuser, so we can access to Django admin interface
`DBPASSWORD=SomeStrongPassword docker-compose run app sh -c "python manage.py createsuperuser"`

Script to populate DB with mock data, in order to test it.
`DBPASSWORD=SomeStrongPassword docker-compose run app sh -c "python manage.py populate"`

Optionally you can check tests runs correctly
`DBPASSWORD=SomeStrongPassword docker-compose run app sh -c "python manage.py test && flake8"`

You can start the server
`DBPASSWORD=SomeStrongPassword docker-compose up`

And open some browser with the url:
`http://127.0.0.1:8000/`
