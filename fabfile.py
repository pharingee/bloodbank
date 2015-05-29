from fabric.api import local


def mmig():
    local('foreman run ./manage.py makemigrations')


def rs():
    local('foreman run ./manage.py runserver')


def mig():
    local('foreman run ./manage.py migrate')


def csu():
    local('foreman run ./manage.py createsuperuser')


def test():
    local('foreman run ./manage.py test')
