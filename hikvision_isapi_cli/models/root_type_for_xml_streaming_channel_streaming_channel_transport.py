from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_control_protocol_list import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolList,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_multicast import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_security import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_srtp_multicast import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportSRTPMulticast,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_unicast import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportUnicast,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelTransport")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelTransport:
    """
    Attributes:
        max_packet_size (Union[Unset, str]):
        audio_packet_length (Union[Unset, str]):
        audio_inbound_packet_length (Union[Unset, str]):
        audio_inbound_port_no (Union[Unset, str]):
        video_source_port_no (Union[Unset, str]):
        audio_source_port_no (Union[Unset, str]):
        control_protocol_list (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolList]):
        unicast (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportUnicast]):
        multicast (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast]):
        security (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity]):
        srtp_multicast (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportSRTPMulticast]):
    """

    max_packet_size: Union[Unset, str] = UNSET
    audio_packet_length: Union[Unset, str] = UNSET
    audio_inbound_packet_length: Union[Unset, str] = UNSET
    audio_inbound_port_no: Union[Unset, str] = UNSET
    video_source_port_no: Union[Unset, str] = UNSET
    audio_source_port_no: Union[Unset, str] = UNSET
    control_protocol_list: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolList"
    ] = UNSET
    unicast: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportUnicast"] = UNSET
    multicast: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast"] = UNSET
    security: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity"] = UNSET
    srtp_multicast: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportSRTPMulticast"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_packet_size = self.max_packet_size
        audio_packet_length = self.audio_packet_length
        audio_inbound_packet_length = self.audio_inbound_packet_length
        audio_inbound_port_no = self.audio_inbound_port_no
        video_source_port_no = self.video_source_port_no
        audio_source_port_no = self.audio_source_port_no
        control_protocol_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.control_protocol_list, Unset):
            control_protocol_list = self.control_protocol_list.to_dict()

        unicast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unicast, Unset):
            unicast = self.unicast.to_dict()

        multicast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.multicast, Unset):
            multicast = self.multicast.to_dict()

        security: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.security, Unset):
            security = self.security.to_dict()

        srtp_multicast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.srtp_multicast, Unset):
            srtp_multicast = self.srtp_multicast.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_packet_size is not UNSET:
            field_dict["maxPacketSize"] = max_packet_size
        if audio_packet_length is not UNSET:
            field_dict["audioPacketLength"] = audio_packet_length
        if audio_inbound_packet_length is not UNSET:
            field_dict["audioInboundPacketLength"] = audio_inbound_packet_length
        if audio_inbound_port_no is not UNSET:
            field_dict["audioInboundPortNo"] = audio_inbound_port_no
        if video_source_port_no is not UNSET:
            field_dict["videoSourcePortNo"] = video_source_port_no
        if audio_source_port_no is not UNSET:
            field_dict["audioSourcePortNo"] = audio_source_port_no
        if control_protocol_list is not UNSET:
            field_dict["ControlProtocolList"] = control_protocol_list
        if unicast is not UNSET:
            field_dict["Unicast"] = unicast
        if multicast is not UNSET:
            field_dict["Multicast"] = multicast
        if security is not UNSET:
            field_dict["Security"] = security
        if srtp_multicast is not UNSET:
            field_dict["SRTPMulticast"] = srtp_multicast

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_control_protocol_list import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolList,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_multicast import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_security import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_srtp_multicast import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportSRTPMulticast,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_unicast import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportUnicast,
        )

        d = src_dict.copy()
        max_packet_size = d.pop("maxPacketSize", UNSET)

        audio_packet_length = d.pop("audioPacketLength", UNSET)

        audio_inbound_packet_length = d.pop("audioInboundPacketLength", UNSET)

        audio_inbound_port_no = d.pop("audioInboundPortNo", UNSET)

        video_source_port_no = d.pop("videoSourcePortNo", UNSET)

        audio_source_port_no = d.pop("audioSourcePortNo", UNSET)

        _control_protocol_list = d.pop("ControlProtocolList", UNSET)
        control_protocol_list: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolList]
        if isinstance(_control_protocol_list, Unset):
            control_protocol_list = UNSET
        else:
            control_protocol_list = (
                RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolList.from_dict(
                    _control_protocol_list
                )
            )

        _unicast = d.pop("Unicast", UNSET)
        unicast: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportUnicast]
        if isinstance(_unicast, Unset):
            unicast = UNSET
        else:
            unicast = RootTypeForXMLStreamingChannelStreamingChannelTransportUnicast.from_dict(_unicast)

        _multicast = d.pop("Multicast", UNSET)
        multicast: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast]
        if isinstance(_multicast, Unset):
            multicast = UNSET
        else:
            multicast = RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast.from_dict(_multicast)

        _security = d.pop("Security", UNSET)
        security: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity]
        if isinstance(_security, Unset):
            security = UNSET
        else:
            security = RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity.from_dict(_security)

        _srtp_multicast = d.pop("SRTPMulticast", UNSET)
        srtp_multicast: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportSRTPMulticast]
        if isinstance(_srtp_multicast, Unset):
            srtp_multicast = UNSET
        else:
            srtp_multicast = RootTypeForXMLStreamingChannelStreamingChannelTransportSRTPMulticast.from_dict(
                _srtp_multicast
            )

        root_type_for_xml_streaming_channel_streaming_channel_transport = cls(
            max_packet_size=max_packet_size,
            audio_packet_length=audio_packet_length,
            audio_inbound_packet_length=audio_inbound_packet_length,
            audio_inbound_port_no=audio_inbound_port_no,
            video_source_port_no=video_source_port_no,
            audio_source_port_no=audio_source_port_no,
            control_protocol_list=control_protocol_list,
            unicast=unicast,
            multicast=multicast,
            security=security,
            srtp_multicast=srtp_multicast,
        )

        root_type_for_xml_streaming_channel_streaming_channel_transport.additional_properties = d
        return root_type_for_xml_streaming_channel_streaming_channel_transport

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
