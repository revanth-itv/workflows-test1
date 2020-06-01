#!/usr/bin/env python

from fabric2 import run 
from fabric import tasks


@task 
def host_type():
    runners('hostname')


'''


import random

from fabric.contrib.files import append, exists 
from fabric.api import cd, env, local, run

REPO_URL= 'https://bitbucket.org/itversity-team/labs-ansible-template.git'


def deploy():
    site_folder = f'/home/admin/sites/192.168.100.220'
    run(f'mkdir -p /home/admin/sampleproject')
    with cd(sampleproject):
        get_latest_code()
        update_venv()
        create_or_update_dotenv()
        update_static_files()
        update_bases()
        

def get_latest_code():
    if exists('.git'):
        run ('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local('git log -n 1 --format=%H', capture=True)
        



VENV = 'djangovenv'
        
def update_venv():
    if not exists ('virtualenv/bin/pip'):
        run(f'python3 -m venv {VENV}')
        
    run('./{}/bin/pip install -r requirements.txt'.format(VENV))
'''    
