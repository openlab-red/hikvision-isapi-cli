from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm:
    """
    Attributes:
        algorithm_type (Union[Unset, str]):
    """

    algorithm_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        algorithm_type = self.algorithm_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm_type is not UNSET:
            field_dict["algorithmType"] = algorithm_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        algorithm_type = d.pop("algorithmType", UNSET)

        root_type_for_xml_streaming_channel_streaming_channel_transport_security_security_algorithm = cls(
            algorithm_type=algorithm_type,
        )

        root_type_for_xml_streaming_channel_streaming_channel_transport_security_security_algorithm.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_transport_security_security_algorithm

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
