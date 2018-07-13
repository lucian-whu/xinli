from fabric.api import *

# env.hosts = raw_input('enter your host address: ')
# env.user = raw_input('enter  your username: ')
# env.password = raw_input('enter your password: ')

env.hosts = ['119.23.27.37']
env.user = 'root'
env.password = raw_input("please enter your password: ")
def hello():
    print('hello world!')

def deployxinli():
    with cd('/root/xinli'):
        run('git pull')
        sudo('supervisorctl restart xinli')
        sudo('supervisorctl status')

def deployspace():
    with cd('/root/myspace'):
        run('git pull')
        sudo('supervisorctl restart space')
        sudo('supervisorctl status')



