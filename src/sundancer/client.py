__author__ = 'swt8w'

import json
from http.client import HTTPSConnection
from urllib.parse import urlencode

class APIClient:

    def __init__(self, api_url, api_key):
        self.api_key = api_key
        self.url = api_url
        self.headers = {
            'Authorization': 'Token %s' % self.api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_nodes(self, filters=None):

        h = HTTPSConnection(self.url, 443)
        url = "/dpnode/api-v1/node/"
        if filters:
            url = "%s?%s" % (url, urlencode(filters))
        h.request('GET', url, headers=self.headers)
        rsp = h.getresponse()
        data = json.loads(rsp.read().decode('utf-8'))
        return data