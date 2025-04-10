#!/bin/bash

# Deploy the app on NGINX Docker container
#docker run --name ao3trendingpage-website -it -p 8080:80 -v ${pwd}/flask-website/templates/index.html:/usr/share/www/html/index.html -d nginx 


# Deploy the the mariadb database
#docker run --name ao3trendingpage-database -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d docker.io/library/mariadb:10.3
#docker build -t ao3trendingpage-database . && docker run -it -p 80:80 ao3trendingpage-database
#
#databaseip=`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ao3trendingpage-database`
#mysql -h $databaseip -u root -proot ao3trendingpage-database


# To open a bash terminal inside the container:
#docker exec -ti ao3trendingpage-database bash

sudo docker compose -f dockercompose.yml up &
sudo docker exec -i ao3trendingpage-database mysql -u root -proot < database/sql-config.sql
 