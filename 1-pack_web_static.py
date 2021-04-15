#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""

from fabric.operations import local
from datetime import datetime

def do_pack():
    """generates a .tgz archive"""
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(datetime.strftime(
                                                   datetime.now(), "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static"
                   .format(path))
    if result.failed:
        return None
    return path
