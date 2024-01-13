#!/usr/bin/python3
"""Generates a .tgz archive"""

from fabric.api import put, run, env

env.hosts = ['54.242.168.59', '52.206.252.73']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """ Deploy archive to server """
    fd = archive_path.split("/")[1]
    try:
        put(archive_path, "/tmp/{}".format(fd))
        run("rm -r /data/web_static/releases/{}".format(fd))
        run("mkdir -p /data/web_static/releases/{}".format(fd))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(fd, fd))
        run("rm /tmp/{}".format(fd))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(fd, fd))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fd))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
        /data/web_static/current".format(fd))
        print("New version deployed!")
        return True
    except Exception:
        print("Deployment failed!")
        return False
