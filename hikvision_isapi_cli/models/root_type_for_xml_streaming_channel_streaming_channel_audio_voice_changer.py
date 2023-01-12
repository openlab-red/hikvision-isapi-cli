from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelAudioVoiceChanger")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelAudioVoiceChanger:
    """
    Attributes:
        enabled (Union[Unset, str]):
        level (Union[Unset, str]):
    """

    enabled: Union[Unset, str] = UNSET
    level: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        level = self.level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        level = d.pop("level", UNSET)

        root_type_for_xml_streaming_channel_streaming_channel_audio_voice_changer = cls(
            enabled=enabled,
            level=level,
        )

        root_type_for_xml_streaming_channel_streaming_channel_audio_voice_changer.additional_properties = d
        return root_type_for_xml_streaming_channel_streaming_channel_audio_voice_changer

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
