import connexion
import six

from swagger_server.models.chat_gpt import ChatGpt  # noqa: E501
from swagger_server import util


def post_chat_gpt(body):  # noqa: E501
    """chat_gpt

    # noqa: E501

    :param body: chat_gpt
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [ChatGpt.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
