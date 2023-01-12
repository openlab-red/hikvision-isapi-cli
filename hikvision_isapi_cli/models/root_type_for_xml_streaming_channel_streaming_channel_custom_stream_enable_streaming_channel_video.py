from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_constant_bit_rate import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoConstantBitRate,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_intelligent_info_display_method import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoIntelligentInfoDisplayMethod,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_max_frame_rate import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoMaxFrameRate,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_smart_codec import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSmartCodec,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_svc import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSVC,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_vbr_lower_cap import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrLowerCap,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_vbr_upper_cap import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrUpperCap,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_codec_type import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoCodecType,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_input_channel_id import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_quality_control_type import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoQualityControlType,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_resolution_height import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionHeight,
    )
    from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_resolution_width import (
        RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionWidth,
    )


T = TypeVar("T", bound="RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideo:
    """
    Attributes:
        enabled (Union[Unset, str]):
        video_input_channel_id (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID]):
        video_codec_type (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoCodecType]):
        video_resolution_width (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionWidth]):
        video_resolution_height (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionHeight]):
        video_quality_control_type (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoQualityControlType]):
        constant_bit_rate (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoConstantBitRate]):
        vbr_upper_cap (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrUpperCap]):
        vbr_lower_cap (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrLowerCap]):
        max_frame_rate (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoMaxFrameRate]):
        key_frame_interval (Union[Unset, str]):
        rotation_degree (Union[Unset, str]):
        mirror_enabled (Union[Unset, str]):
        snap_shot_image_type (Union[Unset, str]):
        mpeg_4_profile (Union[Unset, str]):
        h264_profile (Union[Unset, str]):
        svac_profile (Union[Unset, str]):
        gov_length (Union[Unset, str]):
        svc (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSVC]):
        smoothing (Union[Unset, str]):
        smart_codec (Union[Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSmartCodec]):
        vbr_average_cap (Union[Unset, str]):
        intelligent_info_display_method (Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableSt
            reamingChannelVideoIntelligentInfoDisplayMethod]):
    """

    enabled: Union[Unset, str] = UNSET
    video_input_channel_id: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID",
    ] = UNSET
    video_codec_type: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoCodecType"
    ] = UNSET
    video_resolution_width: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionWidth",
    ] = UNSET
    video_resolution_height: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionHeight",
    ] = UNSET
    video_quality_control_type: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoQualityControlType",
    ] = UNSET
    constant_bit_rate: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoConstantBitRate"
    ] = UNSET
    vbr_upper_cap: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrUpperCap"
    ] = UNSET
    vbr_lower_cap: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrLowerCap"
    ] = UNSET
    max_frame_rate: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoMaxFrameRate"
    ] = UNSET
    key_frame_interval: Union[Unset, str] = UNSET
    rotation_degree: Union[Unset, str] = UNSET
    mirror_enabled: Union[Unset, str] = UNSET
    snap_shot_image_type: Union[Unset, str] = UNSET
    mpeg_4_profile: Union[Unset, str] = UNSET
    h264_profile: Union[Unset, str] = UNSET
    svac_profile: Union[Unset, str] = UNSET
    gov_length: Union[Unset, str] = UNSET
    svc: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSVC"
    ] = UNSET
    smoothing: Union[Unset, str] = UNSET
    smart_codec: Union[
        Unset, "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSmartCodec"
    ] = UNSET
    vbr_average_cap: Union[Unset, str] = UNSET
    intelligent_info_display_method: Union[
        Unset,
        "RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoIntelligentInfoDisplayMethod",
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
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_constant_bit_rate import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoConstantBitRate,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_intelligent_info_display_method import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoIntelligentInfoDisplayMethod,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_max_frame_rate import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoMaxFrameRate,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_smart_codec import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSmartCodec,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_svc import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSVC,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_vbr_lower_cap import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrLowerCap,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_vbr_upper_cap import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrUpperCap,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_codec_type import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoCodecType,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_input_channel_id import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_quality_control_type import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoQualityControlType,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_resolution_height import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionHeight,
        )
        from ..models.root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video_video_resolution_width import (
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionWidth,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        _video_input_channel_id = d.pop("videoInputChannelID", UNSET)
        video_input_channel_id: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID,
        ]
        if isinstance(_video_input_channel_id, Unset):
            video_input_channel_id = UNSET
        else:
            video_input_channel_id = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoInputChannelID.from_dict(
                _video_input_channel_id
            )

        _video_codec_type = d.pop("videoCodecType", UNSET)
        video_codec_type: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoCodecType
        ]
        if isinstance(_video_codec_type, Unset):
            video_codec_type = UNSET
        else:
            video_codec_type = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoCodecType.from_dict(
                _video_codec_type
            )

        _video_resolution_width = d.pop("videoResolutionWidth", UNSET)
        video_resolution_width: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionWidth,
        ]
        if isinstance(_video_resolution_width, Unset):
            video_resolution_width = UNSET
        else:
            video_resolution_width = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionWidth.from_dict(
                _video_resolution_width
            )

        _video_resolution_height = d.pop("videoResolutionHeight", UNSET)
        video_resolution_height: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionHeight,
        ]
        if isinstance(_video_resolution_height, Unset):
            video_resolution_height = UNSET
        else:
            video_resolution_height = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoResolutionHeight.from_dict(
                _video_resolution_height
            )

        _video_quality_control_type = d.pop("videoQualityControlType", UNSET)
        video_quality_control_type: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoQualityControlType,
        ]
        if isinstance(_video_quality_control_type, Unset):
            video_quality_control_type = UNSET
        else:
            video_quality_control_type = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVideoQualityControlType.from_dict(
                _video_quality_control_type
            )

        _constant_bit_rate = d.pop("constantBitRate", UNSET)
        constant_bit_rate: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoConstantBitRate
        ]
        if isinstance(_constant_bit_rate, Unset):
            constant_bit_rate = UNSET
        else:
            constant_bit_rate = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoConstantBitRate.from_dict(
                _constant_bit_rate
            )

        _vbr_upper_cap = d.pop("vbrUpperCap", UNSET)
        vbr_upper_cap: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrUpperCap
        ]
        if isinstance(_vbr_upper_cap, Unset):
            vbr_upper_cap = UNSET
        else:
            vbr_upper_cap = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrUpperCap.from_dict(
                _vbr_upper_cap
            )

        _vbr_lower_cap = d.pop("vbrLowerCap", UNSET)
        vbr_lower_cap: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrLowerCap
        ]
        if isinstance(_vbr_lower_cap, Unset):
            vbr_lower_cap = UNSET
        else:
            vbr_lower_cap = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoVbrLowerCap.from_dict(
                _vbr_lower_cap
            )

        _max_frame_rate = d.pop("maxFrameRate", UNSET)
        max_frame_rate: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoMaxFrameRate
        ]
        if isinstance(_max_frame_rate, Unset):
            max_frame_rate = UNSET
        else:
            max_frame_rate = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoMaxFrameRate.from_dict(
                _max_frame_rate
            )

        key_frame_interval = d.pop("keyFrameInterval", UNSET)

        rotation_degree = d.pop("rotationDegree", UNSET)

        mirror_enabled = d.pop("mirrorEnabled", UNSET)

        snap_shot_image_type = d.pop("snapShotImageType", UNSET)

        mpeg_4_profile = d.pop("Mpeg4Profile", UNSET)

        h264_profile = d.pop("H264Profile", UNSET)

        svac_profile = d.pop("SVACProfile", UNSET)

        gov_length = d.pop("GovLength", UNSET)

        _svc = d.pop("SVC", UNSET)
        svc: Union[Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSVC]
        if isinstance(_svc, Unset):
            svc = UNSET
        else:
            svc = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSVC.from_dict(
                _svc
            )

        smoothing = d.pop("smoothing", UNSET)

        _smart_codec = d.pop("SmartCodec", UNSET)
        smart_codec: Union[
            Unset, RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSmartCodec
        ]
        if isinstance(_smart_codec, Unset):
            smart_codec = UNSET
        else:
            smart_codec = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoSmartCodec.from_dict(
                _smart_codec
            )

        vbr_average_cap = d.pop("vbrAverageCap", UNSET)

        _intelligent_info_display_method = d.pop("IntelligentInfoDisplayMethod", UNSET)
        intelligent_info_display_method: Union[
            Unset,
            RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoIntelligentInfoDisplayMethod,
        ]
        if isinstance(_intelligent_info_display_method, Unset):
            intelligent_info_display_method = UNSET
        else:
            intelligent_info_display_method = RootTypeForXMLStreamingChannelStreamingChannelCustomStreamEnableStreamingChannelVideoIntelligentInfoDisplayMethod.from_dict(
                _intelligent_info_display_method
            )

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video = cls(
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

        root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video.additional_properties = (
            d
        )
        return root_type_for_xml_streaming_channel_streaming_channel_custom_stream_enable_streaming_channel_video

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
