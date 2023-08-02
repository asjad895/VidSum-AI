from distutils.core import setup
from setuptools import setup,find_packages
from typing import List
HYPHEN_E_DOT='-e .'

def get_requirements()->List[str]:
    with open('requirements.txt') as f:
        l=f.readlines()
        l=[r.replace('\n','') for r in l]
        if HYPHEN_E_DOT in l:
            l.remove(HYPHEN_E_DOT)
    return l

setup(name='VidSumAI',
      version='1.0',
      description='This is an Intelligent systems',
      author='Asjad',
      author_email='mdasjad895@gmail.com',
      url='',
      packages=find_packages(),
      install_requires=get_requirements()
    )