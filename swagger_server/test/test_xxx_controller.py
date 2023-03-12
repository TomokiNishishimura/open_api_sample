# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.xxx import Xxx  # noqa: E501
from swagger_server.test import BaseTestCase


class TestXxxController(BaseTestCase):
    """XxxController integration test stubs"""

    def test_get_xxx(self):
        """Test case for get_xxx

        xxx
        """
        query_string = [('xxx', 'xxx_example')]
        response = self.client.open(
            '/xxx',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_xxx(self):
        """Test case for post_xxx

        xxx
        """
        body = [Xxx()]
        response = self.client.open(
            '/xxx',
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
