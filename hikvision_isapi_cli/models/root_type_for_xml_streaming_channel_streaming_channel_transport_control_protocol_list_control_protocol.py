from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_control_protocol_list_control_protocol_streaming_transport import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocolStreamingTransport,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocol")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocol:
    """
    Attributes:
        streaming_transport (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocolStreamingTransport]):
    """

    streaming_transport: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocolStreamingTransport",
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        streaming_transport: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.streaming_transport, Unset):
            streaming_transport = self.streaming_transport.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if streaming_transport is not UNSET:
            field_dict["streamingTransport"] = streaming_transport

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_control_protocol_list_control_protocol_streaming_transport import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocolStreamingTransport,
        )

        d = src_dict.copy()
        _streaming_transport = d.pop("streamingTransport", UNSET)
        streaming_transport: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocolStreamingTransport,
        ]
        if isinstance(_streaming_transport, Unset):
            streaming_transport = UNSET
        else:
            streaming_transport = RootTypeForXMLStreamingChannelStreamingChannelTransportControlProtocolListControlProtocolStreamingTransport.from_dict(
                _streaming_transport
            )

        root_type_for_xml_streaming_channel_streaming_channel_transport_control_protocol_list_control_protocol = cls(
            streaming_transport=streaming_transport,
        )

        root_type_for_xml_streaming_channel_streaming_channel_transport_control_protocol_list_control_protocol.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_transport_control_protocol_list_control_protocol

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
