# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.chat_gpt import ChatGpt  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChatGptController(BaseTestCase):
    """ChatGptController integration test stubs"""

    def test_post_chat_gpt(self):
        """Test case for post_chat_gpt

        chat_gpt
        """
        body = [ChatGpt()]
        response = self.client.open(
            '/chat_gpt',
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
