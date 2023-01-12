from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLStreamingChannelAudio")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelAudio:
    """
    Attributes:
        enabled (Union[Unset, str]):
        audio_input_channel_id (Union[Unset, str]):
        audio_compression_type (Union[Unset, str]):
    """

    enabled: Union[Unset, str] = UNSET
    audio_input_channel_id: Union[Unset, str] = UNSET
    audio_compression_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        audio_input_channel_id = self.audio_input_channel_id
        audio_compression_type = self.audio_compression_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if audio_input_channel_id is not UNSET:
            field_dict["audioInputChannelID"] = audio_input_channel_id
        if audio_compression_type is not UNSET:
            field_dict["audioCompressionType"] = audio_compression_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        audio_input_channel_id = d.pop("audioInputChannelID", UNSET)

        audio_compression_type = d.pop("audioCompressionType", UNSET)

        root_type_for_xml_streaming_channel_audio = cls(
            enabled=enabled,
            audio_input_channel_id=audio_input_channel_id,
            audio_compression_type=audio_compression_type,
        )

        root_type_for_xml_streaming_channel_audio.additional_properties = d
        return root_type_for_xml_streaming_channel_audio

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
