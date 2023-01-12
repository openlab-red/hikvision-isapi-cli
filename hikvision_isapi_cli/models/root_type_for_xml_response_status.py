from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_response_status_response_status import RootTypeForXMLResponseStatusResponseStatus


T = TypeVar("T", bound="RootTypeForXMLResponseStatus")


@attr.s(auto_attribs=True)
class RootTypeForXMLResponseStatus:
    """ResponseStatus message in XML format

    Example:
        {'ResponseStatus': {'@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema', 'requestURL': '',
            'statusCode': '', 'statusString': '', 'subStatusCode': ''}}

    Attributes:
        response_status (Union[Unset, RootTypeForXMLResponseStatusResponseStatus]):
    """

    response_status: Union[Unset, "RootTypeForXMLResponseStatusResponseStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        response_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response_status, Unset):
            response_status = self.response_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response_status is not UNSET:
            field_dict["ResponseStatus"] = response_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_response_status_response_status import (
            RootTypeForXMLResponseStatusResponseStatus,
        )

        d = src_dict.copy()
        _response_status = d.pop("ResponseStatus", UNSET)
        response_status: Union[Unset, RootTypeForXMLResponseStatusResponseStatus]
        if isinstance(_response_status, Unset):
            response_status = UNSET
        else:
            response_status = RootTypeForXMLResponseStatusResponseStatus.from_dict(_response_status)

        root_type_for_xml_response_status = cls(
            response_status=response_status,
        )

        root_type_for_xml_response_status.additional_properties = d
        return root_type_for_xml_response_status

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
