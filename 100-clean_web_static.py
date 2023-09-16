#!/usr/bin/python3
"""
Based on the file 3-deploy_web_static.py
"""
from fabric.api import env, local, run
from datetime import datetime
import os

env.hosts = ["100.26.161.31", "18.204.7.85"]
fmt = "%Y%m%d%H%M%S"


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
    deploy
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


def do_clean(number=0):
    """
    Deletes outdated .tgz files
    """
    try:
        n = max(int(number), 1)
        files = local("ls -1t versions", capture=True).split("\n")
        for fl in files[n:]:
            local(f"rm -r versions/{fl}")
        dirs = run("ls -1t /data/web_static/releases").split("\n")
        for dr in dirs[n:]:
            if "web_static" in dr:
                run(f"rm -rf /data/web_static/releases/{dr}")
    except Exception as e:
        print("--E--:", e)
        pass
