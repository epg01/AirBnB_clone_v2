#!/usr/bin/python3
# do_deploy of web static content

from fabric.api import *
from os import path

env.hosts = ["35.237.222.244", "34.73.185.36"]
env.user = "ubuntu"


def do_deploy(archive_path):

    if path.exists(archive_path) is False:
        print("pass")
        return False

    try:
        file_ = archive_path.split("/")[1]
        filename = file_.split(".")[0]
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/" + filename)
        run("sudo tar -zxf /tmp/{}.tgz -C {}".format(
            filename, "/data/web_static/releases/" + filename))
        run("sudo rm /tmp/{}".format(file_))
        sudo('mv /data/web_static/releases/{}/web_static/* /data/web_static\
/releases/{}'.format(filename, filename))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(filename))
        print("New version deployed!")
        return True
    except:
        return False
