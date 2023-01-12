from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_device_info_device_info import RootTypeForXMLDeviceInfoDeviceInfo


T = TypeVar("T", bound="RootTypeForXMLDeviceInfo")


@attr.s(auto_attribs=True)
class RootTypeForXMLDeviceInfo:
    """XML message about device information

    Example:
        {'DeviceInfo': {'deviceName': '', 'deviceID': '', 'deviceDescription': '', 'deviceLocation': '', 'deviceStatus':
            '', 'DetailAbnormalStatus': {'hardDiskFull': {}, 'hardDiskError': {}, 'ethernetBroken': {}, 'ipaddrConflict':
            {}, 'illegalAccess': {}, 'recordError': {}, 'raidLogicDiskError': {}, 'spareWorkDeviceError': {}},
            'systemContact': '', 'model': '', 'serialNumber': '', 'macAddress': '', 'firmwareVersion': '',
            'firmwareReleasedDate': '', 'bootVersion': '', 'bootReleasedDate': '', 'hardwareVersion': '', 'encoderVersion':
            '', 'encoderReleasedDate': '', 'decoderVersion': '', 'decoderReleasedDate': '', 'softwareVersion': '',
            'capacity': '', 'usedCapacity': '', 'deviceType': '', 'telecontrolID': '', 'supportBeep': '',
            'supportVideoLoss': '', 'firmwareVersionInfo': '', 'actualFloorNum': '', 'subChannelEnabled': '',
            'thrChannelEnabled': '', 'radarVersion': '', 'cameraModuleVersion': '', 'mainversion': '', 'subversion': '',
            'upgradeversion': '', 'customizeversion': '', 'companyName': '', 'copyright': '', 'systemName': '',
            'systemStatus': '', 'isLeaderDevice': '', 'clusterVersion': '', 'customizedInfo': '', 'localZoneNum': '',
            'alarmOutNum': '', 'distanceResolution': '', 'angleResolution': '', 'speedResolution': '', 'detectDistance': '',
            'languageType': '', 'relayNum': '', 'electroLockNum': '', 'RS485Num': '', 'powerOnMode': '', 'DockStation':
            {'Platform': {'type': '', 'ip': '', 'port': '', 'userName': '', 'password': ''}, 'centralStorageBackupEnabled':
            ''}, 'webVersion': '', 'deviceRFProgramVersion': '', 'securityModuleSerialNo': '', 'securityModuleVersion': '',
            'securityChipVersion': '', 'securityModuleKeyVersion': '', 'UIDLampRecognition': {'enabled': ''}, 'bootTime':
            '', 'ZigBeeVersion': {'@min': '0', '@max': '16'}, 'R3Version': {'@min': '0', '@max': '16'}, 'RxVersion':
            {'@min': '0', '@max': '16'}, 'bspVersion': '', 'dspVersion': '', 'localUIVersion': '', 'isResetDeviceLanguage':
            {'@_text': 'false'}, '@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        device_info (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfo]):
    """

    device_info: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = self.device_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_info is not UNSET:
            field_dict["DeviceInfo"] = device_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_device_info_device_info import RootTypeForXMLDeviceInfoDeviceInfo

        d = src_dict.copy()
        _device_info = d.pop("DeviceInfo", UNSET)
        device_info: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfo]
        if isinstance(_device_info, Unset):
            device_info = UNSET
        else:
            device_info = RootTypeForXMLDeviceInfoDeviceInfo.from_dict(_device_info)

        root_type_for_xml_device_info = cls(
            device_info=device_info,
        )

        root_type_for_xml_device_info.additional_properties = d
        return root_type_for_xml_device_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
