from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_security_security_algorithm import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelTransportSecurity:
    """
    Attributes:
        enabled (Union[Unset, str]):
        certificate_type (Union[Unset, str]):
        security_algorithm (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm]):
    """

    enabled: Union[Unset, str] = UNSET
    certificate_type: Union[Unset, str] = UNSET
    security_algorithm: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        certificate_type = self.certificate_type
        security_algorithm: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.security_algorithm, Unset):
            security_algorithm = self.security_algorithm.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if certificate_type is not UNSET:
            field_dict["certificateType"] = certificate_type
        if security_algorithm is not UNSET:
            field_dict["SecurityAlgorithm"] = security_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_security_security_algorithm import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        certificate_type = d.pop("certificateType", UNSET)

        _security_algorithm = d.pop("SecurityAlgorithm", UNSET)
        security_algorithm: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm
        ]
        if isinstance(_security_algorithm, Unset):
            security_algorithm = UNSET
        else:
            security_algorithm = (
                RootTypeForXMLStreamingChannelStreamingChannelTransportSecuritySecurityAlgorithm.from_dict(
                    _security_algorithm
                )
            )

        root_type_for_xml_streaming_channel_streaming_channel_transport_security = cls(
            enabled=enabled,
            certificate_type=certificate_type,
            security_algorithm=security_algorithm,
        )

        root_type_for_xml_streaming_channel_streaming_channel_transport_security.additional_properties = d
        return root_type_for_xml_streaming_channel_streaming_channel_transport_security

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
