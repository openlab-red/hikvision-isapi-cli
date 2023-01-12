from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_two_way_audio_channel import RootTypeForXMLTwoWayAudioChannel


T = TypeVar("T", bound="RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList")


@attr.s(auto_attribs=True)
class RootTypeForXMLTwoWayAudioChannelListTwoWayAudioChannelList:
    """
    Attributes:
        two_way_audio_channel (Union[Unset, List['RootTypeForXMLTwoWayAudioChannel']]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    two_way_audio_channel: Union[Unset, List["RootTypeForXMLTwoWayAudioChannel"]] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        two_way_audio_channel: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.two_way_audio_channel, Unset):
            two_way_audio_channel = []
            for two_way_audio_channel_item_data in self.two_way_audio_channel:
                two_way_audio_channel_item = two_way_audio_channel_item_data.to_dict()

                two_way_audio_channel.append(two_way_audio_channel_item)

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if two_way_audio_channel is not UNSET:
            field_dict["TwoWayAudioChannel"] = two_way_audio_channel
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_two_way_audio_channel import RootTypeForXMLTwoWayAudioChannel

        d = src_dict.copy()
        two_way_audio_channel = []
        _two_way_audio_channel = d.pop("TwoWayAudioChannel", UNSET)
        for two_way_audio_channel_item_data in _two_way_audio_channel or []:
            two_way_audio_channel_item = RootTypeForXMLTwoWayAudioChannel.from_dict(two_way_audio_channel_item_data)

            two_way_audio_channel.append(two_way_audio_channel_item)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_two_way_audio_channel_list_two_way_audio_channel_list = cls(
            two_way_audio_channel=two_way_audio_channel,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_two_way_audio_channel_list_two_way_audio_channel_list.additional_properties = d
        return root_type_for_xml_two_way_audio_channel_list_two_way_audio_channel_list

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
