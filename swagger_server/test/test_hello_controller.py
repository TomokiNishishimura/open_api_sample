# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.hello import Hello  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHelloController(BaseTestCase):
    """HelloController integration test stubs"""

    def test_get_hello(self):
        """Test case for get_hello

        Return 'Hello, {your_name}'
        """
        query_string = [('your_name', 'your_name_example')]
        response = self.client.open(
            '/hello',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
