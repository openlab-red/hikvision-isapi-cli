from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar(
    "T",
    bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID",
)


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID:
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_input_channel_id = (
            cls()
        )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_input_channel_id.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_input_channel_id

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
