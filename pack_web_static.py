#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    fmt = "%Y%m%d%H%M%S"

    local("mkdir -p versions")

    now = datetime.now()
    timestamp = now.strftime(fmt)
    name = f"web_static_{timestamp}.tgz"
    result = local(f"tar -czvf versions/{name} web_static")

    if result.succeeded:
        return f"versions/{name}"
    else:
        return None


