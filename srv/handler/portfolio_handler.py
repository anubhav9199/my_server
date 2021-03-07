import cherrypy

from Lib import common_utils
from Lib import as_params
from Lib import as_globals

from www import wsgi_portfolio

class PortfolioRoot(object):
    def __init__(self, vroot):
        self.vroot = vroot
    
    @cherrypy.expose
    def index(self):
        try:
            return self.__serve_request()
        except Exception as e:
            raise e
