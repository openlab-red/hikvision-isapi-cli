from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelVideoSVC")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelVideoSVC:
    """
    Attributes:
        enabled (Union[Unset, str]):
        svc_mode (Union[Unset, str]):
    """

    enabled: Union[Unset, str] = UNSET
    svc_mode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        svc_mode = self.svc_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if svc_mode is not UNSET:
            field_dict["SVCMode"] = svc_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        svc_mode = d.pop("SVCMode", UNSET)

        root_type_for_xml_streaming_channel_streaming_channel_video_svc = cls(
            enabled=enabled,
            svc_mode=svc_mode,
        )

        root_type_for_xml_streaming_channel_streaming_channel_video_svc.additional_properties = d
        return root_type_for_xml_streaming_channel_streaming_channel_video_svc

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
