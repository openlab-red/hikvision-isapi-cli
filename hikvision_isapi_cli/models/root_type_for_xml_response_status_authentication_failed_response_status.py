from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus")


@attr.s(auto_attribs=True)
class RootTypeForXMLResponseStatusAuthenticationFailedResponseStatus:
    """
    Attributes:
        request_url (Union[Unset, str]):
        status_code (Union[Unset, str]):
        status_string (Union[Unset, str]):
        sub_status_code (Union[Unset, str]):
        lock_status (Union[Unset, str]):
        retry_times (Union[Unset, str]):
        res_lock_time (Union[Unset, str]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    request_url: Union[Unset, str] = UNSET
    status_code: Union[Unset, str] = UNSET
    status_string: Union[Unset, str] = UNSET
    sub_status_code: Union[Unset, str] = UNSET
    lock_status: Union[Unset, str] = UNSET
    retry_times: Union[Unset, str] = UNSET
    res_lock_time: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_url = self.request_url
        status_code = self.status_code
        status_string = self.status_string
        sub_status_code = self.sub_status_code
        lock_status = self.lock_status
        retry_times = self.retry_times
        res_lock_time = self.res_lock_time
        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_url is not UNSET:
            field_dict["requestURL"] = request_url
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if status_string is not UNSET:
            field_dict["statusString"] = status_string
        if sub_status_code is not UNSET:
            field_dict["subStatusCode"] = sub_status_code
        if lock_status is not UNSET:
            field_dict["lockStatus"] = lock_status
        if retry_times is not UNSET:
            field_dict["retryTimes"] = retry_times
        if res_lock_time is not UNSET:
            field_dict["resLockTime"] = res_lock_time
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_url = d.pop("requestURL", UNSET)

        status_code = d.pop("statusCode", UNSET)

        status_string = d.pop("statusString", UNSET)

        sub_status_code = d.pop("subStatusCode", UNSET)

        lock_status = d.pop("lockStatus", UNSET)

        retry_times = d.pop("retryTimes", UNSET)

        res_lock_time = d.pop("resLockTime", UNSET)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_response_status_authentication_failed_response_status = cls(
            request_url=request_url,
            status_code=status_code,
            status_string=status_string,
            sub_status_code=sub_status_code,
            lock_status=lock_status,
            retry_times=retry_times,
            res_lock_time=res_lock_time,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_response_status_authentication_failed_response_status.additional_properties = d
        return root_type_for_xml_response_status_authentication_failed_response_status

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
