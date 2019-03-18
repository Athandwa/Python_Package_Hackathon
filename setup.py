from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python_Package_Hackathon',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Athandwa/Python_Package_Hackathon',
    author='Lakhiwe Liwani',
    author_email='lakhiweliwani@gmail.com'
)
