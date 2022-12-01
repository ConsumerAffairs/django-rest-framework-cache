from setuptools import setup
from rest_framework_cache import meta


github_url = "https://github.com/ervilis/django-rest-framework-cache/"

setup(
    name="rest-framework-cache",
    version=meta.__version__,
    author=meta.__author__,
    author_email=meta.__email__,
    description="Easy to use cache framework for django-rest-framwork apps",
    license="GPLv3",
    keywords="rest_framework_cache",
    url=github_url,
    packages=['rest_framework_cache', 'tests'],
    namespace_packages=['rest_framework_cache'],
    package_dir={'rest_framework_cache': 'rest_framework_cache'},
    download_url="{}/tarball/master".format(github_url),
    tests_require=["Django", "djangorestframework", "mock"],
    test_suite='tests',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Topic :: Utilities",
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
