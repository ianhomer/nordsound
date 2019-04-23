from setuptools import setup
setup(
    name='nordsound',
    version='0.0.1',
    description='Nord Sound',
    packages=['nordsound'],
    entry_points={
        'console_scripts': [
            'nordview=nordsound.nordview:run',
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose']
)
