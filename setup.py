import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cadence-python",
    version="0.0.1rc1",
    author="Jia Xuyang",
    author_email="xuyang.jia@gmail.com",
    description="Python client for uber/cadence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiaxuyang/cadence-python",
    packages=setuptools.find_packages(exclude=["cadence.tests", "cadence.spikes"]),
    install_requires=[
        "dataclasses-json>=0.3.8",
        "more-itertools>=7.0.0",
        "ply>=3.11",
        "six>=1.12.0",
        "tblib>=1.6.0",
        "thriftrw>=1.7.2",
        'contextvars;python_version<"3.7"',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
