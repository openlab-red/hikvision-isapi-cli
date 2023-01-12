from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RootTypeForXMLStreamingChannelVideo")


@attr.s(auto_attribs=True)
class RootTypeForXMLStreamingChannelVideo:
    """
    Attributes:
        enabled (Union[Unset, str]):
        video_input_channel_id (Union[Unset, str]):
        video_codec_type (Union[Unset, str]):
        video_scan_type (Union[Unset, str]):
        video_resolution_width (Union[Unset, str]):
        video_resolution_height (Union[Unset, str]):
        video_quality_control_type (Union[Unset, str]):
        constant_bit_rate (Union[Unset, str]):
        fixed_quality (Union[Unset, str]):
        vbr_upper_cap (Union[Unset, str]):
        vbr_lower_cap (Union[Unset, str]):
        max_frame_rate (Union[Unset, str]):
        key_frame_interval (Union[Unset, str]):
        snap_shot_image_type (Union[Unset, str]):
        gov_length (Union[Unset, str]):
    """

    enabled: Union[Unset, str] = UNSET
    video_input_channel_id: Union[Unset, str] = UNSET
    video_codec_type: Union[Unset, str] = UNSET
    video_scan_type: Union[Unset, str] = UNSET
    video_resolution_width: Union[Unset, str] = UNSET
    video_resolution_height: Union[Unset, str] = UNSET
    video_quality_control_type: Union[Unset, str] = UNSET
    constant_bit_rate: Union[Unset, str] = UNSET
    fixed_quality: Union[Unset, str] = UNSET
    vbr_upper_cap: Union[Unset, str] = UNSET
    vbr_lower_cap: Union[Unset, str] = UNSET
    max_frame_rate: Union[Unset, str] = UNSET
    key_frame_interval: Union[Unset, str] = UNSET
    snap_shot_image_type: Union[Unset, str] = UNSET
    gov_length: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        video_input_channel_id = self.video_input_channel_id
        video_codec_type = self.video_codec_type
        video_scan_type = self.video_scan_type
        video_resolution_width = self.video_resolution_width
        video_resolution_height = self.video_resolution_height
        video_quality_control_type = self.video_quality_control_type
        constant_bit_rate = self.constant_bit_rate
        fixed_quality = self.fixed_quality
        vbr_upper_cap = self.vbr_upper_cap
        vbr_lower_cap = self.vbr_lower_cap
        max_frame_rate = self.max_frame_rate
        key_frame_interval = self.key_frame_interval
        snap_shot_image_type = self.snap_shot_image_type
        gov_length = self.gov_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if video_input_channel_id is not UNSET:
            field_dict["videoInputChannelID"] = video_input_channel_id
        if video_codec_type is not UNSET:
            field_dict["videoCodecType"] = video_codec_type
        if video_scan_type is not UNSET:
            field_dict["videoScanType"] = video_scan_type
        if video_resolution_width is not UNSET:
            field_dict["videoResolutionWidth"] = video_resolution_width
        if video_resolution_height is not UNSET:
            field_dict["videoResolutionHeight"] = video_resolution_height
        if video_quality_control_type is not UNSET:
            field_dict["videoQualityControlType"] = video_quality_control_type
        if constant_bit_rate is not UNSET:
            field_dict["constantBitRate"] = constant_bit_rate
        if fixed_quality is not UNSET:
            field_dict["fixedQuality"] = fixed_quality
        if vbr_upper_cap is not UNSET:
            field_dict["vbrUpperCap"] = vbr_upper_cap
        if vbr_lower_cap is not UNSET:
            field_dict["vbrLowerCap"] = vbr_lower_cap
        if max_frame_rate is not UNSET:
            field_dict["maxFrameRate"] = max_frame_rate
        if key_frame_interval is not UNSET:
            field_dict["keyFrameInterval"] = key_frame_interval
        if snap_shot_image_type is not UNSET:
            field_dict["snapShotImageType"] = snap_shot_image_type
        if gov_length is not UNSET:
            field_dict["GovLength"] = gov_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        video_input_channel_id = d.pop("videoInputChannelID", UNSET)

        video_codec_type = d.pop("videoCodecType", UNSET)

        video_scan_type = d.pop("videoScanType", UNSET)

        video_resolution_width = d.pop("videoResolutionWidth", UNSET)

        video_resolution_height = d.pop("videoResolutionHeight", UNSET)

        video_quality_control_type = d.pop("videoQualityControlType", UNSET)

        constant_bit_rate = d.pop("constantBitRate", UNSET)

        fixed_quality = d.pop("fixedQuality", UNSET)

        vbr_upper_cap = d.pop("vbrUpperCap", UNSET)

        vbr_lower_cap = d.pop("vbrLowerCap", UNSET)

        max_frame_rate = d.pop("maxFrameRate", UNSET)

        key_frame_interval = d.pop("keyFrameInterval", UNSET)

        snap_shot_image_type = d.pop("snapShotImageType", UNSET)

        gov_length = d.pop("GovLength", UNSET)

        root_type_for_xml_streaming_channel_video = cls(
            enabled=enabled,
            video_input_channel_id=video_input_channel_id,
            video_codec_type=video_codec_type,
            video_scan_type=video_scan_type,
            video_resolution_width=video_resolution_width,
            video_resolution_height=video_resolution_height,
            video_quality_control_type=video_quality_control_type,
            constant_bit_rate=constant_bit_rate,
            fixed_quality=fixed_quality,
            vbr_upper_cap=vbr_upper_cap,
            vbr_lower_cap=vbr_lower_cap,
            max_frame_rate=max_frame_rate,
            key_frame_interval=key_frame_interval,
            snap_shot_image_type=snap_shot_image_type,
            gov_length=gov_length,
        )

        root_type_for_xml_streaming_channel_video.additional_properties = d
        return root_type_for_xml_streaming_channel_video

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
