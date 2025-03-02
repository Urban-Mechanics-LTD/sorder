from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sorder",
    version="0.1.0",
    author="Author",
    author_email="author@example.com",
    description="A brief description of the sorder package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/sorder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add your package dependencies here
        # For example: "requests>=2.25.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black",
            "isort",
            "mypy",
        ],
    },
)

