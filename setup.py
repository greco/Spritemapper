from setuptools import setup

readme_text = open("README.rst", "U").read()

cli_tools = ["spritemapper = spritecss.main:main"]

setup(name="spritemapper", version="0.5",
      url="http://yostudios.github.com/Spritemapper/",
      author="Yo Studios AB", author_email="opensource@yostudios.se",
      description="A suite for merging multiple images "
                  "and generate corresponding CSS in one go",
      long_description=readme_text,
      license="MIT/X11",
      packages=["spritecss", "spritecss.css", "spritecss.packing"],
      test_suite="nose.collector", tests_require=["nose"],
      entry_points={"console_scripts": cli_tools})
