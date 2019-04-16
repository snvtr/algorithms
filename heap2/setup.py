try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    "description" : "Binary heap implementation",
    "author" : "Alexander A.",
    "url" : "http://example.com/no_url/",
    "download_url" : "http://example.com/no_url/download/",
    "author_email" : "aaa.bbb@gmail.com",
    "version" : "0.0",
    "install_requires" : ["nose"],
    "packages" : ["heap2"],
    "scripts" : [],
    "name" : "heap2"
}

setup(**config)
