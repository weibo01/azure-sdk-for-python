# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GenerateArmTemplateRequest(Model):
    """Parameters for generating an ARM template for deploying artifacts.

    :param virtual_machine_name: The resource name of the virtual machine.
    :type virtual_machine_name: str
    :param parameters: The parameters of the ARM template.
    :type parameters: list[~azure.mgmt.devtestlabs.models.ParameterInfo]
    :param location: The location of the virtual machine.
    :type location: str
    :param file_upload_options: Options for uploading the files for the
     artifact. UploadFilesAndGenerateSasTokens is the default value. Possible
     values include: 'UploadFilesAndGenerateSasTokens', 'None'
    :type file_upload_options: str or
     ~azure.mgmt.devtestlabs.models.FileUploadOptions
    """

    _attribute_map = {
        'virtual_machine_name': {'key': 'virtualMachineName', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[ParameterInfo]'},
        'location': {'key': 'location', 'type': 'str'},
        'file_upload_options': {'key': 'fileUploadOptions', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GenerateArmTemplateRequest, self).__init__(**kwargs)
        self.virtual_machine_name = kwargs.get('virtual_machine_name', None)
        self.parameters = kwargs.get('parameters', None)
        self.location = kwargs.get('location', None)
        self.file_upload_options = kwargs.get('file_upload_options', None)