from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_enabled import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsEnabled,
    )
    from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_video_input_channel_list import (
        RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList,
    )


T = TypeVar("T", bound="RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs")


@attr.s(auto_attribs=True)
class RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputs:
    """
    Attributes:
        enabled (Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsEnabled]):
        video_input_channel_list (Union[Unset,
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList]):
    """

    enabled: Union[Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsEnabled"] = UNSET
    video_input_channel_list: Union[
        Unset, "RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = self.enabled.to_dict()

        video_input_channel_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_input_channel_list, Unset):
            video_input_channel_list = self.video_input_channel_list.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if video_input_channel_list is not UNSET:
            field_dict["videoInputChannelList"] = video_input_channel_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_enabled import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsEnabled,
        )
        from ..models.root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs_video_input_channel_list import (
            RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList,
        )

        d = src_dict.copy()
        _enabled = d.pop("enabled", UNSET)
        enabled: Union[Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsEnabled]
        if isinstance(_enabled, Unset):
            enabled = UNSET
        else:
            enabled = RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsEnabled.from_dict(_enabled)

        _video_input_channel_list = d.pop("videoInputChannelList", UNSET)
        video_input_channel_list: Union[
            Unset, RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList
        ]
        if isinstance(_video_input_channel_list, Unset):
            video_input_channel_list = UNSET
        else:
            video_input_channel_list = (
                RootTypeForXMLTwoWayAudioChannelTwoWayAudioChannelAssociateVideoInputsVideoInputChannelList.from_dict(
                    _video_input_channel_list
                )
            )

        root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs = cls(
            enabled=enabled,
            video_input_channel_list=video_input_channel_list,
        )

        root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs.additional_properties = d
        return root_type_for_xml_two_way_audio_channel_two_way_audio_channel_associate_video_inputs

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
