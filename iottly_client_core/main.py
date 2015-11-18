"""

Copyright 2015 Stefano Terna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
"""

BETA AGREEMENT

OurCompany has developed RASPBERRY IOTTLY AGENT including modifications, 
enhancements, improvements, updates, additions, derivative works, 
documentation and related material ("Software"). 
OurCompany desires that the Software be tested prior to general release.

Licensee agrees that Software is the sole property of OurCompany 
until it is officially released and includes valuable trade secrets of 
OurCompany. Licensee agrees to treat Software as confidential and 
will not without the express written authorization of OurCompany: 
- Demonstrate, copy, sell or market Software to any third party; 
- or Publish or otherwise disclose information relating to performance 
  or quality of the Software to any third party; 
- or Modify, reuse, disassemble, decompile, reverse engineer or otherwise 
  translate Software or any portion thereof. 

Software is provided "AS IS" without warranty of any kind. 
The entire risk arising out of the use or performance of Software remains 
with Licensee. In no event shall OurCompany be liable for any damage 
whatsoever arising out of the use of or inability to use Software, 
even if OurCompany has been advised of the possibility of such damages.

"""

__author__ = "Stefano Terna"
__copyright__ = "Copyright 2015, Stefano Terna"
__credits__ = []
__license__ = "BETA AGREEMENT"

__version__ = "0.6"
__maintainer__ = "Stefano Terna"
__email__ = "stefano.terna@tomorrowdata.io"
__status__ = "Prototype"


import json
import logging
import os
import pytz
import time
import tornado
import ujson
import unicodedata
import urllib
import urlparse

from bson import json_util
from datetime import datetime
from tornado import gen, autoreload, httpclient
import tornado.ioloop
import tornado.web
from tornado.httputil import url_concat
from tornado.escape import json_encode
from sockjs.tornado import SockJSRouter, SockJSConnection

from iottly_client_core import settings
from iottly_client_core.util import module_to_dict, extract_request_dict

logging.getLogger().setLevel(logging.DEBUG)

connected_clients = set()

class BaseHandler(tornado.web.RequestHandler):
    pass


class MessagesConnection(SockJSConnection):
    def on_open(self, info):
        connected_clients.add(self)

    def on_close(self):
        connected_clients.remove(self)

class MessageHandler(BaseHandler):
    def initialize(self):
        pass


    @gen.coroutine
    def post(self):
        
        msg = self.get_argument('msg')

        # Immediately return control to the caller
        self.set_status(200)
        self.finish()

        self._broadcast(msg)


    def _broadcast(self, msg):
        for client in connected_clients:
            client.send(msg)




class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')


def shutdown():
    pass

if __name__ == "__main__":
    MessagesRouter = SockJSRouter(MessagesConnection, '/messageChannel')
    app_settings = module_to_dict(settings)
    autoreload.add_reload_hook(shutdown)

    application = tornado.web.Application(
      MessagesRouter.urls +
      [
        (r'/msg', MessageHandler),
        (r'/', MainHandler),
      ], **app_settings)

    application.listen(8521)
    logging.info(" [*] Listening on 0.0.0.0:8521")

    tornado.ioloop.IOLoop.instance().start()
