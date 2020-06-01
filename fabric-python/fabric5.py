import random

from fabric.contrib.files import append, exists 
from fabric.api import cd, env, local, run

from fabric.contrib

REPO_URL= 'https://bitbucket.org/itversity-team/labs-ansible-template.git'


def deploy():
    site_folder = f'/home/vagrant/'
    run(f'sudo su - itvadmin')
    with run(ls):
        get_latest_code()
#        update_venv()
#        create_or_update_dotenv()
        update_static_files()
        update_databases()
        restart_django()

def get_latest_code():
    run(f'git pull origin master')
    
'''    
    if exists('.git'):
        run ('git fetch')
    else:
        run(f'git clone {} .'.format(REPO_URL))
    current_commit = local('git log -n 1 --format=%H', capture=True)
'''        

'''

VENV = 'venv'
        
def update_venv():
    if not exists ('venv/bin/pip'):
        run(f'python3 -m venv {}'.format(VENV))
        
    run(f'./{}/bin/pip install -r requirements.txt'.format(VENV))

'''


def update_static_files():
    run(f'./venv/bin/python manage.py collectstatic --noinput')
    
    
    
def update_databases():
    run(f'./venv/bin/python manage.py migrate --noinput')
    
    
def restart_django():
    run (f'exit')
    run(f'sudo service restart')