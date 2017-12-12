from setuptools import setup, find_packages

setup(
    name='dinosauron',
    version='0.1.0a1',
    url='https://github.com/allred/dinosauron',
    license='MIT',
    author='Mike Allred',
    author_email='mikejallred@gmail.com',
    description='Network scanner tool',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    zip_safe=False,
    setup_requires=[
        'nose>=1.0',
    ],
    test_suite='nose.collector',
)
