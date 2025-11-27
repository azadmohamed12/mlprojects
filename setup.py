from setuptools import find_packages
from setuptools import setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    """
    This function reads the requirements.txt file and returns a list of requirements.
    """
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.01",
    author="Asad astro",
    author_email="asadastro2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
