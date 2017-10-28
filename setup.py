from setuptools import setup

setup(
    name='octoscat',
    version='1.0.0',
    description='Search for "hidden treasures" in git repositories.',
    url='https://github.com/quietsec/octoscat',
    author='quietsec',
    author_email='quietsec@lavabit.com',
    license='MIT',
    packages=['octoscat'],
    install_requires=[
        'GitPython==2.1.7',
    ]
)
