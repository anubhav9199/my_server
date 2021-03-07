import threading

from Lib import as_globals, as_params
from ServiceAPILib import PortfolioAPIManager

def __start_background_threads():
    if as_globals.SERVICE_ENVIRONMENT == as_params.PRODUCTION_ENVIRONMENT:
        if as_globals.server_name == as_params.PORTFOLIO_SERVER_NAME:
            threading.Thread().start()


def initialize(start_threads = False):
    as_globals.portfolio = PortfolioAPIManager.PortfolioAPI

    if not start_threads:
        return

    threading.Thread(target=__start_background_threads).start()