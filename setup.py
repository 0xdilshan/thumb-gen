import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

version_file = here / "thumb_gen" / "version.py"
for line in version_file.read_text().splitlines():
    if line.startswith("__version__"):
        __version__ = line.split("=")[1].strip().strip('"\'')
        break
else:
    raise RuntimeError("Unable to find __version__ in version.py")

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="thumb_gen",
    version=__version__,
    description="Generate video thumbnails for MP4 and MKV files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/thumb-gen",
    project_urls={
        "Bug Tracker": "https://github.com/truethari/thumb-gen/issues",
    },
    keywords="thumbnails video screenshot",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "thumb_gen": ["fonts/*.ttf"],
    },
    install_requires=[
        "Pillow>=11.0.0",
        "infomedia>=1.0.2",
        "opencv-python>=4.13.0",
    ],
    entry_points={
        "console_scripts": [
            "thumb-gen=thumb_gen.__main__:main",
        ],
    },
    python_requires=">=3.9",
)