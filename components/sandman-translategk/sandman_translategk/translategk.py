
from decaf_utils_components import daemonize
from decaf_utils_components import BasePlugin, In, Out
import decaf_storage
import gkmodule

class TranslateGK(BasePlugin):
	__version__ = "0.1-dev01"

	def __init__(self, logger=None, config=None):
		super(TranslateGK, self).__init__(logger=logger, config=config)
		gkmodule.startServer()

	def _before_connect(self,url=None,rpc=None,routing_key=None):
		pass

	def _after_connect(self):
		self.s = decaf_storage.Endpoint(self.rpc, self.logger)

	def dispose(self):
		gkmodule.stopServer()

def daemon():
    daemonize(TranslateGK)

if __name__ == "__main__":
    daemon()
