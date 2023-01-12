from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_constant_bit_rate import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoConstantBitRate,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_intelligent_info_display_method import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoIntelligentInfoDisplayMethod,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_max_frame_rate import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoMaxFrameRate,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_smart_codec import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoSmartCodec,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_svc import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoSVC,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_vbr_lower_cap import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoVbrLowerCap,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_vbr_upper_cap import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoVbrUpperCap,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_codec_type import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoVideoCodecType,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_input_channel_id import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoVideoInputChannelID,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_quality_control_type import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoVideoQualityControlType,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_resolution_height import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionHeight,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_resolution_width import (
        RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionWidth,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelVideo")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelVideo:
    """
    Attributes:
        enabled (Union[Unset, str]):
        video_input_channel_id (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoInputChannelID]):
        video_codec_type (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoCodecType]):
        video_resolution_width (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionWidth]):
        video_resolution_height (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionHeight]):
        video_quality_control_type (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelVideoVideoQualityControlType]):
        constant_bit_rate (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoConstantBitRate]):
        vbr_upper_cap (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVbrUpperCap]):
        vbr_lower_cap (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVbrLowerCap]):
        max_frame_rate (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoMaxFrameRate]):
        key_frame_interval (Union[Unset, str]):
        rotation_degree (Union[Unset, str]):
        mirror_enabled (Union[Unset, str]):
        snap_shot_image_type (Union[Unset, str]):
        mpeg_4_profile (Union[Unset, str]):
        h264_profile (Union[Unset, str]):
        svac_profile (Union[Unset, str]):
        gov_length (Union[Unset, str]):
        svc (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoSVC]):
        smoothing (Union[Unset, str]):
        smart_codec (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoSmartCodec]):
        vbr_average_cap (Union[Unset, str]):
        intelligent_info_display_method (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelVideoIntelligentInfoDisplayMethod]):
    """

    enabled: Union[Unset, str] = UNSET
    video_input_channel_id: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoVideoInputChannelID"
    ] = UNSET
    video_codec_type: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoVideoCodecType"] = UNSET
    video_resolution_width: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionWidth"
    ] = UNSET
    video_resolution_height: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionHeight"
    ] = UNSET
    video_quality_control_type: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoVideoQualityControlType"
    ] = UNSET
    constant_bit_rate: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoConstantBitRate"] = UNSET
    vbr_upper_cap: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoVbrUpperCap"] = UNSET
    vbr_lower_cap: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoVbrLowerCap"] = UNSET
    max_frame_rate: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoMaxFrameRate"] = UNSET
    key_frame_interval: Union[Unset, str] = UNSET
    rotation_degree: Union[Unset, str] = UNSET
    mirror_enabled: Union[Unset, str] = UNSET
    snap_shot_image_type: Union[Unset, str] = UNSET
    mpeg_4_profile: Union[Unset, str] = UNSET
    h264_profile: Union[Unset, str] = UNSET
    svac_profile: Union[Unset, str] = UNSET
    gov_length: Union[Unset, str] = UNSET
    svc: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoSVC"] = UNSET
    smoothing: Union[Unset, str] = UNSET
    smart_codec: Union[Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoSmartCodec"] = UNSET
    vbr_average_cap: Union[Unset, str] = UNSET
    intelligent_info_display_method: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelVideoIntelligentInfoDisplayMethod"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        video_input_channel_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_input_channel_id, Unset):
            video_input_channel_id = self.video_input_channel_id.to_dict()

        video_codec_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_codec_type, Unset):
            video_codec_type = self.video_codec_type.to_dict()

        video_resolution_width: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_resolution_width, Unset):
            video_resolution_width = self.video_resolution_width.to_dict()

        video_resolution_height: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_resolution_height, Unset):
            video_resolution_height = self.video_resolution_height.to_dict()

        video_quality_control_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.video_quality_control_type, Unset):
            video_quality_control_type = self.video_quality_control_type.to_dict()

        constant_bit_rate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constant_bit_rate, Unset):
            constant_bit_rate = self.constant_bit_rate.to_dict()

        vbr_upper_cap: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vbr_upper_cap, Unset):
            vbr_upper_cap = self.vbr_upper_cap.to_dict()

        vbr_lower_cap: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vbr_lower_cap, Unset):
            vbr_lower_cap = self.vbr_lower_cap.to_dict()

        max_frame_rate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_frame_rate, Unset):
            max_frame_rate = self.max_frame_rate.to_dict()

        key_frame_interval = self.key_frame_interval
        rotation_degree = self.rotation_degree
        mirror_enabled = self.mirror_enabled
        snap_shot_image_type = self.snap_shot_image_type
        mpeg_4_profile = self.mpeg_4_profile
        h264_profile = self.h264_profile
        svac_profile = self.svac_profile
        gov_length = self.gov_length
        svc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.svc, Unset):
            svc = self.svc.to_dict()

        smoothing = self.smoothing
        smart_codec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.smart_codec, Unset):
            smart_codec = self.smart_codec.to_dict()

        vbr_average_cap = self.vbr_average_cap
        intelligent_info_display_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.intelligent_info_display_method, Unset):
            intelligent_info_display_method = self.intelligent_info_display_method.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if video_input_channel_id is not UNSET:
            field_dict["videoInputChannelID"] = video_input_channel_id
        if video_codec_type is not UNSET:
            field_dict["videoCodecType"] = video_codec_type
        if video_resolution_width is not UNSET:
            field_dict["videoResolutionWidth"] = video_resolution_width
        if video_resolution_height is not UNSET:
            field_dict["videoResolutionHeight"] = video_resolution_height
        if video_quality_control_type is not UNSET:
            field_dict["videoQualityControlType"] = video_quality_control_type
        if constant_bit_rate is not UNSET:
            field_dict["constantBitRate"] = constant_bit_rate
        if vbr_upper_cap is not UNSET:
            field_dict["vbrUpperCap"] = vbr_upper_cap
        if vbr_lower_cap is not UNSET:
            field_dict["vbrLowerCap"] = vbr_lower_cap
        if max_frame_rate is not UNSET:
            field_dict["maxFrameRate"] = max_frame_rate
        if key_frame_interval is not UNSET:
            field_dict["keyFrameInterval"] = key_frame_interval
        if rotation_degree is not UNSET:
            field_dict["rotationDegree"] = rotation_degree
        if mirror_enabled is not UNSET:
            field_dict["mirrorEnabled"] = mirror_enabled
        if snap_shot_image_type is not UNSET:
            field_dict["snapShotImageType"] = snap_shot_image_type
        if mpeg_4_profile is not UNSET:
            field_dict["Mpeg4Profile"] = mpeg_4_profile
        if h264_profile is not UNSET:
            field_dict["H264Profile"] = h264_profile
        if svac_profile is not UNSET:
            field_dict["SVACProfile"] = svac_profile
        if gov_length is not UNSET:
            field_dict["GovLength"] = gov_length
        if svc is not UNSET:
            field_dict["SVC"] = svc
        if smoothing is not UNSET:
            field_dict["smoothing"] = smoothing
        if smart_codec is not UNSET:
            field_dict["SmartCodec"] = smart_codec
        if vbr_average_cap is not UNSET:
            field_dict["vbrAverageCap"] = vbr_average_cap
        if intelligent_info_display_method is not UNSET:
            field_dict["IntelligentInfoDisplayMethod"] = intelligent_info_display_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_constant_bit_rate import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoConstantBitRate,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_intelligent_info_display_method import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoIntelligentInfoDisplayMethod,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_max_frame_rate import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoMaxFrameRate,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_smart_codec import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoSmartCodec,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_svc import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoSVC,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_vbr_lower_cap import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoVbrLowerCap,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_vbr_upper_cap import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoVbrUpperCap,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_codec_type import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoVideoCodecType,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_input_channel_id import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoVideoInputChannelID,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_quality_control_type import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoVideoQualityControlType,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_resolution_height import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionHeight,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_video_video_resolution_width import (
            RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionWidth,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        _video_input_channel_id = d.pop("videoInputChannelID", UNSET)
        video_input_channel_id: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoInputChannelID]
        if isinstance(_video_input_channel_id, Unset):
            video_input_channel_id = UNSET
        else:
            video_input_channel_id = RootTypeForXMLStreamingChannelStreamingChannelVideoVideoInputChannelID.from_dict(
                _video_input_channel_id
            )

        _video_codec_type = d.pop("videoCodecType", UNSET)
        video_codec_type: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoCodecType]
        if isinstance(_video_codec_type, Unset):
            video_codec_type = UNSET
        else:
            video_codec_type = RootTypeForXMLStreamingChannelStreamingChannelVideoVideoCodecType.from_dict(
                _video_codec_type
            )

        _video_resolution_width = d.pop("videoResolutionWidth", UNSET)
        video_resolution_width: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionWidth]
        if isinstance(_video_resolution_width, Unset):
            video_resolution_width = UNSET
        else:
            video_resolution_width = RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionWidth.from_dict(
                _video_resolution_width
            )

        _video_resolution_height = d.pop("videoResolutionHeight", UNSET)
        video_resolution_height: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionHeight]
        if isinstance(_video_resolution_height, Unset):
            video_resolution_height = UNSET
        else:
            video_resolution_height = (
                RootTypeForXMLStreamingChannelStreamingChannelVideoVideoResolutionHeight.from_dict(
                    _video_resolution_height
                )
            )

        _video_quality_control_type = d.pop("videoQualityControlType", UNSET)
        video_quality_control_type: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVideoQualityControlType
        ]
        if isinstance(_video_quality_control_type, Unset):
            video_quality_control_type = UNSET
        else:
            video_quality_control_type = (
                RootTypeForXMLStreamingChannelStreamingChannelVideoVideoQualityControlType.from_dict(
                    _video_quality_control_type
                )
            )

        _constant_bit_rate = d.pop("constantBitRate", UNSET)
        constant_bit_rate: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoConstantBitRate]
        if isinstance(_constant_bit_rate, Unset):
            constant_bit_rate = UNSET
        else:
            constant_bit_rate = RootTypeForXMLStreamingChannelStreamingChannelVideoConstantBitRate.from_dict(
                _constant_bit_rate
            )

        _vbr_upper_cap = d.pop("vbrUpperCap", UNSET)
        vbr_upper_cap: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVbrUpperCap]
        if isinstance(_vbr_upper_cap, Unset):
            vbr_upper_cap = UNSET
        else:
            vbr_upper_cap = RootTypeForXMLStreamingChannelStreamingChannelVideoVbrUpperCap.from_dict(_vbr_upper_cap)

        _vbr_lower_cap = d.pop("vbrLowerCap", UNSET)
        vbr_lower_cap: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoVbrLowerCap]
        if isinstance(_vbr_lower_cap, Unset):
            vbr_lower_cap = UNSET
        else:
            vbr_lower_cap = RootTypeForXMLStreamingChannelStreamingChannelVideoVbrLowerCap.from_dict(_vbr_lower_cap)

        _max_frame_rate = d.pop("maxFrameRate", UNSET)
        max_frame_rate: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoMaxFrameRate]
        if isinstance(_max_frame_rate, Unset):
            max_frame_rate = UNSET
        else:
            max_frame_rate = RootTypeForXMLStreamingChannelStreamingChannelVideoMaxFrameRate.from_dict(_max_frame_rate)

        key_frame_interval = d.pop("keyFrameInterval", UNSET)

        rotation_degree = d.pop("rotationDegree", UNSET)

        mirror_enabled = d.pop("mirrorEnabled", UNSET)

        snap_shot_image_type = d.pop("snapShotImageType", UNSET)

        mpeg_4_profile = d.pop("Mpeg4Profile", UNSET)

        h264_profile = d.pop("H264Profile", UNSET)

        svac_profile = d.pop("SVACProfile", UNSET)

        gov_length = d.pop("GovLength", UNSET)

        _svc = d.pop("SVC", UNSET)
        svc: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoSVC]
        if isinstance(_svc, Unset):
            svc = UNSET
        else:
            svc = RootTypeForXMLStreamingChannelStreamingChannelVideoSVC.from_dict(_svc)

        smoothing = d.pop("smoothing", UNSET)

        _smart_codec = d.pop("SmartCodec", UNSET)
        smart_codec: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoSmartCodec]
        if isinstance(_smart_codec, Unset):
            smart_codec = UNSET
        else:
            smart_codec = RootTypeForXMLStreamingChannelStreamingChannelVideoSmartCodec.from_dict(_smart_codec)

        vbr_average_cap = d.pop("vbrAverageCap", UNSET)

        _intelligent_info_display_method = d.pop("IntelligentInfoDisplayMethod", UNSET)
        intelligent_info_display_method: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelVideoIntelligentInfoDisplayMethod
        ]
        if isinstance(_intelligent_info_display_method, Unset):
            intelligent_info_display_method = UNSET
        else:
            intelligent_info_display_method = (
                RootTypeForXMLStreamingChannelStreamingChannelVideoIntelligentInfoDisplayMethod.from_dict(
                    _intelligent_info_display_method
                )
            )

        root_type_for_xml_streaming_channel_streaming_channel_video = cls(
            enabled=enabled,
            video_input_channel_id=video_input_channel_id,
            video_codec_type=video_codec_type,
            video_resolution_width=video_resolution_width,
            video_resolution_height=video_resolution_height,
            video_quality_control_type=video_quality_control_type,
            constant_bit_rate=constant_bit_rate,
            vbr_upper_cap=vbr_upper_cap,
            vbr_lower_cap=vbr_lower_cap,
            max_frame_rate=max_frame_rate,
            key_frame_interval=key_frame_interval,
            rotation_degree=rotation_degree,
            mirror_enabled=mirror_enabled,
            snap_shot_image_type=snap_shot_image_type,
            mpeg_4_profile=mpeg_4_profile,
            h264_profile=h264_profile,
            svac_profile=svac_profile,
            gov_length=gov_length,
            svc=svc,
            smoothing=smoothing,
            smart_codec=smart_codec,
            vbr_average_cap=vbr_average_cap,
            intelligent_info_display_method=intelligent_info_display_method,
        )

        root_type_for_xml_streaming_channel_streaming_channel_video.additional_properties = d
        return root_type_for_xml_streaming_channel_streaming_channel_video

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
