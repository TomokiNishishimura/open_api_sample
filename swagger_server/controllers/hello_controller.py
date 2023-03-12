import connexion
import six
import json

from swagger_server.models.hello import Hello  # noqa: E501
from swagger_server import util


def get_hello(your_name):  # noqa: E501
    """Return &#x27;Hello, {your_name}&#x27;

    Return &#x27;Hello, {your_name}&#x27; # noqa: E501

    :param your_name: The name displayed with Hello
    :type your_name: str

    :rtype: Hello
    """
    # return 'do some magic!'
    return json.dumps({
        'result': 'Hello, {}'.format(your_name)
    })
