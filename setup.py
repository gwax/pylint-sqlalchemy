"""Setup script for mtg_ssm."""

import setuptools

# Get version information without importing the package
__version__ = None
exec(open("pylint_sqlalchemy/_version.py", "r").read())  # pylint: disable=exec-used

SHORT_DESCRIPTION = "pylint plugin to fix incompatibility issues with sqlalchemy"
LONG_DESCRIPTION = open("README.rst", "r").read()

INSTALL_REQUIRES = [l.strip() for l in open("requirements.txt", "r")]
TEST_DEPENDENCIES = [l.strip() for l in open("test_requirements.txt", "r")]

CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Unix",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Quality Assurance",
]

setuptools.setup(
    name="pylint-sqlalchemy",
    version=__version__,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="George Leslie-Waksman",
    author_email="waksman@gmail.com",
    url="https://github.com/gwax/pylint-sqlalchemy",
    packages=setuptools.find_packages(exclude=("tests*",)),
    license="MIT",
    platforms=["any"],
    keywords=["pylint", "sqlalchemy", "plugin"],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_DEPENDENCIES,
)
