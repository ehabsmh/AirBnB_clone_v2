#!/usr/bin/python3
"""Generates a .tgz archive"""

from fabric.api import put, run, env
import os

env.hosts = ['54.242.168.59', '52.206.252.73']
env.user = 'ubuntu'

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
        arch_name = archive_file.split(".")[0]
        releases_path = "/data/web_static/releases/{}".format(arch_name)
        tmp_arch = "/tmp/{}".format(archive_file)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        
        # Create the release directory for ex: web_static_20170315003959
        run(f"rm -rf {releases_path}/")
        run("mkdir -p {}/".format(releases_path))

        
        # Uncompress the archive
        run("tar -xzf {} -C {}/".format(tmp_arch, releases_path))

        # Delete the archive file
        run("rm {}".format(tmp_arch))

        # Move all the extracted content to our release directory
        run("mv {}/web_static/* {}/".format(releases_path, releases_path))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(releases_path))

        # Delete symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link
        run("ln -s {}/ /data/web_static/current".format(releases_path))
        print("New version deployed!")

        return True
    except BaseException:
        return False
