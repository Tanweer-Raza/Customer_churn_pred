from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "customer churn"
VERSION = "0.0.1"
AUTHOR = "ineuron"
DESCRIPTION = "This is my first Machine Learning project"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:     
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

    """.remove("-e .") has been used here because already find_packages has bee used here which does the same work."""


setup(
    name = PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()
)

