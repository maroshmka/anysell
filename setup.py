from setuptools import setup

with open("requirements.txt", "r") as f:
    reqs = f.read().split("\n")

setup(
    name="anysell",
    version="0.0.1",
    py_modules=["main"],
    install_requires=reqs,
    entry_points="""
        [console_scripts]
        anysell=anysell.main:cli
    """,
)
