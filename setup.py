import pathlib
from setuptools import find_packages, setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
    name="word-scramble",
    version="1.0.0",
    description="Python 3+ version scrabble word finder! Super efficient with hashtables!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Harvard90873/word-scramble",
    author="Harvard90873",
    author_email="harvard90873@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(exclude=("tests", "build")),
    include_package_data=False,
    install_requires=["python-algorithms-3x", "termcolor", "and-or-not", "data-structures3x", "spell-checker"],
)