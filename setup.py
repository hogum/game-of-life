import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="game-of-life-MUGOH",
    version="0.0.1",
    author="mugoh",
    author_email="mugo.ks@gmail.com",
    description="Conway's game of life in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hogum/game-of-life",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
