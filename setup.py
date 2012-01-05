#coding: utf-8

# This set-up script is a kind of dummy,
# just checks dependencies and tells descriptions.

from distutils.core import setup
import glob
import os

def glob_wo_dir(p):
    return [f for f in glob.glob(p) if not os.path.isdir(f)]

setup(
    name='locdic',
    version='0.1.0',
    description="Off-line Dictionary / Dictionary Server Tool",
    author="Toshihiro Kamiya",
    author_email="kamiya@mbj.nifty.com",
    url="http://www.remics.org/locdic/",
    requires=[
        "bottle (>=0.10)", # LocDic uses a bottle 0.10 feature (url wildcard), which changed from 0.9
        "PyGtk",
        "pywebkitgtk",
    ],
    
    data_files=[
        ('bin', [ 'bin/ldfind', 'bin/ldweb' ]),
        ('bin/locdic', glob.glob("bin/locdic/*.py")),
        ('bin/locdic/engine', glob.glob("bin/locdic/engine/*.py")),
        ('bin/locdic/test', glob.glob("bin/locdic/test/*.py")),
        ('bin/locdic/doc', [ 'bin/locdic/doc/LICENSE', 'bin/locdic/doc/README', 
                'bin/locdic/doc/INSTALLATION' ]),
        ('bin/locdic/data', [ "bin/locdic/data/readme", 
                "bin/locdic/data/import_gene.py", "bin/locdic/data/import_wordnet.py", 
                "bin/locdic/data/wordnet.utf8" ]),
        ('bin/locdic/static', glob_wo_dir('bin/locdic/static/*')),
        ('bin/locdic/static/images', glob_wo_dir('bin/locdic/static/images/*')),
        ('bin/locdic/view', glob_wo_dir('bin/locdic/view/*')),
    ],
      
    license="MIT license / BSD license",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Office/Business",
        "Topic :: Utilities",
    ],
  )
