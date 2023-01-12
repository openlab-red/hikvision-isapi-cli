from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLResponseStatusResponseStatus")


@attr.s(auto_attribs=True)
class RootTypeForXMLResponseStatusResponseStatus:
    """
    Attributes:
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
        request_url (Union[Unset, str]):
        status_code (Union[Unset, str]):
        status_string (Union[Unset, str]):
        sub_status_code (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    request_url: Union[Unset, str] = UNSET
    status_code: Union[Unset, str] = UNSET
    status_string: Union[Unset, str] = UNSET
    sub_status_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        xmlns = self.xmlns
        request_url = self.request_url
        status_code = self.status_code
        status_string = self.status_string
        sub_status_code = self.sub_status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns
        if request_url is not UNSET:
            field_dict["requestURL"] = request_url
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if status_string is not UNSET:
            field_dict["statusString"] = status_string
        if sub_status_code is not UNSET:
            field_dict["subStatusCode"] = sub_status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        request_url = d.pop("requestURL", UNSET)

        status_code = d.pop("statusCode", UNSET)

        status_string = d.pop("statusString", UNSET)

        sub_status_code = d.pop("subStatusCode", UNSET)

        root_type_for_xml_response_status_response_status = cls(
            version=version,
            xmlns=xmlns,
            request_url=request_url,
            status_code=status_code,
            status_string=status_string,
            sub_status_code=sub_status_code,
        )

        root_type_for_xml_response_status_response_status.additional_properties = d
        return root_type_for_xml_response_status_response_status

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
