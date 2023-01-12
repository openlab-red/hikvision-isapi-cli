from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLSessionLoginSessionLogin")


@attr.s(auto_attribs=True)
class RootTypeForXMLSessionLoginSessionLogin:
    """
    Attributes:
        user_name (Union[Unset, str]):
        password (Union[Unset, str]):
        session_id (Union[Unset, str]):
        is_support_session_tag (Union[Unset, str]):
        is_session_id_valid_long_term (Union[Unset, str]):
        session_id_version (Union[Unset, str]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    user_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    is_support_session_tag: Union[Unset, str] = UNSET
    is_session_id_valid_long_term: Union[Unset, str] = UNSET
    session_id_version: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        password = self.password
        session_id = self.session_id
        is_support_session_tag = self.is_support_session_tag
        is_session_id_valid_long_term = self.is_session_id_valid_long_term
        session_id_version = self.session_id_version
        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if password is not UNSET:
            field_dict["password"] = password
        if session_id is not UNSET:
            field_dict["sessionID"] = session_id
        if is_support_session_tag is not UNSET:
            field_dict["isSupportSessionTag"] = is_support_session_tag
        if is_session_id_valid_long_term is not UNSET:
            field_dict["isSessionIDValidLongTerm"] = is_session_id_valid_long_term
        if session_id_version is not UNSET:
            field_dict["sessionIDVersion"] = session_id_version
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName", UNSET)

        password = d.pop("password", UNSET)

        session_id = d.pop("sessionID", UNSET)

        is_support_session_tag = d.pop("isSupportSessionTag", UNSET)

        is_session_id_valid_long_term = d.pop("isSessionIDValidLongTerm", UNSET)

        session_id_version = d.pop("sessionIDVersion", UNSET)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_session_login_session_login = cls(
            user_name=user_name,
            password=password,
            session_id=session_id,
            is_support_session_tag=is_support_session_tag,
            is_session_id_valid_long_term=is_session_id_valid_long_term,
            session_id_version=session_id_version,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_session_login_session_login.additional_properties = d
        return root_type_for_xml_session_login_session_login

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
