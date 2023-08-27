from setuptools import setup, find_packages
from typing import List


PROJECT_NAME="ML Project"
VERSION = "0.0.1"
DESCRIPTION = "Python ML Project (Modular coding)"
AUTHOR_NAME = "Nnamdi Daniel Aghanya"
AUTHOR_EMAIL = "daniel2468114@gmail.com"
PORTFOLIO_URL = "http://"
REQUIREMENTS_FILE_LIST = "requirements.txt"

HYPHEN_E_DOT = "-e ."
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_LIST) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement.replace("\n", "") for requirement in requirements_list]

    if HYPHEN_E_DOT in requirements_list:
        requirements_list.remove(HYPHEN_E_DOT)
    
    return requirements_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      url=PORTFOLIO_URL,
      packages=find_packages(),
      install_requires=get_requirements_list()
)