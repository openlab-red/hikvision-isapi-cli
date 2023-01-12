from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_bit_rate import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioBitRate,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_compression_type import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioCompressionType,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_inbound_compression_type import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInboundCompressionType,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_input_type import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInputType,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_enabled import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelEnabled,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_id import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelId,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_line_out_forbidden import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelLineOutForbidden,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_mic_in_forbidden import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicInForbidden,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_microphone_volume import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicrophoneVolume,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_noisereduce import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelNoisereduce,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_speaker_volume import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelSpeakerVolume,
    )


T = TypeVar("T", bound="RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel")


@attr.s(auto_attribs=True)
class RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel:
    """
    Attributes:
        id (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelId]):
        enabled (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelEnabled]):
        audio_compression_type (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioCompressionType]):
        audio_inbound_compression_type (Union[Unset,
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInboundCompressionType]):
        speaker_volume (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelSpeakerVolume]):
        microphone_volume (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicrophoneVolume]):
        noisereduce (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelNoisereduce]):
        audio_bit_rate (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioBitRate]):
        audio_input_type (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInputType]):
        associate_video_inputs (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs]):
        line_out_forbidden (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelLineOutForbidden]):
        mic_in_forbidden (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicInForbidden]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    id: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelId"] = UNSET
    enabled: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelEnabled"] = UNSET
    audio_compression_type: Union[
        Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioCompressionType"
    ] = UNSET
    audio_inbound_compression_type: Union[
        Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInboundCompressionType"
    ] = UNSET
    speaker_volume: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelSpeakerVolume"] = UNSET
    microphone_volume: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicrophoneVolume"] = UNSET
    noisereduce: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelNoisereduce"] = UNSET
    audio_bit_rate: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioBitRate"] = UNSET
    audio_input_type: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInputType"] = UNSET
    associate_video_inputs: Union[
        Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs"
    ] = UNSET
    line_out_forbidden: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelLineOutForbidden"] = UNSET
    mic_in_forbidden: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicInForbidden"] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        enabled: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = self.enabled.to_dict()

        audio_compression_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio_compression_type, Unset):
            audio_compression_type = self.audio_compression_type.to_dict()

        audio_inbound_compression_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio_inbound_compression_type, Unset):
            audio_inbound_compression_type = self.audio_inbound_compression_type.to_dict()

        speaker_volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.speaker_volume, Unset):
            speaker_volume = self.speaker_volume.to_dict()

        microphone_volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.microphone_volume, Unset):
            microphone_volume = self.microphone_volume.to_dict()

        noisereduce: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.noisereduce, Unset):
            noisereduce = self.noisereduce.to_dict()

        audio_bit_rate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio_bit_rate, Unset):
            audio_bit_rate = self.audio_bit_rate.to_dict()

        audio_input_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio_input_type, Unset):
            audio_input_type = self.audio_input_type.to_dict()

        associate_video_inputs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.associate_video_inputs, Unset):
            associate_video_inputs = self.associate_video_inputs.to_dict()

        line_out_forbidden: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_out_forbidden, Unset):
            line_out_forbidden = self.line_out_forbidden.to_dict()

        mic_in_forbidden: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mic_in_forbidden, Unset):
            mic_in_forbidden = self.mic_in_forbidden.to_dict()

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if audio_compression_type is not UNSET:
            field_dict["audioCompressionType"] = audio_compression_type
        if audio_inbound_compression_type is not UNSET:
            field_dict["audioInboundCompressionType"] = audio_inbound_compression_type
        if speaker_volume is not UNSET:
            field_dict["speakerVolume"] = speaker_volume
        if microphone_volume is not UNSET:
            field_dict["microphoneVolume"] = microphone_volume
        if noisereduce is not UNSET:
            field_dict["noisereduce"] = noisereduce
        if audio_bit_rate is not UNSET:
            field_dict["audioBitRate"] = audio_bit_rate
        if audio_input_type is not UNSET:
            field_dict["audioInputType"] = audio_input_type
        if associate_video_inputs is not UNSET:
            field_dict["associateVideoInputs"] = associate_video_inputs
        if line_out_forbidden is not UNSET:
            field_dict["lineOutForbidden"] = line_out_forbidden
        if mic_in_forbidden is not UNSET:
            field_dict["micInForbidden"] = mic_in_forbidden
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_bit_rate import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioBitRate,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_compression_type import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioCompressionType,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_inbound_compression_type import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInboundCompressionType,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_audio_input_type import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInputType,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_enabled import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelEnabled,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_id import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelId,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_line_out_forbidden import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelLineOutForbidden,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_mic_in_forbidden import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicInForbidden,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_microphone_volume import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicrophoneVolume,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_noisereduce import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelNoisereduce,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_speaker_volume import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelSpeakerVolume,
        )

        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelId.from_dict(_id)

        _enabled = d.pop("enabled", UNSET)
        enabled: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelEnabled]
        if isinstance(_enabled, Unset):
            enabled = UNSET
        else:
            enabled = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelEnabled.from_dict(_enabled)

        _audio_compression_type = d.pop("audioCompressionType", UNSET)
        audio_compression_type: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioCompressionType]
        if isinstance(_audio_compression_type, Unset):
            audio_compression_type = UNSET
        else:
            audio_compression_type = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioCompressionType.from_dict(
                _audio_compression_type
            )

        _audio_inbound_compression_type = d.pop("audioInboundCompressionType", UNSET)
        audio_inbound_compression_type: Union[
            Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInboundCompressionType
        ]
        if isinstance(_audio_inbound_compression_type, Unset):
            audio_inbound_compression_type = UNSET
        else:
            audio_inbound_compression_type = (
                RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInboundCompressionType.from_dict(
                    _audio_inbound_compression_type
                )
            )

        _speaker_volume = d.pop("speakerVolume", UNSET)
        speaker_volume: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelSpeakerVolume]
        if isinstance(_speaker_volume, Unset):
            speaker_volume = UNSET
        else:
            speaker_volume = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelSpeakerVolume.from_dict(_speaker_volume)

        _microphone_volume = d.pop("microphoneVolume", UNSET)
        microphone_volume: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicrophoneVolume]
        if isinstance(_microphone_volume, Unset):
            microphone_volume = UNSET
        else:
            microphone_volume = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicrophoneVolume.from_dict(
                _microphone_volume
            )

        _noisereduce = d.pop("noisereduce", UNSET)
        noisereduce: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelNoisereduce]
        if isinstance(_noisereduce, Unset):
            noisereduce = UNSET
        else:
            noisereduce = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelNoisereduce.from_dict(_noisereduce)

        _audio_bit_rate = d.pop("audioBitRate", UNSET)
        audio_bit_rate: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioBitRate]
        if isinstance(_audio_bit_rate, Unset):
            audio_bit_rate = UNSET
        else:
            audio_bit_rate = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioBitRate.from_dict(_audio_bit_rate)

        _audio_input_type = d.pop("audioInputType", UNSET)
        audio_input_type: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInputType]
        if isinstance(_audio_input_type, Unset):
            audio_input_type = UNSET
        else:
            audio_input_type = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAudioInputType.from_dict(
                _audio_input_type
            )

        _associate_video_inputs = d.pop("associateVideoInputs", UNSET)
        associate_video_inputs: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs]
        if isinstance(_associate_video_inputs, Unset):
            associate_video_inputs = UNSET
        else:
            associate_video_inputs = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs.from_dict(
                _associate_video_inputs
            )

        _line_out_forbidden = d.pop("lineOutForbidden", UNSET)
        line_out_forbidden: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelLineOutForbidden]
        if isinstance(_line_out_forbidden, Unset):
            line_out_forbidden = UNSET
        else:
            line_out_forbidden = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelLineOutForbidden.from_dict(
                _line_out_forbidden
            )

        _mic_in_forbidden = d.pop("micInForbidden", UNSET)
        mic_in_forbidden: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicInForbidden]
        if isinstance(_mic_in_forbidden, Unset):
            mic_in_forbidden = UNSET
        else:
            mic_in_forbidden = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelMicInForbidden.from_dict(
                _mic_in_forbidden
            )

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_two_way_audio_channel_two_way_audio_channel = cls(
            id=id,
            enabled=enabled,
            audio_compression_type=audio_compression_type,
            audio_inbound_compression_type=audio_inbound_compression_type,
            speaker_volume=speaker_volume,
            microphone_volume=microphone_volume,
            noisereduce=noisereduce,
            audio_bit_rate=audio_bit_rate,
            audio_input_type=audio_input_type,
            associate_video_inputs=associate_video_inputs,
            line_out_forbidden=line_out_forbidden,
            mic_in_forbidden=mic_in_forbidden,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_two_way_audio_channel_two_way_audio_channel.additional_properties = d
        return root_type_for_xml_two_way_audio_channel_two_way_audio_channel

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
