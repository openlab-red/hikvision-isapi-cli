from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_two_way_audio_channel_list_two_way_audio_channel_list import (
        RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList,
    )


T = TypeVar("T", bound="RootTypeForXMLTwoWayAudioChannelList")


@attr.s(auto_attribs=True)
class RootTypeForXMLTwoWayAudioChannelList:
    """TwoWayAudioChannelList message in XML format

    Example:
        {'TwoWayAudioChannelList': {'TwoWayAudioChannel': [], '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        two_way_audio_channel_list (Union[Unset, RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList]):
    """

    two_way_audio_channel_list: Union[Unset, "RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        two_way_audio_channel_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.two_way_audio_channel_list, Unset):
            two_way_audio_channel_list = self.two_way_audio_channel_list.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if two_way_audio_channel_list is not UNSET:
            field_dict["TwoWayAudioChannelList"] = two_way_audio_channel_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_two_way_audio_channel_list_two_way_audio_channel_list import (
            RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList,
        )

        d = src_dict.copy()
        _two_way_audio_channel_list = d.pop("TwoWayAudioChannelList", UNSET)
        two_way_audio_channel_list: Union[Unset, RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList]
        if isinstance(_two_way_audio_channel_list, Unset):
            two_way_audio_channel_list = UNSET
        else:
            two_way_audio_channel_list = RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList.from_dict(
                _two_way_audio_channel_list
            )

        root_type_for_xml_two_way_audio_channel_list = cls(
            two_way_audio_channel_list=two_way_audio_channel_list,
        )

        root_type_for_xml_two_way_audio_channel_list.additional_properties = d
        return root_type_for_xml_two_way_audio_channel_list

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
