from setuptools import find_packages, setup

setup(
    name="mlops-demo",
    version="0.1.0",
    description="A demo project for MLOps best practices",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)
