from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_two_way_audio_session_two_way_audio_session import (
        RootTypeForXMLTwoWayAudioSessionTwoWayAudioSession,
    )


T = TypeVar("T", bound="RootTypeForXMLTwoWayAudioSession")


@attr.s(auto_attribs=True)
class RootTypeForXMLTwoWayAudioSession:
    """TwoWayAudioSession message in XML format

    Example:
        {'TwoWayAudioSession': {'sessionId': '', '@version': '2.0', '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        two_way_audio_session (Union[Unset, RootTypeForXMLTwoWayAudioSessionTwoWayAudioSession]):
    """

    two_way_audio_session: Union[Unset, "RootTypeForXMLTwoWayAudioSessionTwoWayAudioSession"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        two_way_audio_session: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.two_way_audio_session, Unset):
            two_way_audio_session = self.two_way_audio_session.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if two_way_audio_session is not UNSET:
            field_dict["TwoWayAudioSession"] = two_way_audio_session

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_two_way_audio_session_two_way_audio_session import (
            RootTypeForXMLTwoWayAudioSessionTwoWayAudioSession,
        )

        d = src_dict.copy()
        _two_way_audio_session = d.pop("TwoWayAudioSession", UNSET)
        two_way_audio_session: Union[Unset, RootTypeForXMLTwoWayAudioSessionTwoWayAudioSession]
        if isinstance(_two_way_audio_session, Unset):
            two_way_audio_session = UNSET
        else:
            two_way_audio_session = RootTypeForXMLTwoWayAudioSessionTwoWayAudioSession.from_dict(_two_way_audio_session)

        root_type_for_xml_two_way_audio_session = cls(
            two_way_audio_session=two_way_audio_session,
        )

        root_type_for_xml_two_way_audio_session.additional_properties = d
        return root_type_for_xml_two_way_audio_session

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
