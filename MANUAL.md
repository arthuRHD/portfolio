# Steps of manual deployement

- Install the prerequisites

```sh
sudo apt update -y
sudo apt install -y python3-pip apache2 libapache2-mod-wsgi-py3
```

- Clone the project in an allowed directory by `/etc/apache2/apache2.conf`
- Choose between sqlite3 or your custom database in `/core/core/settings.py`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# or MySQL for example
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': prod.MYSQL_DB_NAME,
        'USER': prod.MYSQL_USER,
        'PASSWORD': prod.MYSQL_PASSWORD,
        'HOST': prod.MYSQL_HOST,
        'PORT': prod.MYSQL_PORT,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
```

- Migrate the database

```sh
cd /var/www/vhosts/core
sudo pip3 install -r requirements.txt
sudo python3 manage.py migrate
```

- Set these parameters in `/core/core/production.py`

```python
DEBUG = False
# if your database engine is MySQL, otherwise leave these empty
MYSQL_USER = '<insert_user>'
MYSQL_PASSWORD = '<insert_password>'
MYSQL_DB_NAME = '<insert_dbname>'
MYSQL_HOST = '<insert_host>'
MYSQL_PORT = '3306'

ALLOWED_HOSTS = ['portfolio.richardinfo.fr']

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = '/var/www/vhosts/core/static'
MEDIA_ROOT = '/var/www/vhosts/core/media'
```

- Collect static files

```sh
cd /var/www/vhosts/core
sudo python3 manage.py collectstatic
```

- Set the virtualhost for apache2

```sh
sudo nano /etc/apache2/sites-available/my-site.conf
# Copy the configuration below
sudo a2enmod wsgi
sudo a2ensite my-site.conf
sudo service apache2 reload
```

## VirtualHost

```apacheconf
<VirtualHost *:80>
        ServerName portfolio.richardinfo.fr
        ServerAdmin arthur.richard2299@gmail.com
        DocumentRoot /var/www/vhosts/core

        Alias /favicon.ico /var/www/vhosts/core/static/images/favicon.ico

        Alias /static /var/www/vhosts/core/static
        <Directory /var/www/vhosts/core/static>
                Options FollowSymLinks
                Require all granted
        </Directory>

        Alias /media /var/www/vhosts/core/media
        <Directory /var/www/vhosts/core/media>
                Options FollowSymLinks
                Require all granted
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/richardinfo_error.log
        CustomLog ${APACHE_LOG_DIR}/richardinfo_access.log combined

        WSGIDaemonProcess portfolio.richardinfo.fr processes=2 threads=15
        WSGIProcessGroup portfolio.richardinfo.fr
        WSGIScriptAlias / /var/www/vhosts/core/core/wsgi.py

        <Directory /var/www/vhosts/core/core>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>
</VirtualHost>
```
