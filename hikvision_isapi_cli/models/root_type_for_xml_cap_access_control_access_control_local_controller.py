from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_cap_access_control_access_control_local_controller_is_support_local_controller_control import (
        RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerControl,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_local_controller_is_support_local_controller_manage import (
        RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerManage,
    )


T = TypeVar("T", bound="RootTypeForXMLCapAccessControlAccessControlLocalController")


@attr.s(auto_attribs=True)
class RootTypeForXMLCapAccessControlAccessControlLocalController:
    """
    Attributes:
        is_support_local_controller_manage (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerManage]):
        is_support_local_controller_control (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerControl]):
    """

    is_support_local_controller_manage: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerManage"
    ] = UNSET
    is_support_local_controller_control: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerControl"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_support_local_controller_manage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_local_controller_manage, Unset):
            is_support_local_controller_manage = self.is_support_local_controller_manage.to_dict()

        is_support_local_controller_control: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_local_controller_control, Unset):
            is_support_local_controller_control = self.is_support_local_controller_control.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_support_local_controller_manage is not UNSET:
            field_dict["isSupportLocalControllerManage"] = is_support_local_controller_manage
        if is_support_local_controller_control is not UNSET:
            field_dict["isSupportLocalControllerControl"] = is_support_local_controller_control

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_cap_access_control_access_control_local_controller_is_support_local_controller_control import (
            RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerControl,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_local_controller_is_support_local_controller_manage import (
            RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerManage,
        )

        d = src_dict.copy()
        _is_support_local_controller_manage = d.pop("isSupportLocalControllerManage", UNSET)
        is_support_local_controller_manage: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerManage
        ]
        if isinstance(_is_support_local_controller_manage, Unset):
            is_support_local_controller_manage = UNSET
        else:
            is_support_local_controller_manage = (
                RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerManage.from_dict(
                    _is_support_local_controller_manage
                )
            )

        _is_support_local_controller_control = d.pop("isSupportLocalControllerControl", UNSET)
        is_support_local_controller_control: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerControl
        ]
        if isinstance(_is_support_local_controller_control, Unset):
            is_support_local_controller_control = UNSET
        else:
            is_support_local_controller_control = (
                RootTypeForXMLCapAccessControlAccessControlLocalControllerIsSupportLocalControllerControl.from_dict(
                    _is_support_local_controller_control
                )
            )

        root_type_for_xml_cap_access_control_access_control_local_controller = cls(
            is_support_local_controller_manage=is_support_local_controller_manage,
            is_support_local_controller_control=is_support_local_controller_control,
        )

        root_type_for_xml_cap_access_control_access_control_local_controller.additional_properties = d
        return root_type_for_xml_cap_access_control_access_control_local_controller

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
