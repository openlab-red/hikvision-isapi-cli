from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_session_login_response_session_login import (
        RootTypeForXMLSessionLoginResponseSessionLogin,
    )


T = TypeVar("T", bound="RootTypeForXMLSessionLoginResponse")


@attr.s(auto_attribs=True)
class RootTypeForXMLSessionLoginResponse:
    """
    Example:
        {'SessionLogin': {'statusValue': '200', 'statusString': 'OK', 'isDefaultPassword': 'false', 'isRiskPassword':
            'false', 'isActivated': 'true', '@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        session_login (Union[Unset, RootTypeForXMLSessionLoginResponseSessionLogin]):
    """

    session_login: Union[Unset, "RootTypeForXMLSessionLoginResponseSessionLogin"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_login: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_login, Unset):
            session_login = self.session_login.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_login is not UNSET:
            field_dict["SessionLogin"] = session_login

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_session_login_response_session_login import (
            RootTypeForXMLSessionLoginResponseSessionLogin,
        )

        d = src_dict.copy()
        _session_login = d.pop("SessionLogin", UNSET)
        session_login: Union[Unset, RootTypeForXMLSessionLoginResponseSessionLogin]
        if isinstance(_session_login, Unset):
            session_login = UNSET
        else:
            session_login = RootTypeForXMLSessionLoginResponseSessionLogin.from_dict(_session_login)

        root_type_for_xml_session_login_response = cls(
            session_login=session_login,
        )

        root_type_for_xml_session_login_response.additional_properties = d
        return root_type_for_xml_session_login_response

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
