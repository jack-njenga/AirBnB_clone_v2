#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import local
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
