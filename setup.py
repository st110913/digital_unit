from distutils.core import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
  name = 'digital_unit',         # How you named your package folder (MyLib)
  packages = ['digital_unit'],   # Chose the same as "name"
  version = '1.6.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'number and units',   # Give a short description about your library
  author = 'st201109',                   # Type in your name
  author_email = 'st20110913@outlook.com',      # Type in your E-Mail
  
  keywords = ['SOME', 'MEANINGFULL', 'MATH'],   # Keywords that define your package best
  long_description = long_description,
  long_description_content_type="text/markdown",

  classifiers=[ 
    'Programming Language :: Python :: 3.6',

  ],
)
