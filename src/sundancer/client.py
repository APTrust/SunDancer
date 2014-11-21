__author__ = 'swt8w'

import json
from urllib.parse import urlparse
from http.client import HTTPSConnection, HTTPConnection
from urllib.parse import urlencode

from sundancer.conf.settings import API_SUBDIR

class APIException(Exception):
    pass

class APIClient:

    def __init__(self, url, api_key):
        self._set_conn(url)
        self.api_key = api_key
        self.headers = {
            'Authorization': 'Token %s' % self.api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def _set_conn(self, u):
        """
        Sets the connection type and port from the URL provided.
        :param url:
        :return:
        """
        url = urlparse(u)
        if url.scheme == "https":
            conn = HTTPSConnection
        elif url.scheme == "http":
            conn = HTTPConnection
        else:
            raise APIException("Invalid url scheme supplied: %s" % url.scheme)

        self.conn = conn(url.netloc)

    ##*** NODE Methods ***##
    def get_node_list(self, filters=None):

        url = "%s/api-v1/node/" % API_SUBDIR
        if filters:
            url = "%s?%s" % (url, urlencode(filters))
        self.conn.request('GET', url, headers=self.headers)
        rsp = self.conn.getresponse()
        data = rsp.read()
        if rsp.status == 200:
            data = json.loads(data.decode('utf-8'))
            return data
        return None

    ##*** REGISTRY METHODS ***##
    def create_registry_entry(self, reg):
        """
        Does a simple post to create a registry entry.

        :param reg: Dict of registry data to POST
        :return: Dict of return.
        """
        data = json.dumps(reg)
        url = "%s/api-v1/registry/" % API_SUBDIR
        self.conn.request('POST', url, body=data, headers=self.headers)
        rsp = self.conn.getresponse()
        if rsp.status == 201:
            return rsp.read()
        raise APIException("Request returned status: %d" % rsp.status)

    ##*** TRANSFER METHODS ***##
    def create_transfer(self, data):
        """
        Does a simple post to create a transfer.

        :param data: Dict of the transfer data to POST
        :return: Data of return.
        """
        data = json.dumps(data)
        url = "%s/api-v1/transfer/" % API_SUBDIR
        self.conn.request('POST', url, body=data, headers=self.headers)
        rsp = self.conn.getresponse()
        if rsp.status == 201:
            return rsp.read()
        raise APIException("Attempt to create transfer returned status %s" % rsp.status)