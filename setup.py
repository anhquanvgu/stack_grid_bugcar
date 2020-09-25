## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
import setuptools
# fetch values from package.xml
setup_args = generate_distutils_setup(
	package_dir={'': 'src'},
	install_requires=[
	'numpy',
	'imutils',
	'time',
	'cv2'
	]
)
setup(**setup_args)
