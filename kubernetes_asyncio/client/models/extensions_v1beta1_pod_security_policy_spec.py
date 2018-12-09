# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class ExtensionsV1beta1PodSecurityPolicySpec(object):
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
        'allow_privilege_escalation': 'bool',
        'allowed_capabilities': 'list[str]',
        'allowed_flex_volumes': 'list[ExtensionsV1beta1AllowedFlexVolume]',
        'allowed_host_paths': 'list[ExtensionsV1beta1AllowedHostPath]',
        'allowed_proc_mount_types': 'list[str]',
        'allowed_unsafe_sysctls': 'list[str]',
        'default_add_capabilities': 'list[str]',
        'default_allow_privilege_escalation': 'bool',
        'forbidden_sysctls': 'list[str]',
        'fs_group': 'ExtensionsV1beta1FSGroupStrategyOptions',
        'host_ipc': 'bool',
        'host_network': 'bool',
        'host_pid': 'bool',
        'host_ports': 'list[ExtensionsV1beta1HostPortRange]',
        'privileged': 'bool',
        'read_only_root_filesystem': 'bool',
        'required_drop_capabilities': 'list[str]',
        'run_as_user': 'ExtensionsV1beta1RunAsUserStrategyOptions',
        'se_linux': 'ExtensionsV1beta1SELinuxStrategyOptions',
        'supplemental_groups': 'ExtensionsV1beta1SupplementalGroupsStrategyOptions',
        'volumes': 'list[str]'
    }

    attribute_map = {
        'allow_privilege_escalation': 'allowPrivilegeEscalation',
        'allowed_capabilities': 'allowedCapabilities',
        'allowed_flex_volumes': 'allowedFlexVolumes',
        'allowed_host_paths': 'allowedHostPaths',
        'allowed_proc_mount_types': 'allowedProcMountTypes',
        'allowed_unsafe_sysctls': 'allowedUnsafeSysctls',
        'default_add_capabilities': 'defaultAddCapabilities',
        'default_allow_privilege_escalation': 'defaultAllowPrivilegeEscalation',
        'forbidden_sysctls': 'forbiddenSysctls',
        'fs_group': 'fsGroup',
        'host_ipc': 'hostIPC',
        'host_network': 'hostNetwork',
        'host_pid': 'hostPID',
        'host_ports': 'hostPorts',
        'privileged': 'privileged',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
        'required_drop_capabilities': 'requiredDropCapabilities',
        'run_as_user': 'runAsUser',
        'se_linux': 'seLinux',
        'supplemental_groups': 'supplementalGroups',
        'volumes': 'volumes'
    }

    def __init__(self, allow_privilege_escalation=None, allowed_capabilities=None, allowed_flex_volumes=None, allowed_host_paths=None, allowed_proc_mount_types=None, allowed_unsafe_sysctls=None, default_add_capabilities=None, default_allow_privilege_escalation=None, forbidden_sysctls=None, fs_group=None, host_ipc=None, host_network=None, host_pid=None, host_ports=None, privileged=None, read_only_root_filesystem=None, required_drop_capabilities=None, run_as_user=None, se_linux=None, supplemental_groups=None, volumes=None):  # noqa: E501
        """ExtensionsV1beta1PodSecurityPolicySpec - a model defined in Swagger"""  # noqa: E501

        self._allow_privilege_escalation = None
        self._allowed_capabilities = None
        self._allowed_flex_volumes = None
        self._allowed_host_paths = None
        self._allowed_proc_mount_types = None
        self._allowed_unsafe_sysctls = None
        self._default_add_capabilities = None
        self._default_allow_privilege_escalation = None
        self._forbidden_sysctls = None
        self._fs_group = None
        self._host_ipc = None
        self._host_network = None
        self._host_pid = None
        self._host_ports = None
        self._privileged = None
        self._read_only_root_filesystem = None
        self._required_drop_capabilities = None
        self._run_as_user = None
        self._se_linux = None
        self._supplemental_groups = None
        self._volumes = None
        self.discriminator = None

        if allow_privilege_escalation is not None:
            self.allow_privilege_escalation = allow_privilege_escalation
        if allowed_capabilities is not None:
            self.allowed_capabilities = allowed_capabilities
        if allowed_flex_volumes is not None:
            self.allowed_flex_volumes = allowed_flex_volumes
        if allowed_host_paths is not None:
            self.allowed_host_paths = allowed_host_paths
        if allowed_proc_mount_types is not None:
            self.allowed_proc_mount_types = allowed_proc_mount_types
        if allowed_unsafe_sysctls is not None:
            self.allowed_unsafe_sysctls = allowed_unsafe_sysctls
        if default_add_capabilities is not None:
            self.default_add_capabilities = default_add_capabilities
        if default_allow_privilege_escalation is not None:
            self.default_allow_privilege_escalation = default_allow_privilege_escalation
        if forbidden_sysctls is not None:
            self.forbidden_sysctls = forbidden_sysctls
        self.fs_group = fs_group
        if host_ipc is not None:
            self.host_ipc = host_ipc
        if host_network is not None:
            self.host_network = host_network
        if host_pid is not None:
            self.host_pid = host_pid
        if host_ports is not None:
            self.host_ports = host_ports
        if privileged is not None:
            self.privileged = privileged
        if read_only_root_filesystem is not None:
            self.read_only_root_filesystem = read_only_root_filesystem
        if required_drop_capabilities is not None:
            self.required_drop_capabilities = required_drop_capabilities
        self.run_as_user = run_as_user
        self.se_linux = se_linux
        self.supplemental_groups = supplemental_groups
        if volumes is not None:
            self.volumes = volumes

    @property
    def allow_privilege_escalation(self):
        """Gets the allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.  # noqa: E501

        :return: The allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: bool
        """
        return self._allow_privilege_escalation

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation):
        """Sets the allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.

        allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.  # noqa: E501

        :param allow_privilege_escalation: The allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: bool
        """

        self._allow_privilege_escalation = allow_privilege_escalation

    @property
    def allowed_capabilities(self):
        """Gets the allowed_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.  # noqa: E501

        :return: The allowed_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_capabilities

    @allowed_capabilities.setter
    def allowed_capabilities(self, allowed_capabilities):
        """Sets the allowed_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.

        allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.  # noqa: E501

        :param allowed_capabilities: The allowed_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[str]
        """

        self._allowed_capabilities = allowed_capabilities

    @property
    def allowed_flex_volumes(self):
        """Gets the allowed_flex_volumes of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the \"volumes\" field.  # noqa: E501

        :return: The allowed_flex_volumes of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[ExtensionsV1beta1AllowedFlexVolume]
        """
        return self._allowed_flex_volumes

    @allowed_flex_volumes.setter
    def allowed_flex_volumes(self, allowed_flex_volumes):
        """Sets the allowed_flex_volumes of this ExtensionsV1beta1PodSecurityPolicySpec.

        allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the \"volumes\" field.  # noqa: E501

        :param allowed_flex_volumes: The allowed_flex_volumes of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[ExtensionsV1beta1AllowedFlexVolume]
        """

        self._allowed_flex_volumes = allowed_flex_volumes

    @property
    def allowed_host_paths(self):
        """Gets the allowed_host_paths of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.  # noqa: E501

        :return: The allowed_host_paths of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[ExtensionsV1beta1AllowedHostPath]
        """
        return self._allowed_host_paths

    @allowed_host_paths.setter
    def allowed_host_paths(self, allowed_host_paths):
        """Sets the allowed_host_paths of this ExtensionsV1beta1PodSecurityPolicySpec.

        allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.  # noqa: E501

        :param allowed_host_paths: The allowed_host_paths of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[ExtensionsV1beta1AllowedHostPath]
        """

        self._allowed_host_paths = allowed_host_paths

    @property
    def allowed_proc_mount_types(self):
        """Gets the allowed_proc_mount_types of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.  # noqa: E501

        :return: The allowed_proc_mount_types of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_proc_mount_types

    @allowed_proc_mount_types.setter
    def allowed_proc_mount_types(self, allowed_proc_mount_types):
        """Sets the allowed_proc_mount_types of this ExtensionsV1beta1PodSecurityPolicySpec.

        AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.  # noqa: E501

        :param allowed_proc_mount_types: The allowed_proc_mount_types of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[str]
        """

        self._allowed_proc_mount_types = allowed_proc_mount_types

    @property
    def allowed_unsafe_sysctls(self):
        """Gets the allowed_unsafe_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.  Examples: e.g. \"foo/*\" allows \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" allows \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :return: The allowed_unsafe_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_unsafe_sysctls

    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(self, allowed_unsafe_sysctls):
        """Sets the allowed_unsafe_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.

        allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.  Examples: e.g. \"foo/*\" allows \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" allows \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :param allowed_unsafe_sysctls: The allowed_unsafe_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[str]
        """

        self._allowed_unsafe_sysctls = allowed_unsafe_sysctls

    @property
    def default_add_capabilities(self):
        """Gets the default_add_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.  # noqa: E501

        :return: The default_add_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_add_capabilities

    @default_add_capabilities.setter
    def default_add_capabilities(self, default_add_capabilities):
        """Sets the default_add_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.

        defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.  # noqa: E501

        :param default_add_capabilities: The default_add_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[str]
        """

        self._default_add_capabilities = default_add_capabilities

    @property
    def default_allow_privilege_escalation(self):
        """Gets the default_allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.  # noqa: E501

        :return: The default_allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: bool
        """
        return self._default_allow_privilege_escalation

    @default_allow_privilege_escalation.setter
    def default_allow_privilege_escalation(self, default_allow_privilege_escalation):
        """Sets the default_allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.

        defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.  # noqa: E501

        :param default_allow_privilege_escalation: The default_allow_privilege_escalation of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: bool
        """

        self._default_allow_privilege_escalation = default_allow_privilege_escalation

    @property
    def forbidden_sysctls(self):
        """Gets the forbidden_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.  Examples: e.g. \"foo/*\" forbids \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" forbids \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :return: The forbidden_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._forbidden_sysctls

    @forbidden_sysctls.setter
    def forbidden_sysctls(self, forbidden_sysctls):
        """Sets the forbidden_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.

        forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.  Examples: e.g. \"foo/*\" forbids \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" forbids \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :param forbidden_sysctls: The forbidden_sysctls of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[str]
        """

        self._forbidden_sysctls = forbidden_sysctls

    @property
    def fs_group(self):
        """Gets the fs_group of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.  # noqa: E501

        :return: The fs_group of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: ExtensionsV1beta1FSGroupStrategyOptions
        """
        return self._fs_group

    @fs_group.setter
    def fs_group(self, fs_group):
        """Sets the fs_group of this ExtensionsV1beta1PodSecurityPolicySpec.

        fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.  # noqa: E501

        :param fs_group: The fs_group of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: ExtensionsV1beta1FSGroupStrategyOptions
        """
        if fs_group is None:
            raise ValueError("Invalid value for `fs_group`, must not be `None`")  # noqa: E501

        self._fs_group = fs_group

    @property
    def host_ipc(self):
        """Gets the host_ipc of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        hostIPC determines if the policy allows the use of HostIPC in the pod spec.  # noqa: E501

        :return: The host_ipc of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """Sets the host_ipc of this ExtensionsV1beta1PodSecurityPolicySpec.

        hostIPC determines if the policy allows the use of HostIPC in the pod spec.  # noqa: E501

        :param host_ipc: The host_ipc of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: bool
        """

        self._host_ipc = host_ipc

    @property
    def host_network(self):
        """Gets the host_network of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.  # noqa: E501

        :return: The host_network of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this ExtensionsV1beta1PodSecurityPolicySpec.

        hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.  # noqa: E501

        :param host_network: The host_network of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: bool
        """

        self._host_network = host_network

    @property
    def host_pid(self):
        """Gets the host_pid of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        hostPID determines if the policy allows the use of HostPID in the pod spec.  # noqa: E501

        :return: The host_pid of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid):
        """Sets the host_pid of this ExtensionsV1beta1PodSecurityPolicySpec.

        hostPID determines if the policy allows the use of HostPID in the pod spec.  # noqa: E501

        :param host_pid: The host_pid of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: bool
        """

        self._host_pid = host_pid

    @property
    def host_ports(self):
        """Gets the host_ports of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        hostPorts determines which host port ranges are allowed to be exposed.  # noqa: E501

        :return: The host_ports of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[ExtensionsV1beta1HostPortRange]
        """
        return self._host_ports

    @host_ports.setter
    def host_ports(self, host_ports):
        """Sets the host_ports of this ExtensionsV1beta1PodSecurityPolicySpec.

        hostPorts determines which host port ranges are allowed to be exposed.  # noqa: E501

        :param host_ports: The host_ports of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[ExtensionsV1beta1HostPortRange]
        """

        self._host_ports = host_ports

    @property
    def privileged(self):
        """Gets the privileged of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        privileged determines if a pod can request to be run as privileged.  # noqa: E501

        :return: The privileged of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this ExtensionsV1beta1PodSecurityPolicySpec.

        privileged determines if a pod can request to be run as privileged.  # noqa: E501

        :param privileged: The privileged of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: bool
        """

        self._privileged = privileged

    @property
    def read_only_root_filesystem(self):
        """Gets the read_only_root_filesystem of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.  # noqa: E501

        :return: The read_only_root_filesystem of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """Sets the read_only_root_filesystem of this ExtensionsV1beta1PodSecurityPolicySpec.

        readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.  # noqa: E501

        :param read_only_root_filesystem: The read_only_root_filesystem of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: bool
        """

        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def required_drop_capabilities(self):
        """Gets the required_drop_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.  # noqa: E501

        :return: The required_drop_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_drop_capabilities

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, required_drop_capabilities):
        """Sets the required_drop_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.

        requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.  # noqa: E501

        :param required_drop_capabilities: The required_drop_capabilities of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[str]
        """

        self._required_drop_capabilities = required_drop_capabilities

    @property
    def run_as_user(self):
        """Gets the run_as_user of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.  # noqa: E501

        :return: The run_as_user of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: ExtensionsV1beta1RunAsUserStrategyOptions
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """Sets the run_as_user of this ExtensionsV1beta1PodSecurityPolicySpec.

        runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.  # noqa: E501

        :param run_as_user: The run_as_user of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: ExtensionsV1beta1RunAsUserStrategyOptions
        """
        if run_as_user is None:
            raise ValueError("Invalid value for `run_as_user`, must not be `None`")  # noqa: E501

        self._run_as_user = run_as_user

    @property
    def se_linux(self):
        """Gets the se_linux of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        seLinux is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :return: The se_linux of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: ExtensionsV1beta1SELinuxStrategyOptions
        """
        return self._se_linux

    @se_linux.setter
    def se_linux(self, se_linux):
        """Sets the se_linux of this ExtensionsV1beta1PodSecurityPolicySpec.

        seLinux is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :param se_linux: The se_linux of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: ExtensionsV1beta1SELinuxStrategyOptions
        """
        if se_linux is None:
            raise ValueError("Invalid value for `se_linux`, must not be `None`")  # noqa: E501

        self._se_linux = se_linux

    @property
    def supplemental_groups(self):
        """Gets the supplemental_groups of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.  # noqa: E501

        :return: The supplemental_groups of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: ExtensionsV1beta1SupplementalGroupsStrategyOptions
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups):
        """Sets the supplemental_groups of this ExtensionsV1beta1PodSecurityPolicySpec.

        supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.  # noqa: E501

        :param supplemental_groups: The supplemental_groups of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: ExtensionsV1beta1SupplementalGroupsStrategyOptions
        """
        if supplemental_groups is None:
            raise ValueError("Invalid value for `supplemental_groups`, must not be `None`")  # noqa: E501

        self._supplemental_groups = supplemental_groups

    @property
    def volumes(self):
        """Gets the volumes of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501

        volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.  # noqa: E501

        :return: The volumes of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ExtensionsV1beta1PodSecurityPolicySpec.

        volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.  # noqa: E501

        :param volumes: The volumes of this ExtensionsV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type: list[str]
        """

        self._volumes = volumes

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
        if not isinstance(other, ExtensionsV1beta1PodSecurityPolicySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
