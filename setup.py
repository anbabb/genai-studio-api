from setuptools import setup, find_packages

setup(
    name="genai_studio",
    version="0.1.0",
    author="Your Name",
    description="API for simplifying technical concepts with GenAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.22.0",
        "pydantic>=1.10.7"
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS"
    ]
)