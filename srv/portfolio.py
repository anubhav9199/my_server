import os
import cherrypy
import request
from genshi.template import TemplateLoader
from Lib import as_params
from Lib import as_globals
from srv.handler import portfolio_handler, root_handler

index_file = os.path.join(os.path.abspath('script'), 'portfolio/index.html')
BASE_URL = '127.0.0.1:8080'

def get_portal_configuration():
    root_handler = root_handler.Root(as_params.PORTFOLIO_VROOT)
    portfoliohtml = os.path.normpath(os.path.join(os.getcwd, '../script/portfolio'))

class Portfolio:
    config = {
        '/': {
            'tools.gzip.on': True,
            'tools.sessions.on': True,
            # 'tools.session_auth.login_screen': root
        }
    }

    @cherrypy.expose
    def index(self):
        response = request.get(BASE_URL + '/get_about_data')
        return open(index_file)


if __name__ == '__main__':

    # config = {
    #     '/': {
    #         'tools.gzip.on': True,
    #         'tools.sessions.on': True,
    #         # 'tools.session_auth.login_screen': root
    #     }
    # }

    cherrypy.tree.mount(Portfolio(), '/', Portfolio.config)

    cherrypy.engine.start()
    cherrypy.engine.block()
