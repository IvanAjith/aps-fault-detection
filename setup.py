from setuptools import find_packages, setup
from typing import List

requirement_file_name = 'requirements.txt'

def get_requirements()->List(str):
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace('/n', '') for requirement_name in requirement_list]
    
    if HYPEN_E_DOT in requirement_list:
        requirement_list.remove(HYPEN_E_DOT)
     return requirement_list   

setup (
    nme = 'sensor',
    version = '0.0.1',
    author = 'ajithkhan',
    author_email= 'ajithkhan619@gmail.com'
    packages = find_packages(),
    install_requires = get_requirements()
)