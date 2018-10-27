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


class V1LoadBalancerIngress(object):
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
        'hostname': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'ip': 'ip'
    }

    def __init__(self, hostname=None, ip=None):  # noqa: E501
        """V1LoadBalancerIngress - a model defined in Swagger"""  # noqa: E501

        self._hostname = None
        self._ip = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if ip is not None:
            self.ip = ip

    @property
    def hostname(self):
        """Gets the hostname of this V1LoadBalancerIngress.  # noqa: E501

        Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)  # noqa: E501

        :return: The hostname of this V1LoadBalancerIngress.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this V1LoadBalancerIngress.

        Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)  # noqa: E501

        :param hostname: The hostname of this V1LoadBalancerIngress.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def ip(self):
        """Gets the ip of this V1LoadBalancerIngress.  # noqa: E501

        IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)  # noqa: E501

        :return: The ip of this V1LoadBalancerIngress.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this V1LoadBalancerIngress.

        IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)  # noqa: E501

        :param ip: The ip of this V1LoadBalancerIngress.  # noqa: E501
        :type: str
        """

        self._ip = ip

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
        if not isinstance(other, V1LoadBalancerIngress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
