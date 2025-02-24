from setuptools import setup, find_packages

setup(
    name="elon_sort",
    version="0.1.0",
    author="minecrafter8001",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Minecrafter8001/elon_sort",  # Replace with your repo
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
