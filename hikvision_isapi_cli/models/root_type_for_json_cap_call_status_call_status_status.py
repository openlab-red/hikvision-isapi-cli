from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForJSONCapCallStatusCallStatusStatus")


@attr.s(auto_attribs=True)
class RootTypeForJSONCapCallStatusCallStatusStatus:
    """
    Attributes:
        opt (Union[Unset, List[str]]):
    """

    opt: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opt: Union[Unset, List[str]] = UNSET
        if not isinstance(self.opt, Unset):
            opt = self.opt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opt is not UNSET:
            field_dict["@opt"] = opt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        opt = cast(List[str], d.pop("@opt", UNSET))

        root_type_for_json_cap_call_status_call_status_status = cls(
            opt=opt,
        )

        root_type_for_json_cap_call_status_call_status_status.additional_properties = d
        return root_type_for_json_cap_call_status_call_status_status

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
