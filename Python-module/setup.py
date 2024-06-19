from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent

setup(
    name='SpatialDE-SO',
    version='1.1.4',
    description='Spatial and Temporal DE test. This is a fork containing some bug fixes.',
    long_description=(HERE.parent / 'README.rst').read_text(),
    url='https://github.com/Mena-SA-Kamel/SpatialDE-SO',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy', 'scipy >= 1.0', 'pandas>=0.23', 'tqdm',
        'NaiveDE', 'Click',
    ],
    entry_points=dict(
        console_scripts=['spatialde=SpatialDE.scripts.spatialde_cli:main'],
    ),
    author='Valentine Svensson',
    author_email='valentine@nxn.se',
    mantainer='Mena Kamel',
    mantainer_email='mena.kamel@sanofi.com',
    license='MIT',
)
