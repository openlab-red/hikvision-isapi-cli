from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_network_interface_network_interface_active_multicast import (
        RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast,
    )
    from ..models.root_type_for_xml_network_interface_network_interface_ethernet_port_list import (
        RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList,
    )
    from ..models.root_type_for_xml_network_interface_network_interface_mac_address import (
        RootTypeForXMLNetworkInterfaceNetworkInterfaceMacAddress,
    )


T = TypeVar("T", bound="RootTypeForXMLNetworkInterfaceNetworkInterface")


@attr.s(auto_attribs=True)
class RootTypeForXMLNetworkInterfaceNetworkInterface:
    """
    Attributes:
        id (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        wireless (Union[Unset, str]):
        discovery (Union[Unset, str]):
        link (Union[Unset, str]):
        default_connection (Union[Unset, str]):
        active_multicast (Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast]):
        mac_address (Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceMacAddress]):
        ethernet_port_list (Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    wireless: Union[Unset, str] = UNSET
    discovery: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    default_connection: Union[Unset, str] = UNSET
    active_multicast: Union[Unset, "RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast"] = UNSET
    mac_address: Union[Unset, "RootTypeForXMLNetworkInterfaceNetworkInterfaceMacAddress"] = UNSET
    ethernet_port_list: Union[Unset, "RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList"] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        ip_address = self.ip_address
        wireless = self.wireless
        discovery = self.discovery
        link = self.link
        default_connection = self.default_connection
        active_multicast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_multicast, Unset):
            active_multicast = self.active_multicast.to_dict()

        mac_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mac_address, Unset):
            mac_address = self.mac_address.to_dict()

        ethernet_port_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ethernet_port_list, Unset):
            ethernet_port_list = self.ethernet_port_list.to_dict()

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["IPAddress"] = ip_address
        if wireless is not UNSET:
            field_dict["Wireless"] = wireless
        if discovery is not UNSET:
            field_dict["Discovery"] = discovery
        if link is not UNSET:
            field_dict["Link"] = link
        if default_connection is not UNSET:
            field_dict["defaultConnection"] = default_connection
        if active_multicast is not UNSET:
            field_dict["ActiveMulticast"] = active_multicast
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if ethernet_port_list is not UNSET:
            field_dict["EthernetPortList"] = ethernet_port_list
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_network_interface_network_interface_active_multicast import (
            RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast,
        )
        from ..models.root_type_for_xml_network_interface_network_interface_ethernet_port_list import (
            RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList,
        )
        from ..models.root_type_for_xml_network_interface_network_interface_mac_address import (
            RootTypeForXMLNetworkInterfaceNetworkInterfaceMacAddress,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        ip_address = d.pop("IPAddress", UNSET)

        wireless = d.pop("Wireless", UNSET)

        discovery = d.pop("Discovery", UNSET)

        link = d.pop("Link", UNSET)

        default_connection = d.pop("defaultConnection", UNSET)

        _active_multicast = d.pop("ActiveMulticast", UNSET)
        active_multicast: Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast]
        if isinstance(_active_multicast, Unset):
            active_multicast = UNSET
        else:
            active_multicast = RootTypeForXMLNetworkInterfaceNetworkInterfaceActiveMulticast.from_dict(
                _active_multicast
            )

        _mac_address = d.pop("macAddress", UNSET)
        mac_address: Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceMacAddress]
        if isinstance(_mac_address, Unset):
            mac_address = UNSET
        else:
            mac_address = RootTypeForXMLNetworkInterfaceNetworkInterfaceMacAddress.from_dict(_mac_address)

        _ethernet_port_list = d.pop("EthernetPortList", UNSET)
        ethernet_port_list: Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList]
        if isinstance(_ethernet_port_list, Unset):
            ethernet_port_list = UNSET
        else:
            ethernet_port_list = RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList.from_dict(
                _ethernet_port_list
            )

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_network_interface_network_interface = cls(
            id=id,
            ip_address=ip_address,
            wireless=wireless,
            discovery=discovery,
            link=link,
            default_connection=default_connection,
            active_multicast=active_multicast,
            mac_address=mac_address,
            ethernet_port_list=ethernet_port_list,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_network_interface_network_interface.additional_properties = d
        return root_type_for_xml_network_interface_network_interface

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
