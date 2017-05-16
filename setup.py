from setuptools import setup, find_packages

setup(
    name='cujo',
    description='Custom Job Ticket Manager',
    install_requires=[
        'django==1.11.1',
        'psycopg2==2.7.1',
        'django-crispy-forms==1.6.1',
    ],
    extras_require={
        'tests': [
            'tox==2.7.0',
            'flake8==3.3.0',
            'coverage==4.4.1',
            'pytest==3.0.7',
            'pytest-django==3.1.2',
        ]
    }
)
