from fabric.api import env, sudo, run, settings
from fabtask.utils import program_exists, is_linux, is_macos

class PackageError(Exception):
    pass

def find_package_management_program():
    if env.get('install_package_command'):
        return
    if is_linux():
        if program_exists('apt-get'):
            env.install_package_command = 'sudo apt-get install -y'
        elif program_exists('yum'):
            env.install_package_command = 'sudo yum -y install'
    elif is_macos():
        ensure_homebrew()
        env.install_package_command = 'brew install'

def ensure_homebrew():
    if not program_exists('brew'):
        run('/usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"')

def ensure_package(name, install_args=""):
    find_package_management_program()
    cmd = '%s %s' % (env.install_package_command, name)
    if install_args:
        cmd += ' ' + install_args
    with settings(warn_only=True):
        result = run(cmd)
        if not result.succeeded and not 'already installed' in result:
            raise PackageError()

def ensure_python_pkg(name):
    if not program_exists('pip'):
        if program_exists('easy_install'):
            sudo('easy_install pip')
        else:
            ensure_package('python-pip')
    sudo('pip install %s' % name)

def ensure_nodejs_pkg(name):
    if not program_exists('npm'):
        ensure_package('nodejs')
    sudo('npm install -g %s' % name)

def ensure_ruby_pkg(name):
    if not program_exists('gem'):
        ensure_package('ruby')
    sudo('gem install %s' % name)
