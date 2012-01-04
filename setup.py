#coding: utf-8

import glob
import os.path
from distutils.core import setup

def glob_wo_dirs(w):
    return [f for f in glob.glob(w) if not os.path.isdir(f)]

setup(
    name='locdic',
    version='0.1.0',
    description="Off-line Dictionary Tool",
    author="Toshihiro Kamiya",
    author_email="kamiya@mbj.nifty.com",
    url="http://www.remics.org/",
    py_modules=[
        '_config', 'ldfind', 'ldweb',
    ],
    packages=[
        'engine'
    ],
    data_files=[
        ('data', [ 'data/readme', 'data/import_gene.py' ]),
        ('doc', [ 'doc/LICENSE', 'doc/README' ]),
        ('static', glob_wo_dirs('static/*')),
        ('static/images', glob_wo_dirs('static/images/*')),
        ('view', glob_wo_dirs('view/*')),
    ],
    install_requires=[
        "bottle >= 0.10",
    ],
      
    liecense="doc/LICENSE",
    long_description="doc/README",
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
