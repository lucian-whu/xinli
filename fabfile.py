from fabric.api import *

env.hosts = ['119.23.27.37']
env.user = 'root'
env.password = input('enter your password: ')
def hello():
    print('hello world!')

def deploy():
    with cd('/home/shin/Todo'):
        run('git pull')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')
