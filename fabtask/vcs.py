from fabric.contrib.files import exists
from fabric.api import run, cd
from fabtask.packages import ensure_package
from fabtask.utils import program_exists

def ensure_git_repo(path, url, pushurl=None, submodules=False):
	if not exists(path):
		if not program_exists('git'):
			ensure_package('git')
		run('git clone %s %s' % (url, path))
		if pushurl:
			with(cd(path)):
				run('git config remote.origin.pushurl %s' % pushurl)
		if submodules:
			with(cd(path)):
				run('git submodule init')
				run('git submodule update')
