from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort")


@attr.s(auto_attribs=True)
class RootTypeForXMLNetworkInterfaceNetworkInterfaceEthernetPortListEthernetPort:
    """
    Attributes:
        id (Union[Unset, str]):
        mac_address (Union[Unset, str]):
        status (Union[Unset, str]):
        speed (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mac_address = self.mac_address
        status = self.status
        speed = self.speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac_address is not UNSET:
            field_dict["MACAddress"] = mac_address
        if status is not UNSET:
            field_dict["status"] = status
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        mac_address = d.pop("MACAddress", UNSET)

        status = d.pop("status", UNSET)

        speed = d.pop("speed", UNSET)

        root_type_for_xml_network_interface_network_interface_ethernet_port_list_ethernet_port = cls(
            id=id,
            mac_address=mac_address,
            status=status,
            speed=speed,
        )

        root_type_for_xml_network_interface_network_interface_ethernet_port_list_ethernet_port.additional_properties = d
        return root_type_for_xml_network_interface_network_interface_ethernet_port_list_ethernet_port

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
