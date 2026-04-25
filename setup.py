from setuptools import setup, find_packages

setup(
    name="bigcalc",
    version="0.1.0",
    author="Ashwin Jain",
    author_email="ashwinjain825@gmail.com",
    description="Advanced mathematical python library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
)