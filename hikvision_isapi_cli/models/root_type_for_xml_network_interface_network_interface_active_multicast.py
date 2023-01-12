from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_network_interface_network_interface_active_multicast_port import (
        RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastPort,
    )
    from ..models.root_type_for_xml_network_interface_network_interface_active_multicast_stream_id import (
        RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastStreamID,
    )


T = TypeVar("T", bound="RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast")


@attr.s(auto_attribs=True)
class RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast:
    """
    Attributes:
        enabled (Union[Unset, str]):
        stream_id (Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastStreamID]):
        ip_v4_address (Union[Unset, str]):
        ip_v6_address (Union[Unset, str]):
        port (Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastPort]):
    """

    enabled: Union[Unset, str] = UNSET
    stream_id: Union[Unset, "RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastStreamID"] = UNSET
    ip_v4_address: Union[Unset, str] = UNSET
    ip_v6_address: Union[Unset, str] = UNSET
    port: Union[Unset, "RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastPort"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        stream_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stream_id, Unset):
            stream_id = self.stream_id.to_dict()

        ip_v4_address = self.ip_v4_address
        ip_v6_address = self.ip_v6_address
        port: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if stream_id is not UNSET:
            field_dict["streamID"] = stream_id
        if ip_v4_address is not UNSET:
            field_dict["ipV4Address"] = ip_v4_address
        if ip_v6_address is not UNSET:
            field_dict["ipV6Address"] = ip_v6_address
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_network_interface_network_interface_active_multicast_port import (
            RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastPort,
        )
        from ..models.root_type_for_xml_network_interface_network_interface_active_multicast_stream_id import (
            RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastStreamID,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        _stream_id = d.pop("streamID", UNSET)
        stream_id: Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastStreamID]
        if isinstance(_stream_id, Unset):
            stream_id = UNSET
        else:
            stream_id = RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastStreamID.from_dict(_stream_id)

        ip_v4_address = d.pop("ipV4Address", UNSET)

        ip_v6_address = d.pop("ipV6Address", UNSET)

        _port = d.pop("port", UNSET)
        port: Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastPort]
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticastPort.from_dict(_port)

        root_type_for_xml_network_interface_network_interface_active_multicast = cls(
            enabled=enabled,
            stream_id=stream_id,
            ip_v4_address=ip_v4_address,
            ip_v6_address=ip_v6_address,
            port=port,
        )

        root_type_for_xml_network_interface_network_interface_active_multicast.additional_properties = d
        return root_type_for_xml_network_interface_network_interface_active_multicast

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
