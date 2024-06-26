from setuptools import setup

APP = ['screenshots.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['os', 'shutil', 'datetime'],  # Add any additional packages your script imports
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)