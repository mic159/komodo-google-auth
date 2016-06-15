from setuptools import setup, find_packages

setup(
    name='komodo-google-auth',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask-login==0.3.2',
        'python-social-auth==0.2.14',
        'sqlalchemy==1.0.12',
        'komodo',
    ]
)
