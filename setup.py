from setuptools import setup
setup(
    name = 'cheatle',
    version = '0.0.1',
    packages = ['cheatle'],
    entry_points = {
        'console_scripts': [
            'cheatle = cheatle.__main__:main'
        ]
    })