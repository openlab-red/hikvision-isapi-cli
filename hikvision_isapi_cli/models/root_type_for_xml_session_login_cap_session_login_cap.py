from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLSessionLoginCapSessionLoginCap")


@attr.s(auto_attribs=True)
class RootTypeForXMLSessionLoginCapSessionLoginCap:
    """
    Attributes:
        session_id (Union[Unset, str]):
        challenge (Union[Unset, str]):
        iterations (Union[Unset, str]):
        is_irreversible (Union[Unset, str]):
        salt (Union[Unset, str]):
        session_id_version (Union[Unset, str]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    session_id: Union[Unset, str] = UNSET
    challenge: Union[Unset, str] = UNSET
    iterations: Union[Unset, str] = UNSET
    is_irreversible: Union[Unset, str] = UNSET
    salt: Union[Unset, str] = UNSET
    session_id_version: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id
        challenge = self.challenge
        iterations = self.iterations
        is_irreversible = self.is_irreversible
        salt = self.salt
        session_id_version = self.session_id_version
        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionID"] = session_id
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if iterations is not UNSET:
            field_dict["iterations"] = iterations
        if is_irreversible is not UNSET:
            field_dict["isIrreversible"] = is_irreversible
        if salt is not UNSET:
            field_dict["salt"] = salt
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
        session_id = d.pop("sessionID", UNSET)

        challenge = d.pop("challenge", UNSET)

        iterations = d.pop("iterations", UNSET)

        is_irreversible = d.pop("isIrreversible", UNSET)

        salt = d.pop("salt", UNSET)

        session_id_version = d.pop("sessionIDVersion", UNSET)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_session_login_cap_session_login_cap = cls(
            session_id=session_id,
            challenge=challenge,
            iterations=iterations,
            is_irreversible=is_irreversible,
            salt=salt,
            session_id_version=session_id_version,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_session_login_cap_session_login_cap.additional_properties = d
        return root_type_for_xml_session_login_cap_session_login_cap

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
