from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_network_interface_network_interface_ethernet_port_list_ethernet_port import (
        RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort,
    )


T = TypeVar("T", bound="RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList")


@attr.s(auto_attribs=True)
class RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortList:
    """
    Attributes:
        ethernet_port (Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort]):
        size (Union[Unset, str]):
    """

    ethernet_port: Union[Unset, "RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort"] = UNSET
    size: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ethernet_port: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ethernet_port, Unset):
            ethernet_port = self.ethernet_port.to_dict()

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ethernet_port is not UNSET:
            field_dict["EthernetPort"] = ethernet_port
        if size is not UNSET:
            field_dict["@size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_network_interface_network_interface_ethernet_port_list_ethernet_port import (
            RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort,
        )

        d = src_dict.copy()
        _ethernet_port = d.pop("EthernetPort", UNSET)
        ethernet_port: Union[Unset, RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort]
        if isinstance(_ethernet_port, Unset):
            ethernet_port = UNSET
        else:
            ethernet_port = RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort.from_dict(
                _ethernet_port
            )

        size = d.pop("@size", UNSET)

        root_type_for_xml_network_interface_network_interface_ethernet_port_list = cls(
            ethernet_port=ethernet_port,
            size=size,
        )

        root_type_for_xml_network_interface_network_interface_ethernet_port_list.additional_properties = d
        return root_type_for_xml_network_interface_network_interface_ethernet_port_list

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
