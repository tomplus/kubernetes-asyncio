# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.12.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1GCEPersistentDiskVolumeSource(object):
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
        'fs_type': 'str',
        'partition': 'int',
        'pd_name': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'partition': 'partition',
        'pd_name': 'pdName',
        'read_only': 'readOnly'
    }

    def __init__(self, fs_type=None, partition=None, pd_name=None, read_only=None):  # noqa: E501
        """V1GCEPersistentDiskVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._fs_type = None
        self._partition = None
        self._pd_name = None
        self._read_only = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        if partition is not None:
            self.partition = partition
        self.pd_name = pd_name
        if read_only is not None:
            self.read_only = read_only

    @property
    def fs_type(self):
        """Gets the fs_type of this V1GCEPersistentDiskVolumeSource.  # noqa: E501

        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :return: The fs_type of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1GCEPersistentDiskVolumeSource.

        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :param fs_type: The fs_type of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def partition(self):
        """Gets the partition of this V1GCEPersistentDiskVolumeSource.  # noqa: E501

        The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :return: The partition of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this V1GCEPersistentDiskVolumeSource.

        The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :param partition: The partition of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :type: int
        """

        self._partition = partition

    @property
    def pd_name(self):
        """Gets the pd_name of this V1GCEPersistentDiskVolumeSource.  # noqa: E501

        Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :return: The pd_name of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._pd_name

    @pd_name.setter
    def pd_name(self, pd_name):
        """Sets the pd_name of this V1GCEPersistentDiskVolumeSource.

        Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :param pd_name: The pd_name of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :type: str
        """
        if pd_name is None:
            raise ValueError("Invalid value for `pd_name`, must not be `None`")  # noqa: E501

        self._pd_name = pd_name

    @property
    def read_only(self):
        """Gets the read_only of this V1GCEPersistentDiskVolumeSource.  # noqa: E501

        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :return: The read_only of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1GCEPersistentDiskVolumeSource.

        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk  # noqa: E501

        :param read_only: The read_only of this V1GCEPersistentDiskVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, V1GCEPersistentDiskVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
