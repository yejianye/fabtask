from fabric.api import env, settings, run, hide

def osname():
	if not env.get('osname'):
		with hide('running', 'stdout'):
			env.osname = run('uname')
	return env.osname

def is_macos():
	return osname() == 'Darwin'

def is_linux():
	return osname() == 'Linux'

def program_exists(name):
	with settings(hide('warnings', 'running', 'stdout', 'stderr'), warn_only=True):
		result = run('which ' + name)
	return False if result.return_code else True

