from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_json_cap_call_status_call_status import RootTypeForJSONCapCallStatusCallStatus


T = TypeVar("T", bound="RootTypeForJSONCapCallStatus")


@attr.s(auto_attribs=True)
class RootTypeForJSONCapCallStatus:
    """JSON message about the capability of getting the call statusv

    Example:
        {'CallStatus': {'status': {'@opt': ['idle', 'ring', 'onCall']}}}

    Attributes:
        call_status (Union[Unset, RootTypeForJSONCapCallStatusCallStatus]):
    """

    call_status: Union[Unset, "RootTypeForJSONCapCallStatusCallStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.call_status, Unset):
            call_status = self.call_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_status is not UNSET:
            field_dict["CallStatus"] = call_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_json_cap_call_status_call_status import RootTypeForJSONCapCallStatusCallStatus

        d = src_dict.copy()
        _call_status = d.pop("CallStatus", UNSET)
        call_status: Union[Unset, RootTypeForJSONCapCallStatusCallStatus]
        if isinstance(_call_status, Unset):
            call_status = UNSET
        else:
            call_status = RootTypeForJSONCapCallStatusCallStatus.from_dict(_call_status)

        root_type_for_json_cap_call_status = cls(
            call_status=call_status,
        )

        root_type_for_json_cap_call_status.additional_properties = d
        return root_type_for_json_cap_call_status

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
