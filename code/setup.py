#Author:: Rohit Bhal

from distutils.core import setup
import py2exe
import os
import glob

def find_data_files(source,target,patterns):
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source,pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target,os.path.relpath(filename,source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path,[]).append(filename)
    return sorted(ret.items())
 
setup(
    windows=['mario_level_1.py'],
    zipfile = None,
    data_files=find_data_files('resources','resources',[
           'fonts/*',
           'graphics/*',
           'music/*',
           'sound/*',
       ]),
    options={
          "py2exe": {
              "optimize": 1,
              'compressed': True,
              "excludes": ['Carbon', 'Carbon.Files', 'OpenGL.GL', '_scproxy', '_sysconfigdata', 'importlib._bootstrap', 'numpy', 'packaging.specifiers', 'packaging.version', 'pygame._view', 'pygame.movie', 'urllib.parse', 'pygame.SRCALPHA', 'pygame.sdlmain_osx'],
              }
          }
      )
