from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_user_check_user_check import RootTypeForXMLUserCheckUserCheck


T = TypeVar("T", bound="RootTypeForXMLUserCheck")


@attr.s(auto_attribs=True)
class RootTypeForXMLUserCheck:
    """userCheck message in XML format

    Example:
        {'userCheck': {'statusValue': '', 'statusString': '', 'isDefaultPassword': '', 'isRiskPassword': '',
            'isActivated': '', 'lockStatus': '', 'unlockTime': '', 'retryLoginTime': '', '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        user_check (Union[Unset, RootTypeForXMLUserCheckUserCheck]):
    """

    user_check: Union[Unset, "RootTypeForXMLUserCheckUserCheck"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_check: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_check, Unset):
            user_check = self.user_check.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_check is not UNSET:
            field_dict["userCheck"] = user_check

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_user_check_user_check import RootTypeForXMLUserCheckUserCheck

        d = src_dict.copy()
        _user_check = d.pop("userCheck", UNSET)
        user_check: Union[Unset, RootTypeForXMLUserCheckUserCheck]
        if isinstance(_user_check, Unset):
            user_check = UNSET
        else:
            user_check = RootTypeForXMLUserCheckUserCheck.from_dict(_user_check)

        root_type_for_xml_user_check = cls(
            user_check=user_check,
        )

        root_type_for_xml_user_check.additional_properties = d
        return root_type_for_xml_user_check

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
