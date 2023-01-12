from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_video_input_channel import RootTypeForXMLVideoInputChannel


T = TypeVar("T", bound="RootTypeForXMLVideoInputChannelListVideoInputChannelList")


@attr.s(auto_attribs=True)
class RootTypeForXMLVideoInputChannelListVideoInputChannelList:
    """
    Attributes:
        video_input_channel (Union[Unset, List['RootTypeForXMLVideoInputChannel']]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    video_input_channel: Union[Unset, List["RootTypeForXMLVideoInputChannel"]] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        video_input_channel: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.video_input_channel, Unset):
            video_input_channel = []
            for video_input_channel_item_data in self.video_input_channel:
                video_input_channel_item = video_input_channel_item_data.to_dict()

                video_input_channel.append(video_input_channel_item)

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video_input_channel is not UNSET:
            field_dict["VideoInputChannel"] = video_input_channel
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_video_input_channel import RootTypeForXMLVideoInputChannel

        d = src_dict.copy()
        video_input_channel = []
        _video_input_channel = d.pop("VideoInputChannel", UNSET)
        for video_input_channel_item_data in _video_input_channel or []:
            video_input_channel_item = RootTypeForXMLVideoInputChannel.from_dict(video_input_channel_item_data)

            video_input_channel.append(video_input_channel_item)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_video_input_channel_list_video_input_channel_list = cls(
            video_input_channel=video_input_channel,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_video_input_channel_list_video_input_channel_list.additional_properties = d
        return root_type_for_xml_video_input_channel_list_video_input_channel_list

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
