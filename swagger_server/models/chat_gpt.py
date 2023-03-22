# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ChatGpt(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, role: str=None, content: str=None):  # noqa: E501
        """ChatGpt - a model defined in Swagger

        :param id: The id of this ChatGpt.  # noqa: E501
        :type id: int
        :param role: The role of this ChatGpt.  # noqa: E501
        :type role: str
        :param content: The content of this ChatGpt.  # noqa: E501
        :type content: str
        """
        self.swagger_types = {
            'id': int,
            'role': str,
            'content': str
        }

        self.attribute_map = {
            'id': 'id',
            'role': 'role',
            'content': 'content'
        }
        self._id = id
        self._role = role
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'ChatGpt':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChatGpt of this ChatGpt.  # noqa: E501
        :rtype: ChatGpt
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ChatGpt.


        :return: The id of this ChatGpt.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ChatGpt.


        :param id: The id of this ChatGpt.
        :type id: int
        """

        self._id = id

    @property
    def role(self) -> str:
        """Gets the role of this ChatGpt.


        :return: The role of this ChatGpt.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this ChatGpt.


        :param role: The role of this ChatGpt.
        :type role: str
        """

        self._role = role

    @property
    def content(self) -> str:
        """Gets the content of this ChatGpt.


        :return: The content of this ChatGpt.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this ChatGpt.


        :param content: The content of this ChatGpt.
        :type content: str
        """

        self._content = content