#!/usr/bin/python3
"""Generates a .tgz archive"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generates a .tgz archive from the contents of the web_static\
     folder of your AirBnB Clone repo"""
    yr = datetime.utcnow().year
    mth = datetime.utcnow().month
    day = datetime.utcnow().day
    hr = datetime.utcnow().hour
    mins = datetime.utcnow().min
    secs = datetime.utcnow().second

    directory = "versions"

    archive = f"{directory}/web_static_{yr}{mth}{day}{hr}{mins}{secs}.tgz"

    if not os.path.isdir(directory):
        if local(f"mkdir {directory}").failed:
            return None

    if local(f"tar -czvf {archive} web_static").failed:
        return None

    return archive
