from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_multicast_active_multicast_enabled import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastActiveMulticastEnabled,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_multicast_fec_info import (
        RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastFecInfo,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelTransportMulticast:
    """
    Attributes:
        enabled (Union[Unset, str]):
        user_trigger_threshold (Union[Unset, str]):
        dest_ip_address (Union[Unset, str]):
        video_dest_port_no (Union[Unset, str]):
        audio_dest_port_no (Union[Unset, str]):
        dest_i_pv_6_address (Union[Unset, str]):
        ttl (Union[Unset, str]):
        active_multicast_enabled (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastActiveMulticastEnabled]):
        packaging_format (Union[Unset, str]):
        fec_info (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastFecInfo]):
    """

    enabled: Union[Unset, str] = UNSET
    user_trigger_threshold: Union[Unset, str] = UNSET
    dest_ip_address: Union[Unset, str] = UNSET
    video_dest_port_no: Union[Unset, str] = UNSET
    audio_dest_port_no: Union[Unset, str] = UNSET
    dest_i_pv_6_address: Union[Unset, str] = UNSET
    ttl: Union[Unset, str] = UNSET
    active_multicast_enabled: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastActiveMulticastEnabled"
    ] = UNSET
    packaging_format: Union[Unset, str] = UNSET
    fec_info: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastFecInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        user_trigger_threshold = self.user_trigger_threshold
        dest_ip_address = self.dest_ip_address
        video_dest_port_no = self.video_dest_port_no
        audio_dest_port_no = self.audio_dest_port_no
        dest_i_pv_6_address = self.dest_i_pv_6_address
        ttl = self.ttl
        active_multicast_enabled: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_multicast_enabled, Unset):
            active_multicast_enabled = self.active_multicast_enabled.to_dict()

        packaging_format = self.packaging_format
        fec_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fec_info, Unset):
            fec_info = self.fec_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if user_trigger_threshold is not UNSET:
            field_dict["userTriggerThreshold"] = user_trigger_threshold
        if dest_ip_address is not UNSET:
            field_dict["destIPAddress"] = dest_ip_address
        if video_dest_port_no is not UNSET:
            field_dict["videoDestPortNo"] = video_dest_port_no
        if audio_dest_port_no is not UNSET:
            field_dict["audioDestPortNo"] = audio_dest_port_no
        if dest_i_pv_6_address is not UNSET:
            field_dict["destIPv6Address"] = dest_i_pv_6_address
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if active_multicast_enabled is not UNSET:
            field_dict["activeMulticastEnabled"] = active_multicast_enabled
        if packaging_format is not UNSET:
            field_dict["packagingFormat"] = packaging_format
        if fec_info is not UNSET:
            field_dict["FecInfo"] = fec_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_multicast_active_multicast_enabled import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastActiveMulticastEnabled,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_transport_multicast_fec_info import (
            RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastFecInfo,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        user_trigger_threshold = d.pop("userTriggerThreshold", UNSET)

        dest_ip_address = d.pop("destIPAddress", UNSET)

        video_dest_port_no = d.pop("videoDestPortNo", UNSET)

        audio_dest_port_no = d.pop("audioDestPortNo", UNSET)

        dest_i_pv_6_address = d.pop("destIPv6Address", UNSET)

        ttl = d.pop("ttl", UNSET)

        _active_multicast_enabled = d.pop("activeMulticastEnabled", UNSET)
        active_multicast_enabled: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastActiveMulticastEnabled
        ]
        if isinstance(_active_multicast_enabled, Unset):
            active_multicast_enabled = UNSET
        else:
            active_multicast_enabled = (
                RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastActiveMulticastEnabled.from_dict(
                    _active_multicast_enabled
                )
            )

        packaging_format = d.pop("packagingFormat", UNSET)

        _fec_info = d.pop("FecInfo", UNSET)
        fec_info: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastFecInfo]
        if isinstance(_fec_info, Unset):
            fec_info = UNSET
        else:
            fec_info = RootTypeForXMLStreamingChannelStreamingChannelTransportMulticastFecInfo.from_dict(_fec_info)

        root_type_for_xml_streaming_channel_streaming_channel_transport_multicast = cls(
            enabled=enabled,
            user_trigger_threshold=user_trigger_threshold,
            dest_ip_address=dest_ip_address,
            video_dest_port_no=video_dest_port_no,
            audio_dest_port_no=audio_dest_port_no,
            dest_i_pv_6_address=dest_i_pv_6_address,
            ttl=ttl,
            active_multicast_enabled=active_multicast_enabled,
            packaging_format=packaging_format,
            fec_info=fec_info,
        )

        root_type_for_xml_streaming_channel_streaming_channel_transport_multicast.additional_properties = d
        return root_type_for_xml_streaming_channel_streaming_channel_transport_multicast

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
