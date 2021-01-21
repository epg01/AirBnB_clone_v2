#!/usr/bin/python3
# scritp to create source distribution tar archive from web_static folder
from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack content to .gz file"""
    local("sudo mkdir -p versions")
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "versions/web_static{}.tgz".format(date_time)
    local("sudo tar -cvzf {} web_static".format(name_file))
    return name_file
