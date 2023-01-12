from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_video_input_channel_list_video_input_channel_list import (
        RootTypeForXMLVideoInputChannelListVideoInputChannelList,
    )


T = TypeVar("T", bound="RootTypeForXMLVideoInputChannelList")


@attr.s(auto_attribs=True)
class RootTypeForXMLVideoInputChannelList:
    """VideoInputChannelList message in XML format

    Example:
        {'VideoInputChannelList': {'VideoInputChannel': [{}], '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        video_input_channel_list (Union[Unset, RootTypeForXMLVideoInputChannelListVideoInputChannelList]):
    """

    video_input_channel_list: Union[Unset, "RootTypeForXMLVideoInputChannelListVideoInputChannelList"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        video_input_channel_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_input_channel_list, Unset):
            video_input_channel_list = self.video_input_channel_list.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video_input_channel_list is not UNSET:
            field_dict["VideoInputChannelList"] = video_input_channel_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_video_input_channel_list_video_input_channel_list import (
            RootTypeForXMLVideoInputChannelListVideoInputChannelList,
        )

        d = src_dict.copy()
        _video_input_channel_list = d.pop("VideoInputChannelList", UNSET)
        video_input_channel_list: Union[Unset, RootTypeForXMLVideoInputChannelListVideoInputChannelList]
        if isinstance(_video_input_channel_list, Unset):
            video_input_channel_list = UNSET
        else:
            video_input_channel_list = RootTypeForXMLVideoInputChannelListVideoInputChannelList.from_dict(
                _video_input_channel_list
            )

        root_type_for_xml_video_input_channel_list = cls(
            video_input_channel_list=video_input_channel_list,
        )

        root_type_for_xml_video_input_channel_list.additional_properties = d
        return root_type_for_xml_video_input_channel_list

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
