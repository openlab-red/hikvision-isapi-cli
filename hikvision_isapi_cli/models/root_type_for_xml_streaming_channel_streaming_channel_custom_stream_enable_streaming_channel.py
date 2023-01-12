from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransport,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel:
    """
    Attributes:
        id (Union[Unset, str]):
        channel_name (Union[Unset, str]):
        enabled (Union[Unset, str]):
        transport (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransport]):
        video (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo]):
        audio (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio]):
        enable_cabac (Union[Unset, str]):
        sub_stream_rec_status (Union[Unset, str]):
        custom_stream_enable (Union[Unset, str]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    channel_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    transport: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransport"
    ] = UNSET
    video: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo"] = UNSET
    audio: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio"] = UNSET
    enable_cabac: Union[Unset, str] = UNSET
    sub_stream_rec_status: Union[Unset, str] = UNSET
    custom_stream_enable: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        channel_name = self.channel_name
        enabled = self.enabled
        transport: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.to_dict()

        video: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        audio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.to_dict()

        enable_cabac = self.enable_cabac
        sub_stream_rec_status = self.sub_stream_rec_status
        custom_stream_enable = self.custom_stream_enable
        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if channel_name is not UNSET:
            field_dict["channelName"] = channel_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if transport is not UNSET:
            field_dict["Transport"] = transport
        if video is not UNSET:
            field_dict["Video"] = video
        if audio is not UNSET:
            field_dict["Audio"] = audio
        if enable_cabac is not UNSET:
            field_dict["enableCABAC"] = enable_cabac
        if sub_stream_rec_status is not UNSET:
            field_dict["subStreamRecStatus"] = sub_stream_rec_status
        if custom_stream_enable is not UNSET:
            field_dict["customStreamEnable"] = custom_stream_enable
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_audio import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransport,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        channel_name = d.pop("channelName", UNSET)

        enabled = d.pop("enabled", UNSET)

        _transport = d.pop("Transport", UNSET)
        transport: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransport
        ]
        if isinstance(_transport, Unset):
            transport = UNSET
        else:
            transport = (
                RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransport.from_dict(
                    _transport
                )
            )

        _video = d.pop("Video", UNSET)
        video: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo]
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo.from_dict(
                _video
            )

        _audio = d.pop("Audio", UNSET)
        audio: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio]
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelAudio.from_dict(
                _audio
            )

        enable_cabac = d.pop("enableCABAC", UNSET)

        sub_stream_rec_status = d.pop("subStreamRecStatus", UNSET)

        custom_stream_enable = d.pop("customStreamEnable", UNSET)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel = cls(
            id=id,
            channel_name=channel_name,
            enabled=enabled,
            transport=transport,
            video=video,
            audio=audio,
            enable_cabac=enable_cabac,
            sub_stream_rec_status=sub_stream_rec_status,
            custom_stream_enable=custom_stream_enable,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel

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
