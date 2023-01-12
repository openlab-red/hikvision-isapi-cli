from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_remote_control_door_remote_control_door import (
        RootTypeForXMLRemoteControlDoorRemoteControlDoor,
    )


T = TypeVar("T", bound="RootTypeForXMLRemoteControlDoor")


@attr.s(auto_attribs=True)
class RootTypeForXMLRemoteControlDoor:
    """RemoteControlDoor message in XML format

    Example:
        {'RemoteControlDoor': {'@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema', 'cmd': '',
            'password': ''}}

    Attributes:
        remote_control_door (Union[Unset, RootTypeForXMLRemoteControlDoorRemoteControlDoor]):
    """

    remote_control_door: Union[Unset, "RootTypeForXMLRemoteControlDoorRemoteControlDoor"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remote_control_door: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remote_control_door, Unset):
            remote_control_door = self.remote_control_door.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remote_control_door is not UNSET:
            field_dict["RemoteControlDoor"] = remote_control_door

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_remote_control_door_remote_control_door import (
            RootTypeForXMLRemoteControlDoorRemoteControlDoor,
        )

        d = src_dict.copy()
        _remote_control_door = d.pop("RemoteControlDoor", UNSET)
        remote_control_door: Union[Unset, RootTypeForXMLRemoteControlDoorRemoteControlDoor]
        if isinstance(_remote_control_door, Unset):
            remote_control_door = UNSET
        else:
            remote_control_door = RootTypeForXMLRemoteControlDoorRemoteControlDoor.from_dict(_remote_control_door)

        root_type_for_xml_remote_control_door = cls(
            remote_control_door=remote_control_door,
        )

        root_type_for_xml_remote_control_door.additional_properties = d
        return root_type_for_xml_remote_control_door

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
