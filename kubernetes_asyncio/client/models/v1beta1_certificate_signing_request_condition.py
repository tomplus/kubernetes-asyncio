# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.11.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1beta1CertificateSigningRequestCondition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'last_update_time': 'datetime',
        'message': 'str',
        'reason': 'str',
        'type': 'str'
    }

    attribute_map = {
        'last_update_time': 'lastUpdateTime',
        'message': 'message',
        'reason': 'reason',
        'type': 'type'
    }

    def __init__(self, last_update_time=None, message=None, reason=None, type=None):  # noqa: E501
        """V1beta1CertificateSigningRequestCondition - a model defined in Swagger"""  # noqa: E501

        self._last_update_time = None
        self._message = None
        self._reason = None
        self._type = None
        self.discriminator = None

        if last_update_time is not None:
            self.last_update_time = last_update_time
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        self.type = type

    @property
    def last_update_time(self):
        """Gets the last_update_time of this V1beta1CertificateSigningRequestCondition.  # noqa: E501

        timestamp for the last update to this condition  # noqa: E501

        :return: The last_update_time of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this V1beta1CertificateSigningRequestCondition.

        timestamp for the last update to this condition  # noqa: E501

        :param last_update_time: The last_update_time of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :type: datetime
        """

        self._last_update_time = last_update_time

    @property
    def message(self):
        """Gets the message of this V1beta1CertificateSigningRequestCondition.  # noqa: E501

        human readable message with details about the request state  # noqa: E501

        :return: The message of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1beta1CertificateSigningRequestCondition.

        human readable message with details about the request state  # noqa: E501

        :param message: The message of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this V1beta1CertificateSigningRequestCondition.  # noqa: E501

        brief reason for the request state  # noqa: E501

        :return: The reason of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1beta1CertificateSigningRequestCondition.

        brief reason for the request state  # noqa: E501

        :param reason: The reason of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def type(self):
        """Gets the type of this V1beta1CertificateSigningRequestCondition.  # noqa: E501

        request approval state, currently Approved or Denied.  # noqa: E501

        :return: The type of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1beta1CertificateSigningRequestCondition.

        request approval state, currently Approved or Denied.  # noqa: E501

        :param type: The type of this V1beta1CertificateSigningRequestCondition.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1CertificateSigningRequestCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
