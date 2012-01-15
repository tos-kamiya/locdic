#coding: utf-8

from distutils.core import setup

def readlines_del1stline_addemptyline(p):
    with open(p) as f:
        return [L.rstrip() for L in f.readlines()][1:] + [""]

setup(
    name='locdic',
    version='0.3.0',
    description="Off-line Dictionary / Dictionary Server Tool",
    long_description='\n'.join(["========", "LocDic", "========", ""] + \
        readlines_del1stline_addemptyline("README.rst") + \
        readlines_del1stline_addemptyline("doc/INSTALLATION") + \
        readlines_del1stline_addemptyline("doc/LICENSE")),
    author="Toshihiro Kamiya",
    author_email="kamiya@mbj.nifty.com",
    url="http://www.remics.org/locdic/",
    requires=[ 
        "PyGtk", 
        "pywebkitgtk" 
    ],
    install_requires=[
        "bottle>=0.9.5",
        # "PyGtk>=2.22", # this line causes try to install PyGtk from source code (and fails).
        # "pywebkitgtk>=1.1.8", # this line, too.
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
            'static/*.css',
            'static/*.js',
            'static/images/*.png',
            'view/*.tpl',
            '../../doc/INSTALLATION',
            '../../doc/LICENSE',
            '../../README.rst',
        ],
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
