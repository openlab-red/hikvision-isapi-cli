from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_video_input_channel_list_video_input_channel_id import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelListVideoInputChannelID,
    )


T = TypeVar("T", bound="RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList")


@attr.s(auto_attribs=True)
class RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList:
    """
    Attributes:
        video_input_channel_id (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideo
            InputChannelListVideoInputChannelID]):
    """

    video_input_channel_id: Union[
        Unset,
        "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelListVideoInputChannelID",
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        video_input_channel_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_input_channel_id, Unset):
            video_input_channel_id = self.video_input_channel_id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video_input_channel_id is not UNSET:
            field_dict["videoInputChannelID"] = video_input_channel_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_video_input_channel_list_video_input_channel_id import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelListVideoInputChannelID,
        )

        d = src_dict.copy()
        _video_input_channel_id = d.pop("videoInputChannelID", UNSET)
        video_input_channel_id: Union[
            Unset,
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelListVideoInputChannelID,
        ]
        if isinstance(_video_input_channel_id, Unset):
            video_input_channel_id = UNSET
        else:
            video_input_channel_id = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelListVideoInputChannelID.from_dict(
                _video_input_channel_id
            )

        root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_video_input_channel_list = cls(
            video_input_channel_id=video_input_channel_id,
        )

        root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_video_input_channel_list.additional_properties = (
            d
        )
        return root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_video_input_channel_list

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
