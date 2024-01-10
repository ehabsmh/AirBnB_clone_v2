#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static

# Install Nginx if it not already installed
apt-get -y update
apt-get -y install nginx

# Create the necessary folders and files
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello world" > /data/web_static/releases/test/index.html

# Create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/
sed -i "/server_name _;/ a\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

service nginx restart
