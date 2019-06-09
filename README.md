SambilProject
Proyecto de administracion de base de datos

Para comenzar el proyecto debe instalar las siguientes librerias de python Django

#--------------------------------------------------------------------------------------------------------------------------------------------------#

Windows pip install django

Luego que se instale la libreria se procede a correr el proyecto:

python manage.py makemigrations ( para guardar los cambios realizados en la base de datos )

python manage.py migrate ( para crear las tablas en la base de datos )

python manage.py createsuperuser ( crear un usuario para loggearte y ver la pagina administrativa del proyecto "opcional" )

python3.6 manage.py runserver localhost:puerto ( Comando para correr el proyecto, ejemplo python3.6 manage.py runserver localhost:8000)

#--------------------------------------------------------------------------------------------------------------------------------------------------#

Linux ( Ubuntu ):

sudo apt update
sudo apt install python3-django
django-admin --version ------> output 1.11.11 u otras versionas mas recientes
sudo apt install python3-pip
pip install django
python manage.py makemigrations ( para guardar los cambios realizados en la base de datos )
python manage.py migrate ( para crear las tablas en la base de datos )
python manage.py createsuperuser ( crear un usuario para loggearte y ver la pagina administrativa del proyecto "opcional" )
python manage.py runserver localhost:puerto ( Comando para correr el proyecto, ejemplo python3.6 manage.py runserver localhost:8000)
