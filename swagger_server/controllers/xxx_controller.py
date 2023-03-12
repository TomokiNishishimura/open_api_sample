import connexion
import six

from swagger_server.models.xxx import Xxx  # noqa: E501
from swagger_server import util


def get_xxx(xxx):  # noqa: E501
    """xxx

    xxx # noqa: E501

    :param xxx: xxx
    :type xxx: str

    :rtype: None
    """
    return 'do some magic!'


def post_xxx(body):  # noqa: E501
    """xxx

     # noqa: E501

    :param body: xxx
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Xxx.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
