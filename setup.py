from setuptools import setup, find_packages

setup(
    name="github-repo-analyzer",
    version="0.1.0",
    description="Find GitHub contribution opportunities",
    author="Open Source Contributor",
    py_modules=["analyzer"],
    entry_points={
        "console_scripts": [
            "gha=analyzer:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
