from setuptools import find_packages, setup


setup(
    name="redis-pg",
    install_requires=[
        "dill",
        "redis",
    ],
    packages=find_packages(),
    extras_require={
        "dev": [
            "black",
            "build",
            "cookiecutter-project-upgrader",
            "coverage",
            "ipykernel",
            "ipython",
            "isort",
            "mypy",
            "pytest",
            "ruff",
        ]
    },
)
