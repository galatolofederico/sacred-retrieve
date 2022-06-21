import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sacred_retrieve",
    version="0.1.0",
    author="Federico A. Galatolo",
    author_email="galatolo.federico@gmail.com",
    description="Retrieve and process results from sacred mongodb database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        "pymongo==3.7.2",
        "numpy==1.22.0",
        "prettytable==0.7.2",
        "scipy==1.1.0"
    ],
    entry_points = {
        'console_scripts': ['sacred-retrieve=sacred_retrieve.__main__:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta"
    ],
)