from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_multicast_fec_info_fec_dest_port_no import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecDestPortNo,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_multicast_fec_info_fec_ratio import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecRatio,
    )


T = TypeVar(
    "T",
    bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfo",
)


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfo:
    """
    Attributes:
        fec_ratio (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTranspor
            tMulticastFecInfoFecRatio]):
        fec_dest_port_no (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelT
            ransportMulticastFecInfoFecDestPortNo]):
    """

    fec_ratio: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecRatio",
    ] = UNSET
    fec_dest_port_no: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecDestPortNo",
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fec_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fec_ratio, Unset):
            fec_ratio = self.fec_ratio.to_dict()

        fec_dest_port_no: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fec_dest_port_no, Unset):
            fec_dest_port_no = self.fec_dest_port_no.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fec_ratio is not UNSET:
            field_dict["fecRatio"] = fec_ratio
        if fec_dest_port_no is not UNSET:
            field_dict["fecDestPortNo"] = fec_dest_port_no

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_multicast_fec_info_fec_dest_port_no import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecDestPortNo,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_multicast_fec_info_fec_ratio import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecRatio,
        )

        d = src_dict.copy()
        _fec_ratio = d.pop("fecRatio", UNSET)
        fec_ratio: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecRatio,
        ]
        if isinstance(_fec_ratio, Unset):
            fec_ratio = UNSET
        else:
            fec_ratio = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecRatio.from_dict(
                _fec_ratio
            )

        _fec_dest_port_no = d.pop("fecDestPortNo", UNSET)
        fec_dest_port_no: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecDestPortNo,
        ]
        if isinstance(_fec_dest_port_no, Unset):
            fec_dest_port_no = UNSET
        else:
            fec_dest_port_no = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelTransportMulticastFecInfoFecDestPortNo.from_dict(
                _fec_dest_port_no
            )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_multicast_fec_info = cls(
            fec_ratio=fec_ratio,
            fec_dest_port_no=fec_dest_port_no,
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_multicast_fec_info.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_transport_multicast_fec_info

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
