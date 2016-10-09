from setuptools import setup

setup(
    name='meninascomp',
    packages=['meninascomp'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'unitest',
    ],
)
