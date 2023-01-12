from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_transport_control_protocol_list_control_protocol_item import (
        RootTypeForXMLStreamingChannelTransportControlProtocolListControlProtocolItem,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelTransportControlProtocolList")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelTransportControlProtocolList:
    """
    Attributes:
        control_protocol (Union[Unset,
            List['RootTypeForXMLStreamingChannelTransportControlProtocolListControlProtocolItem']]):
    """

    control_protocol: Union[
        Unset, List["RootTypeForXMLStreamingChannelTransportControlProtocolListControlProtocolItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        control_protocol: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.control_protocol, Unset):
            control_protocol = []
            for control_protocol_item_data in self.control_protocol:
                control_protocol_item = control_protocol_item_data.to_dict()

                control_protocol.append(control_protocol_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_protocol is not UNSET:
            field_dict["ControlProtocol"] = control_protocol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_transport_control_protocol_list_control_protocol_item import (
            RootTypeForXMLStreamingChannelTransportControlProtocolListControlProtocolItem,
        )

        d = src_dict.copy()
        control_protocol = []
        _control_protocol = d.pop("ControlProtocol", UNSET)
        for control_protocol_item_data in _control_protocol or []:
            control_protocol_item = (
                RootTypeForXMLStreamingChannelTransportControlProtocolListControlProtocolItem.from_dict(
                    control_protocol_item_data
                )
            )

            control_protocol.append(control_protocol_item)

        root_type_for_xml_streaming_channel_transport_control_protocol_list = cls(
            control_protocol=control_protocol,
        )

        root_type_for_xml_streaming_channel_transport_control_protocol_list.additional_properties = d
        return root_type_for_xml_streaming_channel_transport_control_protocol_list

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
