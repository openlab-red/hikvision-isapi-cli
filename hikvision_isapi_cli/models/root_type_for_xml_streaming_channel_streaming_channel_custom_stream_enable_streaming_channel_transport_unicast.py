from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_unicast_rtp_transport_type import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportUnicastRtpTransportType,
    )


T = TypeVar(
    "T", bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportUnicast"
)


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportUnicast:
    """
    Attributes:
        enabled (Union[Unset, str]):
        interface_id (Union[Unset, str]):
        rtp_transport_type (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChanne
            lTransportUnicastRtpTransportType]):
    """

    enabled: Union[Unset, str] = UNSET
    interface_id: Union[Unset, str] = UNSET
    rtp_transport_type: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportUnicastRtpTransportType",
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        interface_id = self.interface_id
        rtp_transport_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rtp_transport_type, Unset):
            rtp_transport_type = self.rtp_transport_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if interface_id is not UNSET:
            field_dict["interfaceID"] = interface_id
        if rtp_transport_type is not UNSET:
            field_dict["rtpTransportType"] = rtp_transport_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_unicast_rtp_transport_type import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportUnicastRtpTransportType,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        interface_id = d.pop("interfaceID", UNSET)

        _rtp_transport_type = d.pop("rtpTransportType", UNSET)
        rtp_transport_type: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportUnicastRtpTransportType,
        ]
        if isinstance(_rtp_transport_type, Unset):
            rtp_transport_type = UNSET
        else:
            rtp_transport_type = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportUnicastRtpTransportType.from_dict(
                _rtp_transport_type
            )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_unicast = cls(
            enabled=enabled,
            interface_id=interface_id,
            rtp_transport_type=rtp_transport_type,
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_unicast.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_unicast

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
