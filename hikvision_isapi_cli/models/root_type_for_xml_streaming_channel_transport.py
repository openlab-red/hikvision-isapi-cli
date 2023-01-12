from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_transport_control_protocol_list import (
        RootTypeForXMLStreamingChannelTransportControlProtocolList,
    )
    from ..models.root_type_for_xml_streaming_channel_transport_security import (
        RootTypeForXMLStreamingChannelTransportSecurity,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelTransport")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelTransport:
    """
    Attributes:
        control_protocol_list (Union[Unset, RootTypeForXMLStreamingChannelTransportControlProtocolList]):
        security (Union[Unset, RootTypeForXMLStreamingChannelTransportSecurity]):
    """

    control_protocol_list: Union[Unset, "RootTypeForXMLStreamingChannelTransportControlProtocolList"] = UNSET
    security: Union[Unset, "RootTypeForXMLStreamingChannelTransportSecurity"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        control_protocol_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.control_protocol_list, Unset):
            control_protocol_list = self.control_protocol_list.to_dict()

        security: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.security, Unset):
            security = self.security.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_protocol_list is not UNSET:
            field_dict["ControlProtocolList"] = control_protocol_list
        if security is not UNSET:
            field_dict["Security"] = security

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_transport_control_protocol_list import (
            RootTypeForXMLStreamingChannelTransportControlProtocolList,
        )
        from ..models.root_type_for_xml_streaming_channel_transport_security import (
            RootTypeForXMLStreamingChannelTransportSecurity,
        )

        d = src_dict.copy()
        _control_protocol_list = d.pop("ControlProtocolList", UNSET)
        control_protocol_list: Union[Unset, RootTypeForXMLStreamingChannelTransportControlProtocolList]
        if isinstance(_control_protocol_list, Unset):
            control_protocol_list = UNSET
        else:
            control_protocol_list = RootTypeForXMLStreamingChannelTransportControlProtocolList.from_dict(
                _control_protocol_list
            )

        _security = d.pop("Security", UNSET)
        security: Union[Unset, RootTypeForXMLStreamingChannelTransportSecurity]
        if isinstance(_security, Unset):
            security = UNSET
        else:
            security = RootTypeForXMLStreamingChannelTransportSecurity.from_dict(_security)

        root_type_for_xml_streaming_channel_transport = cls(
            control_protocol_list=control_protocol_list,
            security=security,
        )

        root_type_for_xml_streaming_channel_transport.additional_properties = d
        return root_type_for_xml_streaming_channel_transport

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
