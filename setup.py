#coding: utf-8

# This set-up script is a kind of dummy,
# just checks dependencies and tells descriptions.

from distutils.core import setup

import sys

sys.stdout.write('\n%s\n\n' % """
---------------------------------------------------------------------------
Warning: This setup.py really does not install locdic on your PC.
In order to install locdic to your PC, you have to manually copy 
the distribution files and run ldweb.py or ldfind.py. 
---------------------------------------------------------------------------
"""[1:-1])

setup(
    name='locdic',
    version='0.1.0',
    description="Off-line Dictionary Tool",
    author="Toshihiro Kamiya",
    author_email="kamiya@mbj.nifty.com",
    url="http://www.remics.org/",
    requires=[
        "bottle (>=0.10)",
    ],
      
    license="LICENSE",
    long_description="README",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Office/Business",
        "Topic :: Utilities",
    ],
  )
