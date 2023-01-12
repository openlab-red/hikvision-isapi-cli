from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio_audio_compression_type import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioCompressionType,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio_audio_inbound_compression_type import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioInboundCompressionType,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio_voice_changer import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioVoiceChanger,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio:
    """
    Attributes:
        enabled (Union[Unset, str]):
        audio_input_channel_id (Union[Unset, str]):
        audio_compression_type (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioCompressionType]):
        audio_inbound_compression_type (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStr
            eamingChannelAudioAudioInboundCompressionType]):
        audio_bit_rate (Union[Unset, str]):
        audio_sampling_rate (Union[Unset, str]):
        audio_resolution (Union[Unset, str]):
        voice_changer (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioVoiceChanger]):
    """

    enabled: Union[Unset, str] = UNSET
    audio_input_channel_id: Union[Unset, str] = UNSET
    audio_compression_type: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioCompressionType",
    ] = UNSET
    audio_inbound_compression_type: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioInboundCompressionType",
    ] = UNSET
    audio_bit_rate: Union[Unset, str] = UNSET
    audio_sampling_rate: Union[Unset, str] = UNSET
    audio_resolution: Union[Unset, str] = UNSET
    voice_changer: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioVoiceChanger"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        audio_input_channel_id = self.audio_input_channel_id
        audio_compression_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio_compression_type, Unset):
            audio_compression_type = self.audio_compression_type.to_dict()

        audio_inbound_compression_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio_inbound_compression_type, Unset):
            audio_inbound_compression_type = self.audio_inbound_compression_type.to_dict()

        audio_bit_rate = self.audio_bit_rate
        audio_sampling_rate = self.audio_sampling_rate
        audio_resolution = self.audio_resolution
        voice_changer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voice_changer, Unset):
            voice_changer = self.voice_changer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if audio_input_channel_id is not UNSET:
            field_dict["audioInputChannelID"] = audio_input_channel_id
        if audio_compression_type is not UNSET:
            field_dict["audioCompressionType"] = audio_compression_type
        if audio_inbound_compression_type is not UNSET:
            field_dict["audioInboundCompressionType"] = audio_inbound_compression_type
        if audio_bit_rate is not UNSET:
            field_dict["audioBitRate"] = audio_bit_rate
        if audio_sampling_rate is not UNSET:
            field_dict["audioSamplingRate"] = audio_sampling_rate
        if audio_resolution is not UNSET:
            field_dict["audioResolution"] = audio_resolution
        if voice_changer is not UNSET:
            field_dict["VoiceChanger"] = voice_changer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio_audio_compression_type import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioCompressionType,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio_audio_inbound_compression_type import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioInboundCompressionType,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio_voice_changer import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioVoiceChanger,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        audio_input_channel_id = d.pop("audioInputChannelID", UNSET)

        _audio_compression_type = d.pop("audioCompressionType", UNSET)
        audio_compression_type: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioCompressionType,
        ]
        if isinstance(_audio_compression_type, Unset):
            audio_compression_type = UNSET
        else:
            audio_compression_type = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioCompressionType.from_dict(
                _audio_compression_type
            )

        _audio_inbound_compression_type = d.pop("audioInboundCompressionType", UNSET)
        audio_inbound_compression_type: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioInboundCompressionType,
        ]
        if isinstance(_audio_inbound_compression_type, Unset):
            audio_inbound_compression_type = UNSET
        else:
            audio_inbound_compression_type = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioAudioInboundCompressionType.from_dict(
                _audio_inbound_compression_type
            )

        audio_bit_rate = d.pop("audioBitRate", UNSET)

        audio_sampling_rate = d.pop("audioSamplingRate", UNSET)

        audio_resolution = d.pop("audioResolution", UNSET)

        _voice_changer = d.pop("VoiceChanger", UNSET)
        voice_changer: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioVoiceChanger
        ]
        if isinstance(_voice_changer, Unset):
            voice_changer = UNSET
        else:
            voice_changer = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudioVoiceChanger.from_dict(
                _voice_changer
            )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio = cls(
            enabled=enabled,
            audio_input_channel_id=audio_input_channel_id,
            audio_compression_type=audio_compression_type,
            audio_inbound_compression_type=audio_inbound_compression_type,
            audio_bit_rate=audio_bit_rate,
            audio_sampling_rate=audio_sampling_rate,
            audio_resolution=audio_resolution,
            voice_changer=voice_changer,
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio

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
