from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_network_interface import RootTypeForXMLNetworkInterface


T = TypeVar("T", bound="RootTypeForXMLNetworkInterfaceListNetworkInterfaceList")


@attr.s(auto_attribs=True)
class RootTypeForXMLNetworkInterfaceListNetworkInterfaceList:
    """
    Attributes:
        network_interface (Union[Unset, List['RootTypeForXMLNetworkInterface']]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    network_interface: Union[Unset, List["RootTypeForXMLNetworkInterface"]] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network_interface: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.network_interface, Unset):
            network_interface = []
            for network_interface_item_data in self.network_interface:
                network_interface_item = network_interface_item_data.to_dict()

                network_interface.append(network_interface_item)

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_interface is not UNSET:
            field_dict["NetworkInterface"] = network_interface
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_network_interface import RootTypeForXMLNetworkInterface

        d = src_dict.copy()
        network_interface = []
        _network_interface = d.pop("NetworkInterface", UNSET)
        for network_interface_item_data in _network_interface or []:
            network_interface_item = RootTypeForXMLNetworkInterface.from_dict(network_interface_item_data)

            network_interface.append(network_interface_item)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_network_interface_list_network_interface_list = cls(
            network_interface=network_interface,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_network_interface_list_network_interface_list.additional_properties = d
        return root_type_for_xml_network_interface_list_network_interface_list

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
