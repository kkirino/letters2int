from setuptools import setup

setup(
    name="letters2int",
    version="0.0.1",
    description="convert alphabetical column names in MS Excel to integers",
    license="MIT",
    author="kkirino",
    install_requires=[],
    entry_points={"console_scripts": ["letters2int = letters2int:main"]},
)
