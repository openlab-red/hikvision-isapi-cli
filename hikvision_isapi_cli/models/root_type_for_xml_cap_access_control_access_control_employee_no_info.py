from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info_character_type import (
        RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoCharacterType,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info_employee_no import (
        RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoEmployeeNo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info_is_support_compress import (
        RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoIsSupportCompress,
    )


T = TypeVar("T", bound="RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo")


@attr.s(auto_attribs=True)
class RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo:
    """
    Attributes:
        employee_no (Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoEmployeeNo]):
        character_type (Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoCharacterType]):
        is_support_compress (Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoIsSupportCompress]):
    """

    employee_no: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoEmployeeNo"] = UNSET
    character_type: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoCharacterType"] = UNSET
    is_support_compress: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoIsSupportCompress"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employee_no: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employee_no, Unset):
            employee_no = self.employee_no.to_dict()

        character_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.character_type, Unset):
            character_type = self.character_type.to_dict()

        is_support_compress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_compress, Unset):
            is_support_compress = self.is_support_compress.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_no is not UNSET:
            field_dict["employeeNo"] = employee_no
        if character_type is not UNSET:
            field_dict["characterType"] = character_type
        if is_support_compress is not UNSET:
            field_dict["isSupportCompress"] = is_support_compress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info_character_type import (
            RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoCharacterType,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info_employee_no import (
            RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoEmployeeNo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info_is_support_compress import (
            RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoIsSupportCompress,
        )

        d = src_dict.copy()
        _employee_no = d.pop("employeeNo", UNSET)
        employee_no: Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoEmployeeNo]
        if isinstance(_employee_no, Unset):
            employee_no = UNSET
        else:
            employee_no = RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoEmployeeNo.from_dict(_employee_no)

        _character_type = d.pop("characterType", UNSET)
        character_type: Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoCharacterType]
        if isinstance(_character_type, Unset):
            character_type = UNSET
        else:
            character_type = RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoCharacterType.from_dict(
                _character_type
            )

        _is_support_compress = d.pop("isSupportCompress", UNSET)
        is_support_compress: Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoIsSupportCompress]
        if isinstance(_is_support_compress, Unset):
            is_support_compress = UNSET
        else:
            is_support_compress = RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfoIsSupportCompress.from_dict(
                _is_support_compress
            )

        root_type_for_xml_cap_access_control_access_control_employee_no_info = cls(
            employee_no=employee_no,
            character_type=character_type,
            is_support_compress=is_support_compress,
        )

        root_type_for_xml_cap_access_control_access_control_employee_no_info.additional_properties = d
        return root_type_for_xml_cap_access_control_access_control_employee_no_info

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
