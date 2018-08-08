# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.11.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class V1SelfSubjectAccessReviewSpec(object):
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
        'non_resource_attributes': 'V1NonResourceAttributes',
        'resource_attributes': 'V1ResourceAttributes'
    }

    attribute_map = {
        'non_resource_attributes': 'nonResourceAttributes',
        'resource_attributes': 'resourceAttributes'
    }

    def __init__(self, non_resource_attributes=None, resource_attributes=None):  # noqa: E501
        """V1SelfSubjectAccessReviewSpec - a model defined in Swagger"""  # noqa: E501

        self._non_resource_attributes = None
        self._resource_attributes = None
        self.discriminator = None

        if non_resource_attributes is not None:
            self.non_resource_attributes = non_resource_attributes
        if resource_attributes is not None:
            self.resource_attributes = resource_attributes

    @property
    def non_resource_attributes(self):
        """Gets the non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501

        NonResourceAttributes describes information for a non-resource access request  # noqa: E501

        :return: The non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1NonResourceAttributes
        """
        return self._non_resource_attributes

    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes):
        """Sets the non_resource_attributes of this V1SelfSubjectAccessReviewSpec.

        NonResourceAttributes describes information for a non-resource access request  # noqa: E501

        :param non_resource_attributes: The non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type: V1NonResourceAttributes
        """

        self._non_resource_attributes = non_resource_attributes

    @property
    def resource_attributes(self):
        """Gets the resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501

        ResourceAuthorizationAttributes describes information for a resource access request  # noqa: E501

        :return: The resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1ResourceAttributes
        """
        return self._resource_attributes

    @resource_attributes.setter
    def resource_attributes(self, resource_attributes):
        """Sets the resource_attributes of this V1SelfSubjectAccessReviewSpec.

        ResourceAuthorizationAttributes describes information for a resource access request  # noqa: E501

        :param resource_attributes: The resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type: V1ResourceAttributes
        """

        self._resource_attributes = resource_attributes

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
        if not isinstance(other, V1SelfSubjectAccessReviewSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
