#!/usr/bin/python3
# Full deploy create file tat to distribution send to server and
# uncompress the file to get the static content

from fabric.api import env, sudo, local, run, put
from datetime import datetime
from os import path
env.hosts = ["35.227.116.106", "34.74.163.244"]
env.user = "ubuntu"


def do_pack():
    """ pack content files to .gz file"""
    local("sudo mkdir -p versions")
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "versions/web_static{}.tgz".format(date_time)
    local("sudo tar -cvzf {} web_static".format(name_file))
    return name_file


def do_deploy(archive_path):
    """ Deploy the .gz file to a host servers"""
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
        run('sudo mv /data/web_static/releases/{}/web_static/* /data/web_static\
/releases/{}'.format(filename, filename))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(filename))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ run the script to pack .gz file and deploy it """
    archive_path = do_pack()
    if archive_path is None:
        print("pass")
        return False
    return do_deploy(archive_path)
