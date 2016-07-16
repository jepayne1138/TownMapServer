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
    install_requires=[''],
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
