from fabric.api import *

env.hosts = raw_input('enter your host address: ')
env.user = raw_input('enter  your username: ')
env.password = raw_input('enter your password: ')
def hello():
    print('hello world!')

def deploy():
    with cd('/root/xinli'):
        run('git pull')
        sudo('supervisorctl restart xinli')
        sudo('supervisorctl status')
