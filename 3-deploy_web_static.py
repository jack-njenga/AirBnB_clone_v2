#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import *
from datetime import datetime
import os

fmt = "%Y%m%d%H%M%S"
env.hosts = ["100.26.161.31", "18.204.7.85"]


def do_pack():
    """
    generates a .tgz archive
    """
    local("mkdir -p versions")
    tm = datetime.strftime(datetime.now(), fmt)
    path = (f"versions/web_static_{tm}.tgz")
    result = local(f"tar -cvzf {path} web_static")

    if result.failed:
        return None
    else:
        return path


def do_deploy(archive_path):
    """
    Do deploy class
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


def deploy():
    """
    Deployment
    """
    path = do_pack()
    if path is None:
        return False
    else:
        return do_deploy(path)
