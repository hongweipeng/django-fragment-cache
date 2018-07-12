import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-fragment-cache",
    version="0.5",
    author="hongweipeng",
    author_email="",
    description="add douyin effect to image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hongweipeng/django-fragment-cache",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['setuptools', 'django>=2', ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)