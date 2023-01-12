from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage")


@attr.s(auto_attribs=True)
class RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage:
    """
    Attributes:
        text (Union[Unset, str]):
    """

    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["@_text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("@_text", UNSET)

        root_type_for_xml_device_info_device_info_is_reset_device_language = cls(
            text=text,
        )

        root_type_for_xml_device_info_device_info_is_reset_device_language.additional_properties = d
        return root_type_for_xml_device_info_device_info_is_reset_device_language

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
