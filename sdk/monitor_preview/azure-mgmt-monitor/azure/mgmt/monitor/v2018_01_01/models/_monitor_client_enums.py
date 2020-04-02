# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AggregationType(str, Enum):
    """the aggregation type of the metric.
    """

    none = "None"
    average = "Average"
    count = "Count"
    minimum = "Minimum"
    maximum = "Maximum"
    total = "Total"

class Unit(str, Enum):
    """the unit of the metric.
    """

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    count_per_second = "CountPerSecond"
    bytes_per_second = "BytesPerSecond"
    percent = "Percent"
    milli_seconds = "MilliSeconds"
    byte_seconds = "ByteSeconds"
    unspecified = "Unspecified"
    cores = "Cores"
    milli_cores = "MilliCores"
    nano_cores = "NanoCores"
    bits_per_second = "BitsPerSecond"

class ResultType(str, Enum):

    data = "Data"
    metadata = "Metadata"
