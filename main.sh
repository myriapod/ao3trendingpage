# install mariadb
sudo apt-get update
sudo apt-get install mariadb
# after configuring mariadb (user root, password root here)
# set up the ao3trendingpage database
mariadb -u root -proot < setup/sql-config.sql

# install python libraries requirements
pip install -r setup/requirements.txt

# copy the .env files
# a bit messy but it works
cp .env flask-website/.env
cp .env packages/.env

# run the data import once
sh setup/reload.sh
# set up the data import as a cron that runs every day at 3 am
(crontab -l 2>/dev/null; echo "0 3 * * * setup/reload.sh") | crontab -

sudo apt-get install nginx

sudo cp setup/ao3trendingpage.service /etc/systemd/system/ao3trendingpage.service
sudo systemctl daemon-reload
sudo systemctl start ao3trendingpage
sudo systemctl enable ao3trendingpage

sudo cp setup/ao3trendingpage.conf /etc/nginx/sites-available/ao4trendingpage.conf
sudo ln -s /etc/nginx/sites-available/ao4trendingpage.conf /etc/nginx/sites-enabled
sudo systemctl restart nginx

# run the flask app (in dev mode)
# env FLASK_APP=flask-website/website.py python3 -m flask run --debug
# deploy in prod with gunicorn
# gunicorn --config flask-website/gunicorn_config.py --chdir flask-website flask-website.website:app