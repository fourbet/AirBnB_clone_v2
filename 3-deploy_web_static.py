#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env

env.hosts = ['35.196.143.91', '35.243.151.189']


def do_pack():
    """generates a .tgz archive"""
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(datetime.strftime(
                                               datetime.now(),
                                               "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static"
                   .format(path))
    if result.failed:
        return None
    return path


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


def deploy():
    """creates and deploy archive"""
    path = do_pack()
    if path is None:
        return False
    print(path)
    res = do_deploy(path)
    return res
