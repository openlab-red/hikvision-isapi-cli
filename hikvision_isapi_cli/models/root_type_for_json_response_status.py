from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForJSONResponseStatus")


@attr.s(auto_attribs=True)
class RootTypeForJSONResponseStatus:
    """JSON message about response status

    Example:
        {'requestURL': '', 'statusCode': 200, 'statusString': '', 'subStatusCode': '', 'errorCode': 1, 'errorMsg': '',
            'MErrCode': '0xFFFFFFFF', 'MErrDevSelfEx': '0xFFFFFFFF'}

    Attributes:
        request_url (Union[Unset, str]):
        status_code (Union[Unset, int]):
        status_string (Union[Unset, str]):
        sub_status_code (Union[Unset, str]):
        error_code (Union[Unset, int]):
        error_msg (Union[Unset, str]):
        m_err_code (Union[Unset, str]):
        m_err_dev_self_ex (Union[Unset, str]):
    """

    request_url: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    status_string: Union[Unset, str] = UNSET
    sub_status_code: Union[Unset, str] = UNSET
    error_code: Union[Unset, int] = UNSET
    error_msg: Union[Unset, str] = UNSET
    m_err_code: Union[Unset, str] = UNSET
    m_err_dev_self_ex: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_url = self.request_url
        status_code = self.status_code
        status_string = self.status_string
        sub_status_code = self.sub_status_code
        error_code = self.error_code
        error_msg = self.error_msg
        m_err_code = self.m_err_code
        m_err_dev_self_ex = self.m_err_dev_self_ex

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
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_msg is not UNSET:
            field_dict["errorMsg"] = error_msg
        if m_err_code is not UNSET:
            field_dict["MErrCode"] = m_err_code
        if m_err_dev_self_ex is not UNSET:
            field_dict["MErrDevSelfEx"] = m_err_dev_self_ex

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_url = d.pop("requestURL", UNSET)

        status_code = d.pop("statusCode", UNSET)

        status_string = d.pop("statusString", UNSET)

        sub_status_code = d.pop("subStatusCode", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        m_err_code = d.pop("MErrCode", UNSET)

        m_err_dev_self_ex = d.pop("MErrDevSelfEx", UNSET)

        root_type_for_json_response_status = cls(
            request_url=request_url,
            status_code=status_code,
            status_string=status_string,
            sub_status_code=sub_status_code,
            error_code=error_code,
            error_msg=error_msg,
            m_err_code=m_err_code,
            m_err_dev_self_ex=m_err_dev_self_ex,
        )

        root_type_for_json_response_status.additional_properties = d
        return root_type_for_json_response_status

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
