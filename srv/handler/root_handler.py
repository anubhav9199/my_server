import json
import sys
import cherrypy
import time
import configparser

from Lib import as_params, as_globals, common_utils

from ServiceAPILib import ServiceAPIManager

def redirect_to_correct_page():
    try:
        host = cherrypy.request.headers['Host']
        if host.find("") != -1:
            raise cherrypy.HTTPRedirect(common_utils.get_redirection_url(as_params.PORTFOLIO_VROOT, ''))
    except Exception as e:
        raise 


class Root(object):
    def __init__(self, vroot):
        self.vroot = vroot

    @classmethod
    def __rebind_service_api(cls):
        ServiceAPIManager.initialize()
        return json.dumps({'status': 0, 'msg': ''}, indent=0)

    @cherrypy.expose
    def rebind_service_api(self):
        return __rebind_service_api()

    @classmethod
    def __reload_config(cls):
        config = configparser.ConfigParser(as_params.MASTER_SERVER_CONFIGFILE)
        config.load()
        as_globals.config = config
        return json.dumps({'status': 0, 'msg': ''}, indent=0)

    @cherrypy.expose
    def reload_config(self):
        return __reload_config()

    @cherrypy.expose
    def index(self, *args, **kwargs):
        redirect_to_correct_page()

    @cherrypy.expose
    def default(self, *args, **kwargs):
        return index(*args, **kwargs)
