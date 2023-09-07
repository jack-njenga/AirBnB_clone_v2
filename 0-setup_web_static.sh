#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# installing nginx if not installed
if command -v nginx > /dev/null;
then
	echo "Nginx Already Installed"
else
	echo "Installing Nginx"
	sudo apt-get update
	sudo install -y nginx
fi

# /data/ dir
if ! [ -d "/data/" ];
then
	sudo mkdir "/data/"
fi
if ! [ -d "/data/web_static/" ];
then
	sudo mkdir "/data/web_static/"
fi
if ! [ -d "/data/web_static/releases/" ];
then
	sudo mkdir "/data/web_static/releases/"
fi
if ! [ -d "/data/web_static/shared/" ];
then
	sudo mkdir "/data/web_static/shared/"
fi
if ! [ -d "/data/web_static/releases/test/" ];
then
	sudo mkdir -p "/data/web_static/releases/test/"
fi

html_content="<html>
<head>
	<title>Nginx Config Test HTML Page</title>
</head>
<body>
	<h1>Welcome to my Nginx Config Test HTML page!</h1>
	<p>Sample HTML file.</p>
</body>
</html>"

echo "$html_content" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

if [ -L "/data/web_static/current" ];
then
	sudo rm "/data/web_static/current"
	echo "symbolic link removed"
fi

sudo ln -s "/data/web_static/releases/test" "/data/web_static/current"

sudo chown -R ubuntu:ubuntu "/data/"

# configuring hbnb_static page reponse
if grep -R "hbnb_static" /etc/nginx/sites-available/default > /dev/null;
then
	echo "hbnb_static Already Configured"
else
	sudo sed -i '/^\tlocation \/ {$/a \\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default;
	echo "hbnb_static Configured"
fi

sudo service nginx restart
