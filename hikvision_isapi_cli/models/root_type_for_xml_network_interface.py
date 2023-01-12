from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_network_interface_network_interface import (
        RootTypeForXMLNetworkInterfaceNetworkInterface,
    )


T = TypeVar("T", bound="RootTypeForXMLNetworkInterface")


@attr.s(auto_attribs=True)
class RootTypeForXMLNetworkInterface:
    """NetworkInterface message in XML format

    Example:
        {'NetworkInterface': {'id': '', 'IPAddress': '', 'Wireless': '', 'Discovery': '', 'Link': '',
            'defaultConnection': '', 'ActiveMulticast': {'enabled': '', 'streamID': {'@opt': 'main'}, 'ipV4Address': '',
            'ipV6Address': '', 'port': {'@min': '', '@max': ''}}, 'macAddress': {'@min': '', '@max': ''},
            'EthernetPortList': {'EthernetPort': {'id': '', 'MACAddress': '', 'status': '', 'speed': ''}, '@size': '4'},
            '@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        network_interface (Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterface]):
    """

    network_interface: Union[Unset, "RootTypeForXMLNetworkInterfaceNetworkInterface"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network_interface: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.network_interface, Unset):
            network_interface = self.network_interface.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_interface is not UNSET:
            field_dict["NetworkInterface"] = network_interface

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_network_interface_network_interface import (
            RootTypeForXMLNetworkInterfaceNetworkInterface,
        )

        d = src_dict.copy()
        _network_interface = d.pop("NetworkInterface", UNSET)
        network_interface: Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterface]
        if isinstance(_network_interface, Unset):
            network_interface = UNSET
        else:
            network_interface = RootTypeForXMLNetworkInterfaceNetworkInterface.from_dict(_network_interface)

        root_type_for_xml_network_interface = cls(
            network_interface=network_interface,
        )

        root_type_for_xml_network_interface.additional_properties = d
        return root_type_for_xml_network_interface

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
