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

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
        
    if local("tar -cvzf {} web_static".format(archive)).failed is True:
        return None
    return archive
