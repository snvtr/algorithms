try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    "description" : "Hoffman decoding",
    "author" : "Alexander A.",
    "url" : "http://example.com/no_url/",
    "download_url" : "http://example.com/no_url/download/",
    "author_email" : "aaa.xxx@gmail.com",
    "version" : "0.0",
    "install_requires" : ["nose"],
    "packages" : ["hoffman"],
    "scripts" : [],
    "name" : "hoffman"
}

setup(**config)
