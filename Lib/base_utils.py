import os
import sys

def get_fs_root_path():
    self = sys.modules[__name__]
    return os.path.abspath(self.__file__).rsplit('/', 2)[0]