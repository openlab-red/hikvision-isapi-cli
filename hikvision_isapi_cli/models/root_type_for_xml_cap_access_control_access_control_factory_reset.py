from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_cap_access_control_access_control_factory_reset_mode import (
        RootTypeForXMLCapAccessControlAccessControlFactoryResetMode,
    )


T = TypeVar("T", bound="RootTypeForXMLCapAccessControlAccessControlFactoryReset")


@attr.s(auto_attribs=True)
class RootTypeForXMLCapAccessControlAccessControlFactoryReset:
    """
    Attributes:
        is_support_factory_reset (Union[Unset, str]):
        mode (Union[Unset, RootTypeForXMLCapAccessControlAccessControlFactoryResetMode]):
    """

    is_support_factory_reset: Union[Unset, str] = UNSET
    mode: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlFactoryResetMode"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_support_factory_reset = self.is_support_factory_reset
        mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_support_factory_reset is not UNSET:
            field_dict["isSupportFactoryReset"] = is_support_factory_reset
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_cap_access_control_access_control_factory_reset_mode import (
            RootTypeForXMLCapAccessControlAccessControlFactoryResetMode,
        )

        d = src_dict.copy()
        is_support_factory_reset = d.pop("isSupportFactoryReset", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, RootTypeForXMLCapAccessControlAccessControlFactoryResetMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = RootTypeForXMLCapAccessControlAccessControlFactoryResetMode.from_dict(_mode)

        root_type_for_xml_cap_access_control_access_control_factory_reset = cls(
            is_support_factory_reset=is_support_factory_reset,
            mode=mode,
        )

        root_type_for_xml_cap_access_control_access_control_factory_reset.additional_properties = d
        return root_type_for_xml_cap_access_control_access_control_factory_reset

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
