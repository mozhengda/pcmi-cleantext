from setuptools import setup, find_packages

setup(
    name='autocleaner',
    version='0.1.0',
    description='A domain-aware text cleaner for automotive repair logs using a rewrite table',
    author='Zhengda Mo',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas'
    ],
)