# Django_REST_PostgreSQL

Data communication: The main purpose of this project is to showcase the seamless communication between Django REST and PostgreSQL. It demonstrates how data can be stored, retrieved, updated, and deleted through the API endpoints.

## Installation and Usage
To set up the project locally, follow these steps:

- Clone the repository
- Create a virtual environment: python3 -m venv env
- Activate the virtual environment: source env/bin/activate
- Install the dependencies: pip install -r requirements.txt
- Set up the PostgreSQL database and update the configuration in the project's settings file.
- Apply the database migrations: python manage.py migrate
- Start the development server: python manage.py runserver

## Workout:
Django comes with a SQLite database which is great for testing and debugging at the beginning of a project.However, it is not very suitable for production. PostgreSQL database is an open source relational database, which should cover most demands you have when creating a database for a Django project.
official postgresql website: https://www.postgresql.org/download/linux/redhat/
https://developer.fedoraproject.org/tech/database/postgresql/about.html

During the PostgreSQL installation process, a default user called "postgres" is created.
Switch to the "postgres" user by running the following command:
```
sudo -u postgres psql
```
Reset the password by running the following command:
```
ALTER USER postgres WITH PASSWORD 'new_password';
```
When i registered in pgAdmin in my fedora linux, i faced some problem like fetal error: to solve this i tried the following method:
Switch to the "postgres" user by running the following command:
```
sudo -u postgres bash
```
in the "postgres" user, locate the data directory by running the following command:
```
psql -c "SHOW data_directory;"
```
This command will display the path to the PostgreSQL data directory. Inside the data directory, you should find the pg_hba.conf file.
Open the pg_hba.conf file using the nano/vi/vim text editor:
```
nano pg_hba.conf
```
Change the authentication method from ident to md5 or password. The line should look like one of the following:
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            ident
# IPv6 local connections:
host    all             all             ::1/128                 ident
```
to
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            password
# IPv6 local connections:
host    all             all             ::1/128                 password
```
after making these changes, save the pg_hba.conf file and restart the PostgreSQL service for the changes to take effect.
some command:
```
systemctl status postgresql
sudo /usr/pgsql-15/bin/postgresql-15-setup initdb
sudo systemctl enable postgresql-15
sudo systemctl start postgresql-15
sudo systemctl stop postgresql-15
sudo systemctl restart postgresql-15
```







