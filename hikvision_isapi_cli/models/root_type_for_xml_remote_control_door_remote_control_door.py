from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLRemoteControlDoorRemoteControlDoor")


@attr.s(auto_attribs=True)
class RootTypeForXMLRemoteControlDoorRemoteControlDoor:
    """
    Attributes:
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
        cmd (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    cmd: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        xmlns = self.xmlns
        cmd = self.cmd
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        cmd = d.pop("cmd", UNSET)

        password = d.pop("password", UNSET)

        root_type_for_xml_remote_control_door_remote_control_door = cls(
            version=version,
            xmlns=xmlns,
            cmd=cmd,
            password=password,
        )

        root_type_for_xml_remote_control_door_remote_control_door.additional_properties = d
        return root_type_for_xml_remote_control_door_remote_control_door

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
