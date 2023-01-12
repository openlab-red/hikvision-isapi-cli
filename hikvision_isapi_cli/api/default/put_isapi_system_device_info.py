from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_device_info import RootTypeForXMLDeviceInfo
from ...models.root_type_for_xml_response_status import RootTypeForXMLResponseStatus
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: RootTypeForXMLDeviceInfo,
) -> Dict[str, Any]:
    url = "{}/ISAPI/System/deviceInfo".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": xmltodict.unparse(json_json_body),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RootTypeForXMLResponseStatus]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RootTypeForXMLResponseStatus.from_dict(xmltodict.parse(response.text))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RootTypeForXMLResponseStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: RootTypeForXMLDeviceInfo,
) -> Response[RootTypeForXMLResponseStatus]:
    """Set the device information.

    Args:
        json_body (RootTypeForXMLDeviceInfo): XML message about device information Example:
            {'DeviceInfo': {'deviceName': '', 'deviceID': '', 'deviceDescription': '',
            'deviceLocation': '', 'deviceStatus': '', 'DetailAbnormalStatus': {'hardDiskFull': {},
            'hardDiskError': {}, 'ethernetBroken': {}, 'ipaddrConflict': {}, 'illegalAccess': {},
            'recordError': {}, 'raidLogicDiskError': {}, 'spareWorkDeviceError': {}}, 'systemContact':
            '', 'model': '', 'serialNumber': '', 'macAddress': '', 'firmwareVersion': '',
            'firmwareReleasedDate': '', 'bootVersion': '', 'bootReleasedDate': '', 'hardwareVersion':
            '', 'encoderVersion': '', 'encoderReleasedDate': '', 'decoderVersion': '',
            'decoderReleasedDate': '', 'softwareVersion': '', 'capacity': '', 'usedCapacity': '',
            'deviceType': '', 'telecontrolID': '', 'supportBeep': '', 'supportVideoLoss': '',
            'firmwareVersionInfo': '', 'actualFloorNum': '', 'subChannelEnabled': '',
            'thrChannelEnabled': '', 'radarVersion': '', 'cameraModuleVersion': '', 'mainversion': '',
            'subversion': '', 'upgradeversion': '', 'customizeversion': '', 'companyName': '',
            'copyright': '', 'systemName': '', 'systemStatus': '', 'isLeaderDevice': '',
            'clusterVersion': '', 'customizedInfo': '', 'localZoneNum': '', 'alarmOutNum': '',
            'distanceResolution': '', 'angleResolution': '', 'speedResolution': '', 'detectDistance':
            '', 'languageType': '', 'relayNum': '', 'electroLockNum': '', 'RS485Num': '',
            'powerOnMode': '', 'DockStation': {'Platform': {'type': '', 'ip': '', 'port': '',
            'userName': '', 'password': ''}, 'centralStorageBackupEnabled': ''}, 'webVersion': '',
            'deviceRFProgramVersion': '', 'securityModuleSerialNo': '', 'securityModuleVersion': '',
            'securityChipVersion': '', 'securityModuleKeyVersion': '', 'UIDLampRecognition':
            {'enabled': ''}, 'bootTime': '', 'ZigBeeVersion': {'@min': '0', '@max': '16'},
            'R3Version': {'@min': '0', '@max': '16'}, 'RxVersion': {'@min': '0', '@max': '16'},
            'bspVersion': '', 'dspVersion': '', 'localUIVersion': '', 'isResetDeviceLanguage':
            {'@_text': 'false'}, '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: RootTypeForXMLDeviceInfo,
) -> Optional[RootTypeForXMLResponseStatus]:
    """Set the device information.

    Args:
        json_body (RootTypeForXMLDeviceInfo): XML message about device information Example:
            {'DeviceInfo': {'deviceName': '', 'deviceID': '', 'deviceDescription': '',
            'deviceLocation': '', 'deviceStatus': '', 'DetailAbnormalStatus': {'hardDiskFull': {},
            'hardDiskError': {}, 'ethernetBroken': {}, 'ipaddrConflict': {}, 'illegalAccess': {},
            'recordError': {}, 'raidLogicDiskError': {}, 'spareWorkDeviceError': {}}, 'systemContact':
            '', 'model': '', 'serialNumber': '', 'macAddress': '', 'firmwareVersion': '',
            'firmwareReleasedDate': '', 'bootVersion': '', 'bootReleasedDate': '', 'hardwareVersion':
            '', 'encoderVersion': '', 'encoderReleasedDate': '', 'decoderVersion': '',
            'decoderReleasedDate': '', 'softwareVersion': '', 'capacity': '', 'usedCapacity': '',
            'deviceType': '', 'telecontrolID': '', 'supportBeep': '', 'supportVideoLoss': '',
            'firmwareVersionInfo': '', 'actualFloorNum': '', 'subChannelEnabled': '',
            'thrChannelEnabled': '', 'radarVersion': '', 'cameraModuleVersion': '', 'mainversion': '',
            'subversion': '', 'upgradeversion': '', 'customizeversion': '', 'companyName': '',
            'copyright': '', 'systemName': '', 'systemStatus': '', 'isLeaderDevice': '',
            'clusterVersion': '', 'customizedInfo': '', 'localZoneNum': '', 'alarmOutNum': '',
            'distanceResolution': '', 'angleResolution': '', 'speedResolution': '', 'detectDistance':
            '', 'languageType': '', 'relayNum': '', 'electroLockNum': '', 'RS485Num': '',
            'powerOnMode': '', 'DockStation': {'Platform': {'type': '', 'ip': '', 'port': '',
            'userName': '', 'password': ''}, 'centralStorageBackupEnabled': ''}, 'webVersion': '',
            'deviceRFProgramVersion': '', 'securityModuleSerialNo': '', 'securityModuleVersion': '',
            'securityChipVersion': '', 'securityModuleKeyVersion': '', 'UIDLampRecognition':
            {'enabled': ''}, 'bootTime': '', 'ZigBeeVersion': {'@min': '0', '@max': '16'},
            'R3Version': {'@min': '0', '@max': '16'}, 'RxVersion': {'@min': '0', '@max': '16'},
            'bspVersion': '', 'dspVersion': '', 'localUIVersion': '', 'isResetDeviceLanguage':
            {'@_text': 'false'}, '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: RootTypeForXMLDeviceInfo,
) -> Response[RootTypeForXMLResponseStatus]:
    """Set the device information.

    Args:
        json_body (RootTypeForXMLDeviceInfo): XML message about device information Example:
            {'DeviceInfo': {'deviceName': '', 'deviceID': '', 'deviceDescription': '',
            'deviceLocation': '', 'deviceStatus': '', 'DetailAbnormalStatus': {'hardDiskFull': {},
            'hardDiskError': {}, 'ethernetBroken': {}, 'ipaddrConflict': {}, 'illegalAccess': {},
            'recordError': {}, 'raidLogicDiskError': {}, 'spareWorkDeviceError': {}}, 'systemContact':
            '', 'model': '', 'serialNumber': '', 'macAddress': '', 'firmwareVersion': '',
            'firmwareReleasedDate': '', 'bootVersion': '', 'bootReleasedDate': '', 'hardwareVersion':
            '', 'encoderVersion': '', 'encoderReleasedDate': '', 'decoderVersion': '',
            'decoderReleasedDate': '', 'softwareVersion': '', 'capacity': '', 'usedCapacity': '',
            'deviceType': '', 'telecontrolID': '', 'supportBeep': '', 'supportVideoLoss': '',
            'firmwareVersionInfo': '', 'actualFloorNum': '', 'subChannelEnabled': '',
            'thrChannelEnabled': '', 'radarVersion': '', 'cameraModuleVersion': '', 'mainversion': '',
            'subversion': '', 'upgradeversion': '', 'customizeversion': '', 'companyName': '',
            'copyright': '', 'systemName': '', 'systemStatus': '', 'isLeaderDevice': '',
            'clusterVersion': '', 'customizedInfo': '', 'localZoneNum': '', 'alarmOutNum': '',
            'distanceResolution': '', 'angleResolution': '', 'speedResolution': '', 'detectDistance':
            '', 'languageType': '', 'relayNum': '', 'electroLockNum': '', 'RS485Num': '',
            'powerOnMode': '', 'DockStation': {'Platform': {'type': '', 'ip': '', 'port': '',
            'userName': '', 'password': ''}, 'centralStorageBackupEnabled': ''}, 'webVersion': '',
            'deviceRFProgramVersion': '', 'securityModuleSerialNo': '', 'securityModuleVersion': '',
            'securityChipVersion': '', 'securityModuleKeyVersion': '', 'UIDLampRecognition':
            {'enabled': ''}, 'bootTime': '', 'ZigBeeVersion': {'@min': '0', '@max': '16'},
            'R3Version': {'@min': '0', '@max': '16'}, 'RxVersion': {'@min': '0', '@max': '16'},
            'bspVersion': '', 'dspVersion': '', 'localUIVersion': '', 'isResetDeviceLanguage':
            {'@_text': 'false'}, '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: RootTypeForXMLDeviceInfo,
) -> Optional[RootTypeForXMLResponseStatus]:
    """Set the device information.

    Args:
        json_body (RootTypeForXMLDeviceInfo): XML message about device information Example:
            {'DeviceInfo': {'deviceName': '', 'deviceID': '', 'deviceDescription': '',
            'deviceLocation': '', 'deviceStatus': '', 'DetailAbnormalStatus': {'hardDiskFull': {},
            'hardDiskError': {}, 'ethernetBroken': {}, 'ipaddrConflict': {}, 'illegalAccess': {},
            'recordError': {}, 'raidLogicDiskError': {}, 'spareWorkDeviceError': {}}, 'systemContact':
            '', 'model': '', 'serialNumber': '', 'macAddress': '', 'firmwareVersion': '',
            'firmwareReleasedDate': '', 'bootVersion': '', 'bootReleasedDate': '', 'hardwareVersion':
            '', 'encoderVersion': '', 'encoderReleasedDate': '', 'decoderVersion': '',
            'decoderReleasedDate': '', 'softwareVersion': '', 'capacity': '', 'usedCapacity': '',
            'deviceType': '', 'telecontrolID': '', 'supportBeep': '', 'supportVideoLoss': '',
            'firmwareVersionInfo': '', 'actualFloorNum': '', 'subChannelEnabled': '',
            'thrChannelEnabled': '', 'radarVersion': '', 'cameraModuleVersion': '', 'mainversion': '',
            'subversion': '', 'upgradeversion': '', 'customizeversion': '', 'companyName': '',
            'copyright': '', 'systemName': '', 'systemStatus': '', 'isLeaderDevice': '',
            'clusterVersion': '', 'customizedInfo': '', 'localZoneNum': '', 'alarmOutNum': '',
            'distanceResolution': '', 'angleResolution': '', 'speedResolution': '', 'detectDistance':
            '', 'languageType': '', 'relayNum': '', 'electroLockNum': '', 'RS485Num': '',
            'powerOnMode': '', 'DockStation': {'Platform': {'type': '', 'ip': '', 'port': '',
            'userName': '', 'password': ''}, 'centralStorageBackupEnabled': ''}, 'webVersion': '',
            'deviceRFProgramVersion': '', 'securityModuleSerialNo': '', 'securityModuleVersion': '',
            'securityChipVersion': '', 'securityModuleKeyVersion': '', 'UIDLampRecognition':
            {'enabled': ''}, 'bootTime': '', 'ZigBeeVersion': {'@min': '0', '@max': '16'},
            'R3Version': {'@min': '0', '@max': '16'}, 'RxVersion': {'@min': '0', '@max': '16'},
            'bspVersion': '', 'dspVersion': '', 'localUIVersion': '', 'isResetDeviceLanguage':
            {'@_text': 'false'}, '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
