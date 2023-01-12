from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_cap_remote_control_door_remote_control_door_cmd import (
        RootTypeForXMLCapRemoteControlDoorRemoteControlDoorCmd,
    )
    from ..models.root_type_for_xml_cap_remote_control_door_remote_control_door_door_no import (
        RootTypeForXMLCapRemoteControlDoorRemoteControlDoorDoorNo,
    )
    from ..models.root_type_for_xml_cap_remote_control_door_remote_control_door_password import (
        RootTypeForXMLCapRemoteControlDoorRemoteControlDoorPassword,
    )


T = TypeVar("T", bound="RootTypeForXMLCapRemoteControlDoorRemoteControlDoor")


@attr.s(auto_attribs=True)
class RootTypeForXMLCapRemoteControlDoorRemoteControlDoor:
    """
    Attributes:
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
        door_no (Union[Unset, RootTypeForXMLCapRemoteControlDoorRemoteControlDoorDoorNo]):
        cmd (Union[Unset, RootTypeForXMLCapRemoteControlDoorRemoteControlDoorCmd]):
        password (Union[Unset, RootTypeForXMLCapRemoteControlDoorRemoteControlDoorPassword]):
    """

    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    door_no: Union[Unset, "RootTypeForXMLCapRemoteControlDoorRemoteControlDoorDoorNo"] = UNSET
    cmd: Union[Unset, "RootTypeForXMLCapRemoteControlDoorRemoteControlDoorCmd"] = UNSET
    password: Union[Unset, "RootTypeForXMLCapRemoteControlDoorRemoteControlDoorPassword"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        xmlns = self.xmlns
        door_no: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.door_no, Unset):
            door_no = self.door_no.to_dict()

        cmd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd.to_dict()

        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns
        if door_no is not UNSET:
            field_dict["doorNo"] = door_no
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_cap_remote_control_door_remote_control_door_cmd import (
            RootTypeForXMLCapRemoteControlDoorRemoteControlDoorCmd,
        )
        from ..models.root_type_for_xml_cap_remote_control_door_remote_control_door_door_no import (
            RootTypeForXMLCapRemoteControlDoorRemoteControlDoorDoorNo,
        )
        from ..models.root_type_for_xml_cap_remote_control_door_remote_control_door_password import (
            RootTypeForXMLCapRemoteControlDoorRemoteControlDoorPassword,
        )

        d = src_dict.copy()
        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        _door_no = d.pop("doorNo", UNSET)
        door_no: Union[Unset, RootTypeForXMLCapRemoteControlDoorRemoteControlDoorDoorNo]
        if isinstance(_door_no, Unset):
            door_no = UNSET
        else:
            door_no = RootTypeForXMLCapRemoteControlDoorRemoteControlDoorDoorNo.from_dict(_door_no)

        _cmd = d.pop("cmd", UNSET)
        cmd: Union[Unset, RootTypeForXMLCapRemoteControlDoorRemoteControlDoorCmd]
        if isinstance(_cmd, Unset):
            cmd = UNSET
        else:
            cmd = RootTypeForXMLCapRemoteControlDoorRemoteControlDoorCmd.from_dict(_cmd)

        _password = d.pop("password", UNSET)
        password: Union[Unset, RootTypeForXMLCapRemoteControlDoorRemoteControlDoorPassword]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = RootTypeForXMLCapRemoteControlDoorRemoteControlDoorPassword.from_dict(_password)

        root_type_for_xml_cap_remote_control_door_remote_control_door = cls(
            version=version,
            xmlns=xmlns,
            door_no=door_no,
            cmd=cmd,
            password=password,
        )

        root_type_for_xml_cap_remote_control_door_remote_control_door.additional_properties = d
        return root_type_for_xml_cap_remote_control_door_remote_control_door

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
