from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_network_interface_list_network_interface_list import (
        RootTypeForXMLNetworkInterfaceListNetworkInterfaceList,
    )


T = TypeVar("T", bound="RootTypeForXMLNetworkInterfaceList")


@attr.s(auto_attribs=True)
class RootTypeForXMLNetworkInterfaceList:
    """NetworkInterfaceList message in XML format

    Example:
        {'NetworkInterfaceList': {'NetworkInterface': [], '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        network_interface_list (Union[Unset, RootTypeForXMLNetworkInterfaceListNetworkInterfaceList]):
    """

    network_interface_list: Union[Unset, "RootTypeForXMLNetworkInterfaceListNetworkInterfaceList"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network_interface_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.network_interface_list, Unset):
            network_interface_list = self.network_interface_list.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_interface_list is not UNSET:
            field_dict["NetworkInterfaceList"] = network_interface_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_network_interface_list_network_interface_list import (
            RootTypeForXMLNetworkInterfaceListNetworkInterfaceList,
        )

        d = src_dict.copy()
        _network_interface_list = d.pop("NetworkInterfaceList", UNSET)
        network_interface_list: Union[Unset, RootTypeForXMLNetworkInterfaceListNetworkInterfaceList]
        if isinstance(_network_interface_list, Unset):
            network_interface_list = UNSET
        else:
            network_interface_list = RootTypeForXMLNetworkInterfaceListNetworkInterfaceList.from_dict(
                _network_interface_list
            )

        root_type_for_xml_network_interface_list = cls(
            network_interface_list=network_interface_list,
        )

        root_type_for_xml_network_interface_list.additional_properties = d
        return root_type_for_xml_network_interface_list

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
