import setuptools

with open("README.md", "r", encoding='utf8') as f:
    description = f.read()

setuptools.setup(
    name="pocketbase_pyclient",
    version="0.0.1",
    author="kirovj",
    author_email="j-wyt@qq.com",
    keywords=["pocketbase", "client"],
    description=description,
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirovj/pocketbase-pyclient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["httpx"]
)
