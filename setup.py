#coding: utf-8

import glob
import os.path
from distutils.core import setup

def glob_wo_dirs(w):
    return [f for f in glob.glob(w) if not os.path.isdir(f)]

def target_dir(relp):
    return os.path.join("/usr/local/lib/locdic", relp)

setup(
    name='locdic',
    version='0.1.0',
    description="Off-line Dictionary Tool",
    author="Toshihiro Kamiya",
    author_email="kamiya@mbj.nifty.com",
    url="http://www.remics.org/",
    data_files=[
        (target_dir(''), glob_wo_dirs('*.py')),
        (target_dir('engine'), glob_wo_dirs('engine/*.py')),
        (target_dir('test'), glob_wo_dirs('test/*.py')),
        (target_dir('data'), [ 'data/readme', 'data/import_gene.py' ]),
        (target_dir(''), [ 'LICENSE', 'README' ]),
        (target_dir('static'), glob_wo_dirs('static/*')),
        (target_dir('static/images'), glob_wo_dirs('static/images/*')),
        (target_dir('view'), glob_wo_dirs('view/*')),
    ],
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
