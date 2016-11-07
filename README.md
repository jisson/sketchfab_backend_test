# sketchfab_backend_test
Technical test for Sketchfab

A simple Django application allowing users to register, to create Model3d and to earn rewards as badges!

You can deploy that application using **Docker** (un tested!):

```
docker-compose up
```

or **Vagrant**:

```
vagrant up; vagrant ssh
```

Using Vagrant, you will also need to install requirements:

```
pip install -r requirements.txt
```

Once your environment is in place with requirements, don't forget:

```
# To sync your database
python manage.py migrate

# To collect static files
python manage.py collectstatic
```

Then, you will be able access to the index page:

```
http://127.0.0.1:8040/
```

and to browse the API:

```
http://127.0.0.1:8040/api/v1/
```

# Used libraries

* https://github.com/ulule/django-badgify

Simple app used on ulule.fr to handle badge features.

* https://github.com/thornomad/django-hitcount

App allowing per object / user session hit count.

* http://www.django-rest-framework.org/

Used to produce the REST api.
