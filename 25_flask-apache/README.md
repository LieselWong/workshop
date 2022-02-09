# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time. 

### Estimated Time Cost: 10 minutes

### Prerequisites:

- A DigitalOcean droplet with Apache2 installed

NOTE: Whenever something is enclosed in angle brackets <like_this_in_snake_case>, that is something
you need to replace

1. SSH into an account with sudo privileges on your droplet
1. Update your apt packages `$ sudo apt update && sudo apt upgrade`
1. Install python3, pip3, and the venv package if you haven't already
    ```
    $ sudo apt install python3
    $ sudo apt install python3-pip
    $ sudo apt install python3.8-venv
    ```
1. Create the main app directory `$ sudo mkdir -p /var/www/<app_name>` and cd into it `$ cd /var/www/<app_name>`
1. Make a virtual environment `$ sudo python3 -m venv venv` and activate it `$ source venv/bin/activate`
1. Install flask in the venv `$ sudo pip3 install flask`
1. Deactivate the venv `$ deactivate`
1. Create the wsgi file `$ sudo nano <wsgi_file>.wsgi` and write the following inside it:
    ```wsgi
    import sys

    sys.path.insert(0, "var/www/<app_name>")

    from app import app as application
    application.secret_key = <secret_key>
    ```
1. Create the flask app directory `$ sudo mkdir app` and cd into it `cd app`
1. Set up the `__init__.py` file `$ sudo nano __init__.py`, the contents should look something like:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/)
    def hello():
        return "Hello, World!"

    if __name__ == "__main__":
        app.run()
    ```
1. cd into the `sites-available` directory `$ cd /etc/apache2/sites-available`
1. Create a config file for the flask app `$ sudo nano <app_name>.conf` and write the following:
    ```conf
    <VirtualHost *>
        ServerName <ip_address>

        WSGIDaemonProcess <app_name> python-home=/var/www/<app_name>/venv

        WSGIProcessGroup <app_name>
        WSGIApplicationGroup %{GLOBAL}

        WSGIScriptAlias / /var/www/<app_name>/<wsgi_file>.wsgi
        <Directory /var/www/<app_name>>
            Require all granted
        </Directory>
        
        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
    ```
1. Dissite and ensite the default page and flask app respectively `$ sudo a2dissite 000-default.conf && sudo a2ensite <app_name>.conf`
1. Reload apache `$ sudo service apache2 reload`
1. Navigate to `<ip_address>` on your web browser and check if the flask app correctly loads


### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
* https://flask.palletsprojects.com/en/2.0.x/deploying/mod_wsgi/
* https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html

---

Accurate as of (last update): 2022-01-19

#### Contributors:  
Wen Hao Dong, pd2  
Liesel Wong, pd2  
