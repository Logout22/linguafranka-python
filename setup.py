from setuptools import setup, find_packages

setup(
    name='dictproxy',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
