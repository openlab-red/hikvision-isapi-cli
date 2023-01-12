from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel import (
        RootTypeForXMLStreamingChannelStreamingChannel,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannel")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannel:
    """StreamingChannel message in XML format

    Example:
        {'StreamingChannel': {'id': '', 'channelName': '', 'enabled': '', 'Transport': {'maxPacketSize': '',
            'audioPacketLength': '', 'audioInboundPacketLength': '', 'audioInboundPortNo': '', 'videoSourcePortNo': '',
            'audioSourcePortNo': '', 'ControlProtocolList': {'ControlProtocol': {'streamingTransport': {}}}, 'Unicast':
            {'enabled': '', 'interfaceID': '', 'rtpTransportType': {}}, 'Multicast': {'enabled': '', 'userTriggerThreshold':
            '', 'destIPAddress': '', 'videoDestPortNo': '', 'audioDestPortNo': '', 'destIPv6Address': '', 'ttl': '',
            'activeMulticastEnabled': {}, 'packagingFormat': '', 'FecInfo': {'fecRatio': {}, 'fecDestPortNo': {}}},
            'Security': {'enabled': '', 'certificateType': '', 'SecurityAlgorithm': {'algorithmType': ''}}, 'SRTPMulticast':
            {'SRTPVideoDestPortNo': '', 'SRTPAudioDestPortNo': ''}}, 'Video': {'enabled': '', 'videoInputChannelID': {},
            'videoCodecType': {}, 'videoResolutionWidth': {}, 'videoResolutionHeight': {}, 'videoQualityControlType': {},
            'constantBitRate': {}, 'vbrUpperCap': {}, 'vbrLowerCap': {}, 'maxFrameRate': {}, 'keyFrameInterval': '',
            'rotationDegree': '', 'mirrorEnabled': '', 'snapShotImageType': '', 'Mpeg4Profile': '', 'H264Profile': '',
            'SVACProfile': '', 'GovLength': '', 'SVC': {'enabled': '', 'SVCMode': ''}, 'smoothing': '', 'SmartCodec':
            {'enabled': ''}, 'vbrAverageCap': '', 'IntelligentInfoDisplayMethod': {}}, 'Audio': {'enabled': '',
            'audioInputChannelID': '', 'audioCompressionType': {}, 'audioInboundCompressionType': {}, 'audioBitRate': '',
            'audioSamplingRate': '', 'audioResolution': '', 'VoiceChanger': {'enabled': '', 'level': ''}}, 'enableCABAC':
            '', 'subStreamRecStatus': '', 'customStreamEnable': {'StreamingChannel': {'id': '', 'channelName': '',
            'enabled': '', 'Transport': {'maxPacketSize': '', 'audioPacketLength': '', 'audioInboundPacketLength': '',
            'audioInboundPortNo': '', 'videoSourcePortNo': '', 'audioSourcePortNo': '', 'ControlProtocolList':
            {'ControlProtocol': {'streamingTransport': {}}}, 'Unicast': {'enabled': '', 'interfaceID': '',
            'rtpTransportType': {}}, 'Multicast': {'enabled': '', 'userTriggerThreshold': '', 'destIPAddress': '',
            'videoDestPortNo': '', 'audioDestPortNo': '', 'destIPv6Address': '', 'ttl': '', 'activeMulticastEnabled': {},
            'packagingFormat': '', 'FecInfo': {'fecRatio': {}, 'fecDestPortNo': {}}}, 'Security': {'enabled': '',
            'certificateType': '', 'SecurityAlgorithm': {'algorithmType': ''}}, 'SRTPMulticast': {'SRTPVideoDestPortNo': '',
            'SRTPAudioDestPortNo': ''}}, 'Video': {'enabled': '', 'videoInputChannelID': {}, 'videoCodecType': {},
            'videoResolutionWidth': {}, 'videoResolutionHeight': {}, 'videoQualityControlType': {}, 'constantBitRate': {},
            'vbrUpperCap': {}, 'vbrLowerCap': {}, 'maxFrameRate': {}, 'keyFrameInterval': '', 'rotationDegree': '',
            'mirrorEnabled': '', 'snapShotImageType': '', 'Mpeg4Profile': '', 'H264Profile': '', 'SVACProfile': '',
            'GovLength': '', 'SVC': {'enabled': '', 'SVCMode': ''}, 'smoothing': '', 'SmartCodec': {'enabled': ''},
            'vbrAverageCap': '', 'IntelligentInfoDisplayMethod': {}}, 'Audio': {'enabled': '', 'audioInputChannelID': '',
            'audioCompressionType': {}, 'audioInboundCompressionType': {}, 'audioBitRate': '', 'audioSamplingRate': '',
            'audioResolution': '', 'VoiceChanger': {'enabled': '', 'level': ''}}, 'enableCABAC': '', 'subStreamRecStatus':
            '', 'customStreamEnable': '', '@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}, '@version':
            '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        streaming_channel (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannel]):
    """

    streaming_channel: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannel"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        streaming_channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.streaming_channel, Unset):
            streaming_channel = self.streaming_channel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if streaming_channel is not UNSET:
            field_dict["StreamingChannel"] = streaming_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel import (
            RootTypeForXMLStreamingChannelStreamingChannel,
        )

        d = src_dict.copy()
        _streaming_channel = d.pop("StreamingChannel", UNSET)
        streaming_channel: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannel]
        if isinstance(_streaming_channel, Unset):
            streaming_channel = UNSET
        else:
            streaming_channel = RootTypeForXMLStreamingChannelStreamingChannel.from_dict(_streaming_channel)

        root_type_for_xml_streaming_channel = cls(
            streaming_channel=streaming_channel,
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
