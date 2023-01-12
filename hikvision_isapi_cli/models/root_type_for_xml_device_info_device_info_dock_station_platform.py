from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform")


@attr.s(auto_attribs=True)
class RootTypeForXMLDeviceInfoDeviceInfoDockStationPlatform:
    """
    Attributes:
        type (Union[Unset, str]):
        ip (Union[Unset, str]):
        port (Union[Unset, str]):
        user_name (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        ip = self.ip
        port = self.port
        user_name = self.user_name
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port is not UNSET:
            field_dict["port"] = port
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        ip = d.pop("ip", UNSET)

        port = d.pop("port", UNSET)

        user_name = d.pop("userName", UNSET)

        password = d.pop("password", UNSET)

        root_type_for_xml_device_info_device_info_dock_station_platform = cls(
            type=type,
            ip=ip,
            port=port,
            user_name=user_name,
            password=password,
        )

        root_type_for_xml_device_info_device_info_dock_station_platform.additional_properties = d
        return root_type_for_xml_device_info_device_info_dock_station_platform

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
