#coding: utf-8

# This set-up script is a kind of dummy,
# just checks dependencies and tells descriptions.

from distutils.core import setup
import glob
import os

def noext(p): return os.path.splitext(p)[0]

setup(
    name='locdic',
    version='0.1.0',
    description="Off-line Dictionary Tool",
    author="Toshihiro Kamiya",
    author_email="kamiya@mbj.nifty.com",
    url="http://www.remics.org/",
    requires=[
        "bottle (>=0.10)", # LocDic uses a bottle 0.10 feature (url wildcard), which changed from 0.9
        "PyGtk",
        "pywebkitgtk",
    ],
      
    py_modules=[
    ] + map(noext, glob.glob("locdic/*.py") + \
            glob.glob("locdic/engine/*.py") + glob.glob("locdic/test/*.py")),
    data_files=[
        ('locdic/doc', [ 'LICENSE', 'README' ]),
        ('locdic/data', [ "locdic/data/readme", 
                "locdic/data/immport_gene.py", "locdic/data/import_wordnet.py", 
                "locdic/data/wordnet.utf8" ]),
        ('locdic/static', glob.glob('locdic/static/*')),
        ('locdic/static/images', glob.glob('locdic/static/images/*')),
        ('locdic/view', glob.glob('locdic/view/*')),
    ],
      
    license="MIT license / other",
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
