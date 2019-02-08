import setuptools

# copies README into `long_description`
with open('README.md', 'r') as readme:
    long_description = readme.read()


setuptools.setup(

    # general metadata
    name="plogs",
    version="0.1.1",
    author="Doug Rudolph",
    author_email="drudolph914@gmail.com",

    # shorthand description
    description="Bring color and formatting to your logs",

    # copies the README.md into `long_description` and notes that it is a markdown file
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Github URL
    url="https://github.com/11/plogs",

    # takes note that the python modules are contained in the source folder
    package_dir={"": "src:"},

    # setuptools will find the python packages for us
    packages=["src"],

    # specify what version of python plogs is targeting
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
