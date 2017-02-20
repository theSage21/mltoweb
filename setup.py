from setuptools import setup
from mltoweb import __version__
__version__ = list(map(str, __version__))
setup(name='mltoweb',
        version='.'.join(__version__),
        description='Quickly make demo pages for ML apps',
        url='http://github.com/theSage21/mltoweb',
        author='Arjoonn Sharma',
        author_email='arjoonn.94@gmail.com',
        license='MIT',
        packages=['mltoweb'],
        zip_safe=False)
