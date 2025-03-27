from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'

def get_requirememnts(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(name='MLPROJECTINAI',
      version='0.0.1',
      author='anni',
      author_email='2022ume1815@mnit.ac.in',
      packages=find_packages(),
      install_requires=get_requirememnts('requirements.txt')

)

