#!/usr/bin/python3
"""
Distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import *
import os
from datetime import datetime

fmt = "%Y%m%d%H%M%S"
env.hosts = ["100.26.161.31", "18.204.7.85"]

def do_pack():
    """
    Generates a ".tgz" file
    """
    local("mkdir -p versions")
    dt = datetime.strftime(datetime.now(), fmt)
    path = (f"versions/web_static_{dt}.tgz")
    result = local(f"tar -cvzf {path} web_static")

    if result.failed:
        return None
    return path


def do_deploy(archive_path):
    """
    do_deploy method
    """
    if not os.path.exists(archive_path):
        return False
    else:
        put(archive_path, "/tmp/")
        name = archive_path.split("/")[-1]
        no_fmt = name.split(".")[0]
        path = "/data/web_static/releases/"

        sudo(f"mkdir -p {path}{no_fmt}/")
        sudo(f"tar -xvf /tmp/{name} -C {path}{no_fmt}/")
        sudo(f"rm /tmp/{name}")
        sudo(f"mv {path}{no_fmt}/web_static/* {path}{no_fmt}/")
        sudo(f"rm -rf {path}{no_fmt}/web_static")
        sudo(f"rm -rf /data/web_static/current")
        sudo(f"ln -s {path}{no_fmt} /data/web_static/current")

        print("New version deployed!")
        return True
