"""Setup script for mtg_ssm."""

import setuptools

# Get version information without importing the package
__version__ = None
with open("pylint_sqlalchemy/_version.py", "rt", encoding="utf-8") as version_file:
    exec(version_file.read())  # pylint: disable=exec-used

SHORT_DESCRIPTION = "pylint plugin to fix incompatibility issues with sqlalchemy"
with open("README.rst", "rt", encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

with open("requirements.txt", "rt", encoding="utf-8") as requirements_file:
    INSTALL_REQUIRES = [line.strip() for line in requirements_file]
with open("test_requirements.txt", "rt", encoding="utf-8") as test_requirements_file:
    TEST_DEPENDENCIES = [line.strip() for line in test_requirements_file]

CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Unix",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
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
