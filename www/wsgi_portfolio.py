import cherrypy
import json

from www import wsgi_base


class Portfolio_Handler(wsgi_base.Base_Handler):
    def __init__(self):
        self.router = None

    def get_about_data(self):
        data = as_globals.Portfolio.get_about_data()
        return json.dumps({'status': 0, 'msg': '', 'data': data})


class Portfolio_Wrapper(wsgi_base.Base_Wrapper):
    def __init__(self):
        pass

    @cherrypy.expose
    def get_about_data(self):
        return self.call_method(Portfolio_handler.get_about_data())
