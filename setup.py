from setuptools import find_packages, setup


DOT = "-e ."


def get_requirements(file_path: str):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [rq.replace("\n", "") for rq in requirements]

        if DOT in requirements:
            requirements.remove(DOT)

    return requirements


setup(
    name="creditCard",
    version="0.0.1",
    author="Fousseni SAMA",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
