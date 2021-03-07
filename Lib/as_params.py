import sys
import os

from Lib import base_utils

PRODUCTION_ENVIRONMENT = 0x0001
DEV_LOCAL_ENVIRONMENT = 0x0002

PRODUCTION_ENVIRONMENT_VERBOSE = 'production'
DEV_LOCAL_ENVIRONMENT_VERBOSE = 'local'

PORTFOLIO_SERVER_NAME = 'portfolioPortal'

MASTER_SERVER_CONFIGFILE = ''
PORTFOLIO_VROOT = '/'

CONFIG_ROOT = ''

project_root_path = base_utils.get_fs_root_path()

def load_dynamic_params():
    self = sys.modules[__name__]
    self.MASTER_SERVER_CONFIGFILE = os.path.realpath(os.path.join(CONFIG_ROOT, 'AnubhavMasterServer.cfg'))

load_dynamic_params()
