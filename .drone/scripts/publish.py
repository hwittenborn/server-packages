#!/usr/bin/python3
import re
import requests
import subprocess

from os import chdir, environ, listdir
from os.path import isfile
from sys import argv

pkgname = argv[1]
proget_api_key = environ["proget_api_key"]

chdir(pkgname)
print(f"INFO: Building '{pkgname}'...")

if subprocess.run(["makedeb", "-s", "--noconfirm"]).returncode != 0:
    print(f"ERROR: Failed to build '{pkgname}'.")
    exit()

debs = [f for f in listdir() if isfile(f) and re.search("\.deb$", f) is not None]

for i in debs:
    with open(i, "rb") as file:
        response = requests.post(f"https://{proget_server}/debian-packages/upload/server-packages/main/{i}",
        data=file,
        auth=HTTPBasicAuth("api", proget_api_key))

    if response.reason != "Created":
        print(f"ERROR: There was an error uploading '{i}': ({response.reason}/{response.text}).")
        exit()

    print(f"INFO: Succesfully uploaded '{i}'.")
