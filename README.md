# Site de Disquettes
Thuis repos contains the code for a dashboard showing multiple data.
# to install:
you need to create a .env file (there is a template `template.env`)

(go in the project's root directory)
create a venv:
`python -m venv env`
activate it (`source env/bin/activate` on linux)
install the dependencies: `pip install -r requirements.txt`

then for the first run, do:
`python manage.py makemigrations`
and
`python manage.py migrate`


you can then run the project with: `python manage.py runserver`
