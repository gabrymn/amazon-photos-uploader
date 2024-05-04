from setuptools import setup

setup (
    name='amazon-photos-uploader-version-control',
    version='0.1',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'amzn-upl = main:main',
        ],
    },
)