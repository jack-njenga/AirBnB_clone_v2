#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# installing nginx if not installed
if command -v nginx > /dev/null;
then
	echo "Nginx Already Installed">/dev/null
else
	echo "Installing Nginx"
	sudo apt-get update>/dev/null
	sudo install -y nginx>/dev/null
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
	<h1>Hello this Nginx Config Test HTML page!</h1>
	<p>Sample HTML file.</p>
</body>
</html>"

echo "$html_content" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

sudo ln -sf "/data/web_static/releases/test" "/data/web_static/current"

sudo chown -R "ubuntu:ubuntu" /data
config='\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current/;\n\t\}'
path="/etc/nginx/sites-available/default"

# configuring hbnb_static page reponse
if grep "location /hbnb_static {" "$path">/dev/null;
then
	echo "hbnb_static Already Configured">/dev/null
else
	sudo sed -i "/^\s*server\s/a $config" "$path"
	echo "hbnb_static Configured">/dev/null
fi
sudo service nginx restart>/dev/null
# sudo nginx -s reload
