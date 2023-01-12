from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportSRTPMulticast"
)


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportSRTPMulticast:
    """
    Attributes:
        srtp_video_dest_port_no (Union[Unset, str]):
        srtp_audio_dest_port_no (Union[Unset, str]):
    """

    srtp_video_dest_port_no: Union[Unset, str] = UNSET
    srtp_audio_dest_port_no: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        srtp_video_dest_port_no = self.srtp_video_dest_port_no
        srtp_audio_dest_port_no = self.srtp_audio_dest_port_no

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if srtp_video_dest_port_no is not UNSET:
            field_dict["SRTPVideoDestPortNo"] = srtp_video_dest_port_no
        if srtp_audio_dest_port_no is not UNSET:
            field_dict["SRTPAudioDestPortNo"] = srtp_audio_dest_port_no

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        srtp_video_dest_port_no = d.pop("SRTPVideoDestPortNo", UNSET)

        srtp_audio_dest_port_no = d.pop("SRTPAudioDestPortNo", UNSET)

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_srtp_multicast = cls(
            srtp_video_dest_port_no=srtp_video_dest_port_no,
            srtp_audio_dest_port_no=srtp_audio_dest_port_no,
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_srtp_multicast.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_srtp_multicast

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
