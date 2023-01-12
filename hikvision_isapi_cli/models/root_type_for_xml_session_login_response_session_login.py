from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLSessionLoginResponseSessionLogin")


@attr.s(auto_attribs=True)
class RootTypeForXMLSessionLoginResponseSessionLogin:
    """
    Attributes:
        status_value (Union[Unset, str]):
        status_string (Union[Unset, str]):
        is_default_password (Union[Unset, str]):
        is_risk_password (Union[Unset, str]):
        is_activated (Union[Unset, str]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    status_value: Union[Unset, str] = UNSET
    status_string: Union[Unset, str] = UNSET
    is_default_password: Union[Unset, str] = UNSET
    is_risk_password: Union[Unset, str] = UNSET
    is_activated: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_value = self.status_value
        status_string = self.status_string
        is_default_password = self.is_default_password
        is_risk_password = self.is_risk_password
        is_activated = self.is_activated
        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_value is not UNSET:
            field_dict["statusValue"] = status_value
        if status_string is not UNSET:
            field_dict["statusString"] = status_string
        if is_default_password is not UNSET:
            field_dict["isDefaultPassword"] = is_default_password
        if is_risk_password is not UNSET:
            field_dict["isRiskPassword"] = is_risk_password
        if is_activated is not UNSET:
            field_dict["isActivated"] = is_activated
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_value = d.pop("statusValue", UNSET)

        status_string = d.pop("statusString", UNSET)

        is_default_password = d.pop("isDefaultPassword", UNSET)

        is_risk_password = d.pop("isRiskPassword", UNSET)

        is_activated = d.pop("isActivated", UNSET)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_session_login_response_session_login = cls(
            status_value=status_value,
            status_string=status_string,
            is_default_password=is_default_password,
            is_risk_password=is_risk_password,
            is_activated=is_activated,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_session_login_response_session_login.additional_properties = d
        return root_type_for_xml_session_login_response_session_login

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
