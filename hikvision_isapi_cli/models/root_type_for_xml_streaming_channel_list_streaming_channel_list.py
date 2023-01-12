from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel import RootTypeForXMLStreamingChannel


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelListStreamingChannelList")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelListStreamingChannelList:
    """
    Attributes:
        streaming_channel (Union[Unset, List['RootTypeForXMLStreamingChannel']]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    streaming_channel: Union[Unset, List["RootTypeForXMLStreamingChannel"]] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        streaming_channel: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.streaming_channel, Unset):
            streaming_channel = []
            for streaming_channel_item_data in self.streaming_channel:
                streaming_channel_item = streaming_channel_item_data.to_dict()

                streaming_channel.append(streaming_channel_item)

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if streaming_channel is not UNSET:
            field_dict["StreamingChannel"] = streaming_channel
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel import RootTypeForXMLStreamingChannel

        d = src_dict.copy()
        streaming_channel = []
        _streaming_channel = d.pop("StreamingChannel", UNSET)
        for streaming_channel_item_data in _streaming_channel or []:
            streaming_channel_item = RootTypeForXMLStreamingChannel.from_dict(streaming_channel_item_data)

            streaming_channel.append(streaming_channel_item)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_streaming_channel_list_streaming_channel_list = cls(
            streaming_channel=streaming_channel,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_streaming_channel_list_streaming_channel_list.additional_properties = d
        return root_type_for_xml_streaming_channel_list_streaming_channel_list

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
