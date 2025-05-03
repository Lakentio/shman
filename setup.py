from setuptools import setup, find_packages

setup(
    name="shman",
    version="1.0",
    description="Gerenciador de Shell Scripts",
    author="Lakentio",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "shman=shman.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
