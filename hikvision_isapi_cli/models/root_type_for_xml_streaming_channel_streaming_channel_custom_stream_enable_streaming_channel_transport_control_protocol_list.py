from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_control_protocol_list_control_protocol import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportControlProtocolListControlProtocol,
    )


T = TypeVar(
    "T",
    bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportControlProtocolList",
)


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportControlProtocolList:
    """
    Attributes:
        control_protocol (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelT
            ransportControlProtocolListControlProtocol]):
    """

    control_protocol: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportControlProtocolListControlProtocol",
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        control_protocol: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.control_protocol, Unset):
            control_protocol = self.control_protocol.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_protocol is not UNSET:
            field_dict["ControlProtocol"] = control_protocol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_control_protocol_list_control_protocol import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportControlProtocolListControlProtocol,
        )

        d = src_dict.copy()
        _control_protocol = d.pop("ControlProtocol", UNSET)
        control_protocol: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportControlProtocolListControlProtocol,
        ]
        if isinstance(_control_protocol, Unset):
            control_protocol = UNSET
        else:
            control_protocol = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportControlProtocolListControlProtocol.from_dict(
                _control_protocol
            )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_control_protocol_list = cls(
            control_protocol=control_protocol,
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_control_protocol_list.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_control_protocol_list

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
