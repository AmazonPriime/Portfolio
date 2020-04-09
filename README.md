# Portfolio [here](https://luke-h.co/)

##### External Resources Used:
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [CKEditor](https://github.com/django-ckeditor/django-ckeditor) (for admin use)
* [Google Charts](https://developers.google.com/chart)

---

#### Setting up the Webserver
* Guide is from here [@_Christopher](https://medium.com/@_christopher/deploying-my-django-app-to-a-real-server-part-i-de78962e95ac) on [Medium](https://medium.com/)
* The guide is for Debian based systems - eg tutorial uses Ubuntu 17.10.1

1. Making sure the server is up to date
	* ```sudo apt-get update``` ```sudo apt-get upgrade```
2. Install Nginx, Gunicorn Python Virtualenv
	* ```sudo apt-get install nginx```
	* ```sudo pip3 install virtualenv```
3. Setup project
	* clone the project ```git clone https://github.com/AmazonPriime/Portfolio.git```
	* change directory into the project ```cd Portfolio```
	* setup virtual enviroment ```python3 -m venv env```
	* activate the virtual enviroment ```source env/bin/activate```
	* install the required packages ```pip3 install -r requirements.txt```
	* change directory to django project folder ```cd portfolio```
	* run collect static ```python3 manage.py collectstatic```
	* migrate database ```python3 manage.py makemigrations``` & ```python3 manage.py migrate```
	* turn debug mode off in ```settings.py``` ```DEBUG = False```
	* add your server ip or domain to ```ALLOWED_HOST = []```
4. Install Gunicorn while still in your virtual enviroment
	* ```pip3 install gunicorn```
	* bind it ```gunicorn --bind 0.0.0.0:8000 portfolio.wsgi:application```
	* get out of the virtual enviroment ```deactivate```
5. Create the Gunicorn service file
	* ```sudo nano /etc/systemd/system/gunicorn.service```
	* ```
      [Unit]
      Description=gunicorn service
      After=network.target
   
      [Service]
      User=chris
      Group=www-data
      WorkingDirectory=/home/<USERNAME>/Portfolio/porfolio/
      ExecStart=/home/<USERNAME>/Portfolio/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/<USERNAME>/Portfolio/portfolio/portfolio.sock portfolio.wsgi:application

      [Install]
      WantedBy=multi-user.target
      ```
	* Copy and paste while replacing the `<USERNAME>` with your account username
6. Enable Gunicorn
	* ```sudo systemctl enable gunicorn.service```
	* ```sudo systemctl start gunicorn.service```
	* ```sudo systemctl daemon-reload```
	* ```sudo systemctl restart gunicorn```
7. Configure Nginx
	* ```sudo nano /etc/nginx/sites-available/portfolio```
	* ```
      server {
             listen 80;    
             server_name 127.0.0.1;
             location = /favicon.ico {access_log off;log_not_found off;} 

             location /static/ {
               root /home/<USERNAME>/Portfolio/porfolio/static;    
             }

             location / {
               include proxy_params;
               proxy_pass http://unix:/home/<USERNAME>/Portfolio/portfolio/portfolio.sock;
             }
           }
   		```
	* Copy and paste while replacing `<USERNAME>` with your account username
8. Setup a link between the file created and the sites-enabled
	* ```sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled```
9. Make sure the Nginx file has no errors
	* ```sudo nginx -t```
9. Remove the default site
	* ```sudo rm /etc/nginx/sites-available/default```
	* ```sudo rm /etc/nginx/sites-enabled/default```
10. Restart Nginx
	* ```sudo systemctl restart nginx```
11. Now the site should be up, to allow outside access you'll need to portforward ```443``` and ```80```
