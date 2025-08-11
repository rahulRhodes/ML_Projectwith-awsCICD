from setuptools import find_packages,setup
from typing import List



HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='rahul',
    author_email='rahul9827193441@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)




# setup.py is the build script for your Python project.

# It tells tools like pip and setuptools:

# What your project is called

# What version it is

# Who wrote it

# What dependencies it needs

# What Python packages are included

# How to install it

# It’s especially important if:

# You want to distribute your project (e.g. on PyPI)

# You want to re-use your code as a module

# You want to maintain it like a professional project