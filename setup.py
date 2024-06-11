from setuptools import find_packages, setup
from typing import List 

HYPHEN_E_DOT ="-e ."

def get_requirements(file:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
    


setup(
name="mlproject",
version='0.0.1',
author='Varun',
author_email='varun.252k4@gmail.com',
packages=find_packages(),
#install_requires = ["numpy",'pandas','matplotlib','seaborn']
install_requires = get_requirements('requirement.txt')

)