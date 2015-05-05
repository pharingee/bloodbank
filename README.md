#JustPay API

##Installation
- After pushing to the hosting platform of your choice run:

````
$ python manage.py migrate
$ python justpay.wsgi.py
````

- Make sure the following environment variables are set

````
ENVIRONMENT
DEBUG
SECRET_KEY
DATABASE
````

- `ENVIRONMENT` can be either `localhost`, `production` or `test`
- `DEBUG` is either `True` or `False`
- `SECRET_KEY` is a 60-character string
- `DATABASE_URL` is the postgres database url, in the format `postgres://{username}{password}@{URL}/{database_name}`

