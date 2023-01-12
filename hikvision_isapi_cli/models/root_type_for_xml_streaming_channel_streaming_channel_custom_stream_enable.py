from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnable")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnable:
    """
    Attributes:
        streaming_channel (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel]):
    """

    streaming_channel: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        streaming_channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.streaming_channel, Unset):
            streaming_channel = self.streaming_channel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if streaming_channel is not UNSET:
            field_dict["StreamingChannel"] = streaming_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel,
        )

        d = src_dict.copy()
        _streaming_channel = d.pop("StreamingChannel", UNSET)
        streaming_channel: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel
        ]
        if isinstance(_streaming_channel, Unset):
            streaming_channel = UNSET
        else:
            streaming_channel = (
                RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannel.from_dict(
                    _streaming_channel
                )
            )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable = cls(
            streaming_channel=streaming_channel,
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable.additional_properties = d
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable

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
