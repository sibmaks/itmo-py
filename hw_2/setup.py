from setuptools import setup

setup(
    name='latex_table_generator',
    version='1.0',
    packages=['latex_table_generator'],
    entry_points={
        'console_scripts': [
            'generate_latex_table=latex_table_generator:generate_latex_table',
        ],
    },
)
