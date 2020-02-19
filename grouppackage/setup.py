from setuptools import setup, find_packages

setup(
    name='grouppackage',
    version='1',
    packages=find_packages(exclude=['test_func*']),
    license='MIT',
    description='EDSA Predict python package',
    long_description=open('README.md').read(),
<<<<<<< HEAD
    install_requires=['numpy', 'pandas', 'datetime', 'unittest'],
    url='https://github.com/Confidono/Team-14-Predict',
=======
    install_requires=['numpy', 'pandas'],
    url='https://github.com/Confidono/Team-14-Predict.git',
>>>>>>> 612e2ced52d41cf5689e2d2969d92c07e6d2c583
    author='Team 14',
    author_email='thekwena011@gmail.com'
)