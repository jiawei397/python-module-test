from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="jw_test",
      version="1.0.3",
      description="jw module",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="jw",
      author_email="jw397@126.com",
      py_modules=["jw.__init__", "jw.test"])
