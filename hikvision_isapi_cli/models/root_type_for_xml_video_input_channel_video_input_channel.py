from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_video_input_channel_video_input_channel_id import (
        RootTypeForXMLVideoInputChannelVideoInputChannelId,
    )
    from ..models.root_type_for_xml_video_input_channel_video_input_channel_input_port import (
        RootTypeForXMLVideoInputChannelVideoInputChannelInputPort,
    )
    from ..models.root_type_for_xml_video_input_channel_video_input_channel_name import (
        RootTypeForXMLVideoInputChannelVideoInputChannelName,
    )
    from ..models.root_type_for_xml_video_input_channel_video_input_channel_port_type import (
        RootTypeForXMLVideoInputChannelVideoInputChannelPortType,
    )
    from ..models.root_type_for_xml_video_input_channel_video_input_channel_res_desc import (
        RootTypeForXMLVideoInputChannelVideoInputChannelResDesc,
    )
    from ..models.root_type_for_xml_video_input_channel_video_input_channel_video_format import (
        RootTypeForXMLVideoInputChannelVideoInputChannelVideoFormat,
    )
    from ..models.root_type_for_xml_video_input_channel_video_input_channel_video_input_enabled import (
        RootTypeForXMLVideoInputChannelVideoInputChannelVideoInputEnabled,
    )


T = TypeVar("T", bound="RootTypeForXMLVideoInputChannelVideoInputChannel")


@attr.s(auto_attribs=True)
class RootTypeForXMLVideoInputChannelVideoInputChannel:
    """
    Attributes:
        id (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelId]):
        input_port (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelInputPort]):
        video_input_enabled (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelVideoInputEnabled]):
        name (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelName]):
        video_format (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelVideoFormat]):
        port_type (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelPortType]):
        res_desc (Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelResDesc]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    id: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannelId"] = UNSET
    input_port: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannelInputPort"] = UNSET
    video_input_enabled: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannelVideoInputEnabled"] = UNSET
    name: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannelName"] = UNSET
    video_format: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannelVideoFormat"] = UNSET
    port_type: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannelPortType"] = UNSET
    res_desc: Union[Unset, "RootTypeForXMLVideoInputChannelVideoInputChannelResDesc"] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        input_port: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.input_port, Unset):
            input_port = self.input_port.to_dict()

        video_input_enabled: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_input_enabled, Unset):
            video_input_enabled = self.video_input_enabled.to_dict()

        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        video_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_format, Unset):
            video_format = self.video_format.to_dict()

        port_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.port_type, Unset):
            port_type = self.port_type.to_dict()

        res_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.res_desc, Unset):
            res_desc = self.res_desc.to_dict()

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if input_port is not UNSET:
            field_dict["inputPort"] = input_port
        if video_input_enabled is not UNSET:
            field_dict["videoInputEnabled"] = video_input_enabled
        if name is not UNSET:
            field_dict["name"] = name
        if video_format is not UNSET:
            field_dict["videoFormat"] = video_format
        if port_type is not UNSET:
            field_dict["portType"] = port_type
        if res_desc is not UNSET:
            field_dict["resDesc"] = res_desc
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_video_input_channel_video_input_channel_id import (
            RootTypeForXMLVideoInputChannelVideoInputChannelId,
        )
        from ..models.root_type_for_xml_video_input_channel_video_input_channel_input_port import (
            RootTypeForXMLVideoInputChannelVideoInputChannelInputPort,
        )
        from ..models.root_type_for_xml_video_input_channel_video_input_channel_name import (
            RootTypeForXMLVideoInputChannelVideoInputChannelName,
        )
        from ..models.root_type_for_xml_video_input_channel_video_input_channel_port_type import (
            RootTypeForXMLVideoInputChannelVideoInputChannelPortType,
        )
        from ..models.root_type_for_xml_video_input_channel_video_input_channel_res_desc import (
            RootTypeForXMLVideoInputChannelVideoInputChannelResDesc,
        )
        from ..models.root_type_for_xml_video_input_channel_video_input_channel_video_format import (
            RootTypeForXMLVideoInputChannelVideoInputChannelVideoFormat,
        )
        from ..models.root_type_for_xml_video_input_channel_video_input_channel_video_input_enabled import (
            RootTypeForXMLVideoInputChannelVideoInputChannelVideoInputEnabled,
        )

        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RootTypeForXMLVideoInputChannelVideoInputChannelId.from_dict(_id)

        _input_port = d.pop("inputPort", UNSET)
        input_port: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelInputPort]
        if isinstance(_input_port, Unset):
            input_port = UNSET
        else:
            input_port = RootTypeForXMLVideoInputChannelVideoInputChannelInputPort.from_dict(_input_port)

        _video_input_enabled = d.pop("videoInputEnabled", UNSET)
        video_input_enabled: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelVideoInputEnabled]
        if isinstance(_video_input_enabled, Unset):
            video_input_enabled = UNSET
        else:
            video_input_enabled = RootTypeForXMLVideoInputChannelVideoInputChannelVideoInputEnabled.from_dict(
                _video_input_enabled
            )

        _name = d.pop("name", UNSET)
        name: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = RootTypeForXMLVideoInputChannelVideoInputChannelName.from_dict(_name)

        _video_format = d.pop("videoFormat", UNSET)
        video_format: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelVideoFormat]
        if isinstance(_video_format, Unset):
            video_format = UNSET
        else:
            video_format = RootTypeForXMLVideoInputChannelVideoInputChannelVideoFormat.from_dict(_video_format)

        _port_type = d.pop("portType", UNSET)
        port_type: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelPortType]
        if isinstance(_port_type, Unset):
            port_type = UNSET
        else:
            port_type = RootTypeForXMLVideoInputChannelVideoInputChannelPortType.from_dict(_port_type)

        _res_desc = d.pop("resDesc", UNSET)
        res_desc: Union[Unset, RootTypeForXMLVideoInputChannelVideoInputChannelResDesc]
        if isinstance(_res_desc, Unset):
            res_desc = UNSET
        else:
            res_desc = RootTypeForXMLVideoInputChannelVideoInputChannelResDesc.from_dict(_res_desc)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_video_input_channel_video_input_channel = cls(
            id=id,
            input_port=input_port,
            video_input_enabled=video_input_enabled,
            name=name,
            video_format=video_format,
            port_type=port_type,
            res_desc=res_desc,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_video_input_channel_video_input_channel.additional_properties = d
        return root_type_for_xml_video_input_channel_video_input_channel

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
