from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_session_login_session_login import RootTypeForXMLSessionLoginSessionLogin


T = TypeVar("T", bound="RootTypeForXMLSessionLogin")


@attr.s(auto_attribs=True)
class RootTypeForXMLSessionLogin:
    """
    Example:
        {'SessionLogin': {'userName': 'admin', 'password': 'xxxxxxxxxxxx', 'sessionID':
            '5ab522a707187090e375dc9e07f80f48f6a2a1c4a171b501b47ea9607db57f7f', 'isSupportSessionTag': 'false',
            'isSessionIDValidLongTerm': 'false', 'sessionIDVersion': '2', '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        session_login (Union[Unset, RootTypeForXMLSessionLoginSessionLogin]):
    """

    session_login: Union[Unset, "RootTypeForXMLSessionLoginSessionLogin"] = UNSET
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
        from ..models.root_type_for_xml_session_login_session_login import RootTypeForXMLSessionLoginSessionLogin

        d = src_dict.copy()
        _session_login = d.pop("SessionLogin", UNSET)
        session_login: Union[Unset, RootTypeForXMLSessionLoginSessionLogin]
        if isinstance(_session_login, Unset):
            session_login = UNSET
        else:
            session_login = RootTypeForXMLSessionLoginSessionLogin.from_dict(_session_login)

        root_type_for_xml_session_login = cls(
            session_login=session_login,
        )

        root_type_for_xml_session_login.additional_properties = d
        return root_type_for_xml_session_login

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
