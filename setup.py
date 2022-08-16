from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="lark-bitable-sdk",
    version="0.0.0.3",
    description="A python-made lark bitable sdk.",
    author="Tianhao Zhang",
    author_email="genji9071@gmail.com",
    license="MIT",
    keywords="lark bitable",
    project_urls={
        "Source": "https://github.com/genji9071/lark-bitable-sdk",
        "Tracker": "https://github.com/genji9071/lark-bitable-sdk/issues"
    },
    packages=find_packages(),
    install_requires=["pydantic==1.8.2", "requests==2.28.1"],
    python_requires=">=3",
    long_description=long_description,
    long_description_content_type='text/markdown'
)