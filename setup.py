import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystarboard",
    version="0.1",
    author="Maria Silva, Tom Mellan, Kiran Karra",
    author_email="misilva73@gmail.com, t.mellan@imperial.ac.uk, kiran.karra@gmail.com",
    description="A Python package for accessing the Filecoin Starboard API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://github.com/protocol/pystarboard",
        "Source": "https://github.com/protocol/pystarboard",
    },
    packages=["pystarboard"],
    install_requires=["numpy>=1.22", "pandas==1.5.3", "requests>=2.28"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
