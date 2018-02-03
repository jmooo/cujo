from setuptools import setup, find_packages

setup(
    name='cujo',
    description='Custom Job Ticket Manager',
    install_requires=[
        'django==2.0.2',
        'psycopg2==2.7.3.2',
        'django-crispy-forms==1.7.0',
    ],
    extras_require={
        'tests': [
            'tox==2.9.1',
            'flake8==3.5.0',
            'coverage==4.4.2',
            'pytest==3.4.0',
            'pytest-django==3.1.2',
        ]
    }
)
