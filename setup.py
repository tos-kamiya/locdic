#coding: utf-8

from distutils.core import setup
import glob
import os

def glob_wo_dir(p):
    return [f for f in glob.glob(p) if not os.path.isdir(f)]

setup(
    name='locdic',
    version='0.2.1',
    description="Off-line Dictionary / Dictionary Server Tool",
    long_description=open("src/locdic/doc/README").read(),
    author="Toshihiro Kamiya",
    author_email="kamiya@mbj.nifty.com",
    url="http://www.remics.org/locdic/",
    requires=[
        "bottle",
        "PyGtk",
        "pywebkitgtk",
    ],
      
    packages=[
        'locdic', 
        'locdic.engine',
    ],
    package_dir={
        'locdic': 'src/locdic',
        'locdic.engine': 'src/locdic/engine',
    },
    package_data={'locdic': 
        [
            'data/import_gene.py', 
            'data/import_wordnet.py',
            'data/readme',
            'data/wordnet.utf8',
            'doc/INSTALLATION',
            'doc/LICENSE',
            'doc/README',
            'static/*.css',
            'static/*.js',
            'static/images/*.png',
            'view/*.tpl',
        ]
    },
    
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
