from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_session_login_cap_session_login_cap import (
        RootTypeForXMLSessionLoginCapSessionLoginCap,
    )


T = TypeVar("T", bound="RootTypeForXMLSessionLoginCap")


@attr.s(auto_attribs=True)
class RootTypeForXMLSessionLoginCap:
    """
    Example:
        {'SessionLoginCap': {'sessionID': '5ab522a707187090e375dc9e07f80f48f6a2a1c4a171b501b47ea9607db57f7f',
            'challenge': '3f559d75aa0c053e631092d75aa59355', 'iterations': '100', 'isIrreversible': 'true', 'salt':
            'ADX8O3PD524FJ1BGFXK7X94SXKU1G3VQGSYKBOXW61S5IJLYWM59B9289WPPFKFV', 'sessionIDVersion': '2', '@version': '2.0',
            '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        session_login_cap (Union[Unset, RootTypeForXMLSessionLoginCapSessionLoginCap]):
    """

    session_login_cap: Union[Unset, "RootTypeForXMLSessionLoginCapSessionLoginCap"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_login_cap: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_login_cap, Unset):
            session_login_cap = self.session_login_cap.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_login_cap is not UNSET:
            field_dict["SessionLoginCap"] = session_login_cap

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_session_login_cap_session_login_cap import (
            RootTypeForXMLSessionLoginCapSessionLoginCap,
        )

        d = src_dict.copy()
        _session_login_cap = d.pop("SessionLoginCap", UNSET)
        session_login_cap: Union[Unset, RootTypeForXMLSessionLoginCapSessionLoginCap]
        if isinstance(_session_login_cap, Unset):
            session_login_cap = UNSET
        else:
            session_login_cap = RootTypeForXMLSessionLoginCapSessionLoginCap.from_dict(_session_login_cap)

        root_type_for_xml_session_login_cap = cls(
            session_login_cap=session_login_cap,
        )

        root_type_for_xml_session_login_cap.additional_properties = d
        return root_type_for_xml_session_login_cap

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
