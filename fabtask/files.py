from fabric.api import settings, hide, run, cd
from fabric.contrib.files import exists, append, sed

def ensure_link(target, source):
	if exists(target):
		run('rm -rf ' +  target)
	run('ln -sf %s %s' % (source, target))

def ensure_dir(directory):
	if not exists(directory):
		run('mkdir -p ' + directory)

def ensure_file(name, **kwargs):
	'''
		Optional arguments:
		append: append lines to the end of the file if they're not already existed.
	'''
	if not exists(name):
		run('touch %s' % name)
	if kwargs.get('append'):
		lines = kwargs.get('append')	
		if not isinstance(lines, list):
			lines = lines.split('\n')
		append(name, lines)

def ensure_bin_path(paths):
	if not isinstance(paths, list):
		paths = [paths]
	with cd('~'):
		with settings(hide('running', 'warnings', 'stdout'), warn_only=True):
			existing = run("grep '^PATH=' .zshenv")
		if existing.return_code:
			append('.zshenv', 'PATH=%s:$PATH' % ':'.join(paths))
		else:
			existing = existing.split('=')[1].split(':')
			paths = paths + [p for p in existing if p not in paths]
			sed('.zshenv', '^PATH=.*', 'PATH=' + ':'.join(paths), backup='')
