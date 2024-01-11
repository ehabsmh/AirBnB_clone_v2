#!/usr/bin/python3
"""Generates a .tgz archive"""

from fabric.api import put, run, env
import os

env.hosts = ['54.242.168.59', '52.206.252.73']


def do_deploy(archive_path):
    """Distributes an archive to web servers
    Args:
        archive_path: The path to the archive file

    Returns:
        True, Otherwise - False.
    """

    # Check if file at the path archive_path doesn’t exist
    if not os.path.exists(archive_path):
        return False

    try:
        archive_file = archive_path.split("/")[-1]
        archive_name = archive_file.split(".")[0]
        releases_path = "/data/web_static/releases"

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create the release directory for ex: web_static_20170315003959
        run(f"mkdir -p {releases_path}/{archive_name}/")

        # Uncompress the archive
        run(f"tar -xzf /tmp/{archive_file} -C {releases_path}/{archive_name}/")

        # Delete the archive file
        run(f"rm /tmp/{archive_file}").failed

        # Move all the extracted content to our release directory

        # Remove the web_static directory
        run(f"rm -rf {releases_path}/{archive_name}/web_static")

        # Delete symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link
        run(f"ln -s {releases_path}/{archive_name} /data/web_static/current")

        print("New version deployed!")
        return True
    except BaseException:
        return False
