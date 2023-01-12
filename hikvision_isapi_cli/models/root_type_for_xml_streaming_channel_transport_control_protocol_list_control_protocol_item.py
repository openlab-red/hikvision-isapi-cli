from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLStreamingChannelTransportControlProtocolListControlProtocolItem")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelTransportControlProtocolListControlProtocolItem:
    """
    Attributes:
        streaming_transport (Union[Unset, str]):
    """

    streaming_transport: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        streaming_transport = self.streaming_transport

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if streaming_transport is not UNSET:
            field_dict["streamingTransport"] = streaming_transport

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        streaming_transport = d.pop("streamingTransport", UNSET)

        root_type_for_xml_streaming_channel_transport_control_protocol_list_control_protocol_item = cls(
            streaming_transport=streaming_transport,
        )

        root_type_for_xml_streaming_channel_transport_control_protocol_list_control_protocol_item.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_transport_control_protocol_list_control_protocol_item

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
