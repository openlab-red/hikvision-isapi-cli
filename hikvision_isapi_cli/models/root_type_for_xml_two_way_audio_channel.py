from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel,
    )


T = TypeVar("T", bound="RootTypeForXMLTwoWayAudioChannel")


@attr.s(auto_attribs=True)
class RootTypeForXMLTwoWayAudioChannel:
    """TwoWayAudioChannel message in XML format

    Example:
        {'TwoWayAudioChannel': {'id': {}, 'enabled': {}, 'audioCompressionType': {}, 'audioInboundCompressionType': {},
            'speakerVolume': {}, 'microphoneVolume': {}, 'noisereduce': {}, 'audioBitRate': {}, 'audioInputType': {},
            'associateVideoInputs': {'enabled': {}, 'videoInputChannelList': {'videoInputChannelID': {}}},
            'lineOutForbidden': {}, 'micInForbidden': {}, '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        two_way_audio_channel (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel]):
    """

    two_way_audio_channel: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        two_way_audio_channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.two_way_audio_channel, Unset):
            two_way_audio_channel = self.two_way_audio_channel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if two_way_audio_channel is not UNSET:
            field_dict["TwoWayAudioChannel"] = two_way_audio_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel,
        )

        d = src_dict.copy()
        _two_way_audio_channel = d.pop("TwoWayAudioChannel", UNSET)
        two_way_audio_channel: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel]
        if isinstance(_two_way_audio_channel, Unset):
            two_way_audio_channel = UNSET
        else:
            two_way_audio_channel = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannel.from_dict(_two_way_audio_channel)

        root_type_for_xml_two_way_audio_channel = cls(
            two_way_audio_channel=two_way_audio_channel,
        )

        root_type_for_xml_two_way_audio_channel.additional_properties = d
        return root_type_for_xml_two_way_audio_channel

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
