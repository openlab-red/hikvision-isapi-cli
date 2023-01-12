from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_response_status_authentication_failed_response_status import (
        RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus,
    )


T = TypeVar("T", bound="RootTypeForXMLResponseStatusAuthenticationFailed")


@attr.s(auto_attribs=True)
class RootTypeForXMLResponseStatusAuthenticationFailed:
    """
    Example:
        {'ResponseStatus': {'requestURL': '', 'statusCode': '', 'statusString': '', 'subStatusCode': '', 'lockStatus':
            '', 'retryTimes': '', 'resLockTime': '', '@version': '1.0', '@xmlns': 'http://www.std-cgi.org/ver20/XMLSchema'}}

    Attributes:
        response_status (Union[Unset, RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus]):
    """

    response_status: Union[Unset, "RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus"] = UNSET
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
        from ..models.root_type_for_xml_response_status_authentication_failed_response_status import (
            RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus,
        )

        d = src_dict.copy()
        _response_status = d.pop("ResponseStatus", UNSET)
        response_status: Union[Unset, RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus]
        if isinstance(_response_status, Unset):
            response_status = UNSET
        else:
            response_status = RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus.from_dict(_response_status)

        root_type_for_xml_response_status_authentication_failed = cls(
            response_status=response_status,
        )

        root_type_for_xml_response_status_authentication_failed.additional_properties = d
        return root_type_for_xml_response_status_authentication_failed

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
