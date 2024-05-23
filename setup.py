from setuptools import setup, find_packages

setup(
    name='dir_structure_tool',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gen-dir-structure=dir_structure.main:main',
        ],
    },
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line tool to generate a structured description of a directory.',
    url='https://github.com/yourusername/dir_structure_tool',
    license='MIT',
)
