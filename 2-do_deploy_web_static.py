#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env

env.hosts = ['35.196.143.91', '35.243.151.189']

def do_deploy(archive_path):
    """deploy a .tgz archive"""
    if not os.path.exists(archive_path):
        return False
    archive_ext = archive_path.split("/")
    res = put(archive_path, "/tmp/{}".format(archive_ext[1]))
    if res.failed:
        return False
    archive = archive_ext[1].split(".")
    res = run("mkdir -p /data/web_static/releases/{}/".format(archive[0]))
    if res.failed:
        return False
    res = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
              .format(archive_ext[1], archive[0]))
    if res.failed:
        return False
    res = run("rm /tmp/{}".format(archive_ext[1]))
    if res.failed:
        return false
    res = run("mv /data/web_static/releases/{}/web_static/* \
    /data/web_static/releases/{}/".format(archive[0], archive[0]))
    if res.failed:
        return false
    res = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(archive[0]))
    if res.failed:
        return false
    res = run("rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(archive[0]))
    if res.failed:
        return False
    print('New version deployed!')
    return True
