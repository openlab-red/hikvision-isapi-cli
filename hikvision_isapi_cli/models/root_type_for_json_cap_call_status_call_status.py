from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_json_cap_call_status_call_status_status import (
        RootTypeForJSONCapCallStatusCallStatusStatus,
    )


T = TypeVar("T", bound="RootTypeForJSONCapCallStatusCallStatus")


@attr.s(auto_attribs=True)
class RootTypeForJSONCapCallStatusCallStatus:
    """
    Attributes:
        status (Union[Unset, RootTypeForJSONCapCallStatusCallStatusStatus]):
    """

    status: Union[Unset, "RootTypeForJSONCapCallStatusCallStatusStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_json_cap_call_status_call_status_status import (
            RootTypeForJSONCapCallStatusCallStatusStatus,
        )

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, RootTypeForJSONCapCallStatusCallStatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RootTypeForJSONCapCallStatusCallStatusStatus.from_dict(_status)

        root_type_for_json_cap_call_status_call_status = cls(
            status=status,
        )

        root_type_for_json_cap_call_status_call_status.additional_properties = d
        return root_type_for_json_cap_call_status_call_status

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
