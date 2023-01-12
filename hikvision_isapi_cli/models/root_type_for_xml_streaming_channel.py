from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_audio import RootTypeForXMLStreamingChannelAudio
    from ..models.root_type_for_xml_streaming_channel_transport import RootTypeForXMLStreamingChannelTransport
    from ..models.root_type_for_xml_streaming_channel_video import RootTypeForXMLStreamingChannelVideo


T = TypeVar("T", bound="RootTypeForXMLStreamingChannel")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannel:
    """StreamingChannel message in XML format

    Example:
        {'id': '101', 'channelName': 'Camera 01', 'enabled': 'true', 'Transport': {'ControlProtocolList':
            {'ControlProtocol': [{'streamingTransport': 'RTSP'}, {'streamingTransport': 'HTTP'}]}, 'Security': {'enabled':
            'true'}}, 'Video': {'enabled': 'true', 'videoInputChannelID': '1', 'videoCodecType': 'H.264', 'videoScanType':
            'progressive', 'videoResolutionWidth': '1280', 'videoResolutionHeight': '720', 'videoQualityControlType': 'VBR',
            'constantBitRate': '2048', 'fixedQuality': '60', 'vbrUpperCap': '2048', 'vbrLowerCap': '32', 'maxFrameRate':
            '2500', 'keyFrameInterval': '2000', 'snapShotImageType': 'JPEG', 'GovLength': '50'}, 'Audio': {'enabled':
            'true', 'audioInputChannelID': '1', 'audioCompressionType': 'G.711ulaw'}}

    Attributes:
        id (Union[Unset, str]):
        channel_name (Union[Unset, str]):
        enabled (Union[Unset, str]):
        transport (Union[Unset, RootTypeForXMLStreamingChannelTransport]):
        video (Union[Unset, RootTypeForXMLStreamingChannelVideo]):
        audio (Union[Unset, RootTypeForXMLStreamingChannelAudio]):
    """

    id: Union[Unset, str] = UNSET
    channel_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    transport: Union[Unset, "RootTypeForXMLStreamingChannelTransport"] = UNSET
    video: Union[Unset, "RootTypeForXMLStreamingChannelVideo"] = UNSET
    audio: Union[Unset, "RootTypeForXMLStreamingChannelAudio"] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_audio import RootTypeForXMLStreamingChannelAudio
        from ..models.root_type_for_xml_streaming_channel_transport import RootTypeForXMLStreamingChannelTransport
        from ..models.root_type_for_xml_streaming_channel_video import RootTypeForXMLStreamingChannelVideo

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        channel_name = d.pop("channelName", UNSET)

        enabled = d.pop("enabled", UNSET)

        _transport = d.pop("Transport", UNSET)
        transport: Union[Unset, RootTypeForXMLStreamingChannelTransport]
        if isinstance(_transport, Unset):
            transport = UNSET
        else:
            transport = RootTypeForXMLStreamingChannelTransport.from_dict(_transport)

        _video = d.pop("Video", UNSET)
        video: Union[Unset, RootTypeForXMLStreamingChannelVideo]
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = RootTypeForXMLStreamingChannelVideo.from_dict(_video)

        _audio = d.pop("Audio", UNSET)
        audio: Union[Unset, RootTypeForXMLStreamingChannelAudio]
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = RootTypeForXMLStreamingChannelAudio.from_dict(_audio)

        root_type_for_xml_streaming_channel = cls(
            id=id,
            channel_name=channel_name,
            enabled=enabled,
            transport=transport,
            video=video,
            audio=audio,
        )

        root_type_for_xml_streaming_channel.additional_properties = d
        return root_type_for_xml_streaming_channel

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
