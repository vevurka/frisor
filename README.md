# Frisor 

Frisor application is a box for urls.

# Local deployment

* create virtualenv: 
    
    `$ virtualenv -p python3 .venv`

* source it: 

    `$ source .venv/bin/activate`

* install requirements: 

    `$ pip install -r requirements.txt`

* run migrations:

    `$ python frisor/manage.py migrate`
    
* create static directory, default is `/tmp/static` (if other please 
adjust `STATIC_ROOT` in your `local_settings.py`), then run:

    `$ python frisor/manage.py collectstatic`

* run: 

    `$ python frisor/manage.py 8080`

