#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""


import os.path as file_path
from datetime import datetime

from fabric.api import local


def do_pack():
    """generates a tgz archive"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_file = "versions/web_static_{}.tgz".format(time)
        if not file_path.exists("versions"):
            local('mkdir -p versions')
        local("tar -cvzf {} web_static".format(archive_file))
        return archive_file
    except FileExistsError:
        return None
