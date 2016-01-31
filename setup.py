
import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='tatoeba2',
    version='0.1.0',
    description="Django orm models for Tatoeba's database.",
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Framework :: Django',
        ],
    author='loolmeh',
    url='http://github.com/Tatoeba/dj-tatoeba2',
    license='MIT',
    py_modules=['tatoeba2'],
    )
