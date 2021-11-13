# Installation

python -m venv env
.\env\Scripts\activate
pip install -r .\requirements.txt
cd app

!!!CHANGE app/settings.py DATABASES to own database instance  

python .\manage.py makemigrations
python .\manage.py makemigrations api
python .\manage.py makemigrations service
python .\manage.py migrate
python .\manage.py collectstatic
python .\manage.py createsuperuser
python .\manage.py runserver

# routes
/ - resorts aggregation page
/landing - landing
/admin - admin panel
/api/... - api paths