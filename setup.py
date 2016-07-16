from setuptools import setup

setup(
    name='TownMapServer',
    packages=['townmapserver', 'townmapserver.resources'],
    version='0.0a1',
    description='Server for the backend of the Town Map app.',
    author='James Payne',
    author_email='jepayne1138@gmail.com',
    url='https://github.com/jepayne1138/TownMapServer',
    license='BSD-new',
    download_url='https://github.com/jepayne1138/TownMapServer/tarball/0.0a1',
    keywords='',
    install_requires=[
        'aniso8601==1.1.0',
        'click==6.6',
        'Flask==0.11.1',
        'Flask-RESTful==0.3.5',
        'Flask-SQLAlchemy==2.1',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'MarkupSafe==0.23',
        'psycopg2==2.6.2',
        'python-dateutil==2.5.3',
        'pytz==2016.6.1',
        'six==1.10.0',
        'SQLAlchemy==1.0.14',
        'Werkzeug==0.11.10',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'console_scripts': [
            'server = townmapserver.console:main',
        ],
    }
)
