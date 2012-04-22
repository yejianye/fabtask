from distutils.core import setup

setup(
    name='fabtask',
    version='0.1.0',
    author='Jianye Ye',
    author_email='yejianye@gmail.com',
    packages=['fabtask'],
    url='http://pypi.python.org/pypi/fabtask/',
    license='LICENSE.txt',
    description='Fabric tasks to perform common bootstrap/deployment/package management operations',
    long_description=open('README.txt').read(),
    install_requires=[
        "fabric >= 1.4.0",
    ],
)
