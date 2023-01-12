from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel import RootTypeForXMLStreamingChannel


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelList")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelList:
    """StreamingChannelList message in XML format

    Example:
        {'StreamingChannelList': {'StreamingChannel': '', '@version': '2.0', '@StreamingChannelList message in XML
            formatxmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        streaming_channel_list (Union[Unset, List['RootTypeForXMLStreamingChannel']]):
    """

    streaming_channel_list: Union[Unset, List["RootTypeForXMLStreamingChannel"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        streaming_channel_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.streaming_channel_list, Unset):
            streaming_channel_list = []
            for streaming_channel_list_item_data in self.streaming_channel_list:
                streaming_channel_list_item = streaming_channel_list_item_data.to_dict()

                streaming_channel_list.append(streaming_channel_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if streaming_channel_list is not UNSET:
            field_dict["StreamingChannelList"] = streaming_channel_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel import RootTypeForXMLStreamingChannel

        d = src_dict.copy()
        streaming_channel_list = []
        _streaming_channel_list = d.pop("StreamingChannelList", UNSET)
        for streaming_channel_list_item_data in _streaming_channel_list or []:
            streaming_channel_list_item = RootTypeForXMLStreamingChannel.from_dict(streaming_channel_list_item_data)

            streaming_channel_list.append(streaming_channel_list_item)

        root_type_for_xml_streaming_channel_list = cls(
            streaming_channel_list=streaming_channel_list,
        )

        root_type_for_xml_streaming_channel_list.additional_properties = d
        return root_type_for_xml_streaming_channel_list

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
