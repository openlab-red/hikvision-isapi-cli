from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_video_input_channel_video_input_channel import (
        RootTypeForXMLVideoInputChannelVideoInputChannel,
    )


T = TypeVar("T", bound="RootTypeForXMLVideoInputChannel")


@attr.s(auto_attribs=True)
class RootTypeForXMLVideoInputChannel:
    """VideoInputChannel message in XML format

    Example:
        {'VideoInputChannel': {'id': {}, 'inputPort': {}, 'videoInputEnabled': {}, 'name': {}, 'videoFormat': {},
            'portType': {}, 'resDesc': {}, '@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        video_input_channel (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannel]):
    """

    video_input_channel: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannel"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        video_input_channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_input_channel, Unset):
            video_input_channel = self.video_input_channel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video_input_channel is not UNSET:
            field_dict["VideoInputChannel"] = video_input_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_video_input_channel_video_input_channel import (
            RootTypeForXMLVideoInputChannelVideoInputChannel,
        )

        d = src_dict.copy()
        _video_input_channel = d.pop("VideoInputChannel", UNSET)
        video_input_channel: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannel]
        if isinstance(_video_input_channel, Unset):
            video_input_channel = UNSET
        else:
            video_input_channel = RootTypeForXMLVideoInputChannelVideoInputChannel.from_dict(_video_input_channel)

        root_type_for_xml_video_input_channel = cls(
            video_input_channel=video_input_channel,
        )

        root_type_for_xml_video_input_channel.additional_properties = d
        return root_type_for_xml_video_input_channel

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
