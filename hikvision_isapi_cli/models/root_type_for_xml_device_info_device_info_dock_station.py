from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_device_info_device_info_dock_station_platform import (
        RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform,
    )


T = TypeVar("T", bound="RootTypeForXMLDeviceInfoDeviceInfoDockStation")


@attr.s(auto_attribs=True)
class RootTypeForXMLDeviceInfoDeviceInfoDockStation:
    """
    Attributes:
        platform (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform]):
        central_storage_backup_enabled (Union[Unset, str]):
    """

    platform: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform"] = UNSET
    central_storage_backup_enabled: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        platform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.to_dict()

        central_storage_backup_enabled = self.central_storage_backup_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["Platform"] = platform
        if central_storage_backup_enabled is not UNSET:
            field_dict["centralStorageBackupEnabled"] = central_storage_backup_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_device_info_device_info_dock_station_platform import (
            RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform,
        )

        d = src_dict.copy()
        _platform = d.pop("Platform", UNSET)
        platform: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform.from_dict(_platform)

        central_storage_backup_enabled = d.pop("centralStorageBackupEnabled", UNSET)

        root_type_for_xml_device_info_device_info_dock_station = cls(
            platform=platform,
            central_storage_backup_enabled=central_storage_backup_enabled,
        )

        root_type_for_xml_device_info_device_info_dock_station.additional_properties = d
        return root_type_for_xml_device_info_device_info_dock_station

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
