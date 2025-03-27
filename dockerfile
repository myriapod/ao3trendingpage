FROM ubuntu:latest
RUN apt-get -y update && apt-get -y install nginx 

COPY content/index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]