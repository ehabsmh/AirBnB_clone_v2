#!/usr/bin/python3
"""Generates a .tgz archive"""

from fabric.api import put, run, env
import os

env.hosts = ['54.242.168.59', '52.206.252.73']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    # Check if file at the path archive_path doesn’t exist
    if not os.path.exists(archive_path):
        return False

    archive_file = archive_path.split("/")[-1]
    archive_name = archive_file.split(".")[0]
    releases_path = "/data/web_static/releases"

    # Upload the archive to the /tmp/ directory of the web server
    if put(archive_path, f"/tmp/{archive_file}").failed:
        return False

    # Create the release directory for ex: web_static_20170315003959
    if run(f"mkdir -p {releases_path}/{archive_name}/").failed:
        return False

    # Uncompress the archive
    if run(f"tar -xzf /tmp/{archive_file} -C {releases_path}/{archive_name}/"
           ).failed:
        return False

    # Delete the archive file
    if run(f"rm /tmp/{archive_file}").failed:
        return False

    # Move all the extracted content to our release directory
    if run(f"mv {releases_path}/{archive_name}/web_static/* "
           f"{releases_path}/{archive_name}/").failed:
        return False

    if run(f"rm -rf {releases_path}/{archive_name}/web_static"
           ).failed:
        return False

    # Delete symbolic link
    if run("rm -rf /data/web_static/current").failed:
        return False

    # Create a new the symbolic link
    if run(f"ln -s {releases_path}/{archive_name} /data/web_static/current"
           ).failed:
        return False

    return True
