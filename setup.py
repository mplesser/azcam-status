from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="azcam-status",
    version="21.1.3",
    description="azcam browser-based status page",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Michael Lesser",
    author_email="mlesser@arizona.edu",
    keywords="ccd imaging astronomy observation observatory",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["azcam", "flask"],
    include_package_data=True,
)
