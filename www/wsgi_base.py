# import error
import cherrypy
import json

class Base_Handler(object):
    def __init__(self):
        self.router = None

class Base_Wrapper(object):
    def __init__(self, router):
        self.router = router
        self.handler_name = 'base'
        self.handler = None
        self.format_response = True

    # def handle_fault(self, fault):
    #     if not self.format_response:
    #         raise fault

    #     if isinstance(fault, error.Fault):
    #         return {'status': -1, 'msg': str(fault), 'errCode': fault.errno}
    #     elif isinstance(fault, cherrypy.HTTPError):
    #         raise fault
    #     else:
    #         original_error = ''
    #         if as_globals.SERVICE_ENVIRONMENT != as_params.PRODUCTION_ENVIRONMENT:
    #             original_error = str(fault)
    #         return {
    #             'status': -1,
    #             'msg': "Unable to process your request at the moment! Please try again.",
    #             'errCode': error.errCode,
    #             'oer': original_error
    #         }

    def handle_access_denied(self):
        if self.format_response:
            return {'status': -1, 'msg': "Access denied.", 'errCode': error.errCode}
        raise

    def _call_method(self, handler_method, *args, **kwargs):  # pylint: disable=too-many-statements
        api_to_call = self.handler_name + '/' + handler_method.im_func.func_name

        if cherrypy.session.get('disabled', False):
            self.handle_access_denied()

        # Check if API access is allowed when logged-in entity is not verified yet.
        verified = cherrypy.session.get('verified', True)
        if self.handler_name != 'config' and not verified:
            self.handle_access_denied()

        # try:
        if as_globals.SERVICE_ENVIRONMENT != as_params.PRODUCTION_ENVIRONMENT:
            api_to_call = self.handler_name + '/' + handler_method.im_func.func_name
            try:
                _params = cherrypy.request.json
            except Exception, fault:
                _params = kwargs

        result = handler_method(*args, **kwargs)
        return result
        # except Exception, fault:
        #     if not _format_response:
        #         raise

        #     return self.handle_fault(fault)

    def call_method(self, handler_method, *args, **kwargs):
        return_data = self._call_method(handler_method, *args, **kwargs)

        if self.format_response:
            return json.dumps(return_data)

        return return_data.get('data', {})
