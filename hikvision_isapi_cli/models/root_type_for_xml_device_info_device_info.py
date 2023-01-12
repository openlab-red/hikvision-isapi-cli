from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus,
    )
    from ..models.root_type_for_xml_device_info_device_info_dock_station import (
        RootTypeForXMLDeviceInfoDeviceInfoDockStation,
    )
    from ..models.root_type_for_xml_device_info_device_info_is_reset_device_language import (
        RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage,
    )
    from ..models.root_type_for_xml_device_info_device_info_r3_version import (
        RootTypeForXMLDeviceInfoDeviceInfoR3Version,
    )
    from ..models.root_type_for_xml_device_info_device_info_rx_version import (
        RootTypeForXMLDeviceInfoDeviceInfoRxVersion,
    )
    from ..models.root_type_for_xml_device_info_device_info_uid_lamp_recognition import (
        RootTypeForXMLDeviceInfoDeviceInfoUIDLampRecognition,
    )
    from ..models.root_type_for_xml_device_info_device_info_zig_bee_version import (
        RootTypeForXMLDeviceInfoDeviceInfoZigBeeVersion,
    )


T = TypeVar("T", bound="RootTypeForXMLDeviceInfoDeviceInfo")


@attr.s(auto_attribs=True)
class RootTypeForXMLDeviceInfoDeviceInfo:
    """
    Attributes:
        device_name (Union[Unset, str]):
        device_id (Union[Unset, str]):
        device_description (Union[Unset, str]):
        device_location (Union[Unset, str]):
        device_status (Union[Unset, str]):
        detail_abnormal_status (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus]):
        system_contact (Union[Unset, str]):
        model (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        mac_address (Union[Unset, str]):
        firmware_version (Union[Unset, str]):
        firmware_released_date (Union[Unset, str]):
        boot_version (Union[Unset, str]):
        boot_released_date (Union[Unset, str]):
        hardware_version (Union[Unset, str]):
        encoder_version (Union[Unset, str]):
        encoder_released_date (Union[Unset, str]):
        decoder_version (Union[Unset, str]):
        decoder_released_date (Union[Unset, str]):
        software_version (Union[Unset, str]):
        capacity (Union[Unset, str]):
        used_capacity (Union[Unset, str]):
        device_type (Union[Unset, str]):
        telecontrol_id (Union[Unset, str]):
        support_beep (Union[Unset, str]):
        support_video_loss (Union[Unset, str]):
        firmware_version_info (Union[Unset, str]):
        actual_floor_num (Union[Unset, str]):
        sub_channel_enabled (Union[Unset, str]):
        thr_channel_enabled (Union[Unset, str]):
        radar_version (Union[Unset, str]):
        camera_module_version (Union[Unset, str]):
        mainversion (Union[Unset, str]):
        subversion (Union[Unset, str]):
        upgradeversion (Union[Unset, str]):
        customizeversion (Union[Unset, str]):
        company_name (Union[Unset, str]):
        copyright_ (Union[Unset, str]):
        system_name (Union[Unset, str]):
        system_status (Union[Unset, str]):
        is_leader_device (Union[Unset, str]):
        cluster_version (Union[Unset, str]):
        customized_info (Union[Unset, str]):
        local_zone_num (Union[Unset, str]):
        alarm_out_num (Union[Unset, str]):
        distance_resolution (Union[Unset, str]):
        angle_resolution (Union[Unset, str]):
        speed_resolution (Union[Unset, str]):
        detect_distance (Union[Unset, str]):
        language_type (Union[Unset, str]):
        relay_num (Union[Unset, str]):
        electro_lock_num (Union[Unset, str]):
        rs485_num (Union[Unset, str]):
        power_on_mode (Union[Unset, str]):
        dock_station (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDockStation]):
        web_version (Union[Unset, str]):
        device_rf_program_version (Union[Unset, str]):
        security_module_serial_no (Union[Unset, str]):
        security_module_version (Union[Unset, str]):
        security_chip_version (Union[Unset, str]):
        security_module_key_version (Union[Unset, str]):
        uid_lamp_recognition (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoUIDLampRecognition]):
        boot_time (Union[Unset, str]):
        zig_bee_version (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoZigBeeVersion]):
        r3_version (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoR3Version]):
        rx_version (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoRxVersion]):
        bsp_version (Union[Unset, str]):
        dsp_version (Union[Unset, str]):
        local_ui_version (Union[Unset, str]):
        is_reset_device_language (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    device_name: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_description: Union[Unset, str] = UNSET
    device_location: Union[Unset, str] = UNSET
    device_status: Union[Unset, str] = UNSET
    detail_abnormal_status: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus"] = UNSET
    system_contact: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    firmware_version: Union[Unset, str] = UNSET
    firmware_released_date: Union[Unset, str] = UNSET
    boot_version: Union[Unset, str] = UNSET
    boot_released_date: Union[Unset, str] = UNSET
    hardware_version: Union[Unset, str] = UNSET
    encoder_version: Union[Unset, str] = UNSET
    encoder_released_date: Union[Unset, str] = UNSET
    decoder_version: Union[Unset, str] = UNSET
    decoder_released_date: Union[Unset, str] = UNSET
    software_version: Union[Unset, str] = UNSET
    capacity: Union[Unset, str] = UNSET
    used_capacity: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    telecontrol_id: Union[Unset, str] = UNSET
    support_beep: Union[Unset, str] = UNSET
    support_video_loss: Union[Unset, str] = UNSET
    firmware_version_info: Union[Unset, str] = UNSET
    actual_floor_num: Union[Unset, str] = UNSET
    sub_channel_enabled: Union[Unset, str] = UNSET
    thr_channel_enabled: Union[Unset, str] = UNSET
    radar_version: Union[Unset, str] = UNSET
    camera_module_version: Union[Unset, str] = UNSET
    mainversion: Union[Unset, str] = UNSET
    subversion: Union[Unset, str] = UNSET
    upgradeversion: Union[Unset, str] = UNSET
    customizeversion: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    copyright_: Union[Unset, str] = UNSET
    system_name: Union[Unset, str] = UNSET
    system_status: Union[Unset, str] = UNSET
    is_leader_device: Union[Unset, str] = UNSET
    cluster_version: Union[Unset, str] = UNSET
    customized_info: Union[Unset, str] = UNSET
    local_zone_num: Union[Unset, str] = UNSET
    alarm_out_num: Union[Unset, str] = UNSET
    distance_resolution: Union[Unset, str] = UNSET
    angle_resolution: Union[Unset, str] = UNSET
    speed_resolution: Union[Unset, str] = UNSET
    detect_distance: Union[Unset, str] = UNSET
    language_type: Union[Unset, str] = UNSET
    relay_num: Union[Unset, str] = UNSET
    electro_lock_num: Union[Unset, str] = UNSET
    rs485_num: Union[Unset, str] = UNSET
    power_on_mode: Union[Unset, str] = UNSET
    dock_station: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDockStation"] = UNSET
    web_version: Union[Unset, str] = UNSET
    device_rf_program_version: Union[Unset, str] = UNSET
    security_module_serial_no: Union[Unset, str] = UNSET
    security_module_version: Union[Unset, str] = UNSET
    security_chip_version: Union[Unset, str] = UNSET
    security_module_key_version: Union[Unset, str] = UNSET
    uid_lamp_recognition: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoUIDLampRecognition"] = UNSET
    boot_time: Union[Unset, str] = UNSET
    zig_bee_version: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoZigBeeVersion"] = UNSET
    r3_version: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoR3Version"] = UNSET
    rx_version: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoRxVersion"] = UNSET
    bsp_version: Union[Unset, str] = UNSET
    dsp_version: Union[Unset, str] = UNSET
    local_ui_version: Union[Unset, str] = UNSET
    is_reset_device_language: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage"] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_name = self.device_name
        device_id = self.device_id
        device_description = self.device_description
        device_location = self.device_location
        device_status = self.device_status
        detail_abnormal_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.detail_abnormal_status, Unset):
            detail_abnormal_status = self.detail_abnormal_status.to_dict()

        system_contact = self.system_contact
        model = self.model
        serial_number = self.serial_number
        mac_address = self.mac_address
        firmware_version = self.firmware_version
        firmware_released_date = self.firmware_released_date
        boot_version = self.boot_version
        boot_released_date = self.boot_released_date
        hardware_version = self.hardware_version
        encoder_version = self.encoder_version
        encoder_released_date = self.encoder_released_date
        decoder_version = self.decoder_version
        decoder_released_date = self.decoder_released_date
        software_version = self.software_version
        capacity = self.capacity
        used_capacity = self.used_capacity
        device_type = self.device_type
        telecontrol_id = self.telecontrol_id
        support_beep = self.support_beep
        support_video_loss = self.support_video_loss
        firmware_version_info = self.firmware_version_info
        actual_floor_num = self.actual_floor_num
        sub_channel_enabled = self.sub_channel_enabled
        thr_channel_enabled = self.thr_channel_enabled
        radar_version = self.radar_version
        camera_module_version = self.camera_module_version
        mainversion = self.mainversion
        subversion = self.subversion
        upgradeversion = self.upgradeversion
        customizeversion = self.customizeversion
        company_name = self.company_name
        copyright_ = self.copyright_
        system_name = self.system_name
        system_status = self.system_status
        is_leader_device = self.is_leader_device
        cluster_version = self.cluster_version
        customized_info = self.customized_info
        local_zone_num = self.local_zone_num
        alarm_out_num = self.alarm_out_num
        distance_resolution = self.distance_resolution
        angle_resolution = self.angle_resolution
        speed_resolution = self.speed_resolution
        detect_distance = self.detect_distance
        language_type = self.language_type
        relay_num = self.relay_num
        electro_lock_num = self.electro_lock_num
        rs485_num = self.rs485_num
        power_on_mode = self.power_on_mode
        dock_station: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dock_station, Unset):
            dock_station = self.dock_station.to_dict()

        web_version = self.web_version
        device_rf_program_version = self.device_rf_program_version
        security_module_serial_no = self.security_module_serial_no
        security_module_version = self.security_module_version
        security_chip_version = self.security_chip_version
        security_module_key_version = self.security_module_key_version
        uid_lamp_recognition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.uid_lamp_recognition, Unset):
            uid_lamp_recognition = self.uid_lamp_recognition.to_dict()

        boot_time = self.boot_time
        zig_bee_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.zig_bee_version, Unset):
            zig_bee_version = self.zig_bee_version.to_dict()

        r3_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.r3_version, Unset):
            r3_version = self.r3_version.to_dict()

        rx_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rx_version, Unset):
            rx_version = self.rx_version.to_dict()

        bsp_version = self.bsp_version
        dsp_version = self.dsp_version
        local_ui_version = self.local_ui_version
        is_reset_device_language: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_reset_device_language, Unset):
            is_reset_device_language = self.is_reset_device_language.to_dict()

        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_id is not UNSET:
            field_dict["deviceID"] = device_id
        if device_description is not UNSET:
            field_dict["deviceDescription"] = device_description
        if device_location is not UNSET:
            field_dict["deviceLocation"] = device_location
        if device_status is not UNSET:
            field_dict["deviceStatus"] = device_status
        if detail_abnormal_status is not UNSET:
            field_dict["DetailAbnormalStatus"] = detail_abnormal_status
        if system_contact is not UNSET:
            field_dict["systemContact"] = system_contact
        if model is not UNSET:
            field_dict["model"] = model
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if firmware_released_date is not UNSET:
            field_dict["firmwareReleasedDate"] = firmware_released_date
        if boot_version is not UNSET:
            field_dict["bootVersion"] = boot_version
        if boot_released_date is not UNSET:
            field_dict["bootReleasedDate"] = boot_released_date
        if hardware_version is not UNSET:
            field_dict["hardwareVersion"] = hardware_version
        if encoder_version is not UNSET:
            field_dict["encoderVersion"] = encoder_version
        if encoder_released_date is not UNSET:
            field_dict["encoderReleasedDate"] = encoder_released_date
        if decoder_version is not UNSET:
            field_dict["decoderVersion"] = decoder_version
        if decoder_released_date is not UNSET:
            field_dict["decoderReleasedDate"] = decoder_released_date
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if used_capacity is not UNSET:
            field_dict["usedCapacity"] = used_capacity
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if telecontrol_id is not UNSET:
            field_dict["telecontrolID"] = telecontrol_id
        if support_beep is not UNSET:
            field_dict["supportBeep"] = support_beep
        if support_video_loss is not UNSET:
            field_dict["supportVideoLoss"] = support_video_loss
        if firmware_version_info is not UNSET:
            field_dict["firmwareVersionInfo"] = firmware_version_info
        if actual_floor_num is not UNSET:
            field_dict["actualFloorNum"] = actual_floor_num
        if sub_channel_enabled is not UNSET:
            field_dict["subChannelEnabled"] = sub_channel_enabled
        if thr_channel_enabled is not UNSET:
            field_dict["thrChannelEnabled"] = thr_channel_enabled
        if radar_version is not UNSET:
            field_dict["radarVersion"] = radar_version
        if camera_module_version is not UNSET:
            field_dict["cameraModuleVersion"] = camera_module_version
        if mainversion is not UNSET:
            field_dict["mainversion"] = mainversion
        if subversion is not UNSET:
            field_dict["subversion"] = subversion
        if upgradeversion is not UNSET:
            field_dict["upgradeversion"] = upgradeversion
        if customizeversion is not UNSET:
            field_dict["customizeversion"] = customizeversion
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if system_status is not UNSET:
            field_dict["systemStatus"] = system_status
        if is_leader_device is not UNSET:
            field_dict["isLeaderDevice"] = is_leader_device
        if cluster_version is not UNSET:
            field_dict["clusterVersion"] = cluster_version
        if customized_info is not UNSET:
            field_dict["customizedInfo"] = customized_info
        if local_zone_num is not UNSET:
            field_dict["localZoneNum"] = local_zone_num
        if alarm_out_num is not UNSET:
            field_dict["alarmOutNum"] = alarm_out_num
        if distance_resolution is not UNSET:
            field_dict["distanceResolution"] = distance_resolution
        if angle_resolution is not UNSET:
            field_dict["angleResolution"] = angle_resolution
        if speed_resolution is not UNSET:
            field_dict["speedResolution"] = speed_resolution
        if detect_distance is not UNSET:
            field_dict["detectDistance"] = detect_distance
        if language_type is not UNSET:
            field_dict["languageType"] = language_type
        if relay_num is not UNSET:
            field_dict["relayNum"] = relay_num
        if electro_lock_num is not UNSET:
            field_dict["electroLockNum"] = electro_lock_num
        if rs485_num is not UNSET:
            field_dict["RS485Num"] = rs485_num
        if power_on_mode is not UNSET:
            field_dict["powerOnMode"] = power_on_mode
        if dock_station is not UNSET:
            field_dict["DockStation"] = dock_station
        if web_version is not UNSET:
            field_dict["webVersion"] = web_version
        if device_rf_program_version is not UNSET:
            field_dict["deviceRFProgramVersion"] = device_rf_program_version
        if security_module_serial_no is not UNSET:
            field_dict["securityModuleSerialNo"] = security_module_serial_no
        if security_module_version is not UNSET:
            field_dict["securityModuleVersion"] = security_module_version
        if security_chip_version is not UNSET:
            field_dict["securityChipVersion"] = security_chip_version
        if security_module_key_version is not UNSET:
            field_dict["securityModuleKeyVersion"] = security_module_key_version
        if uid_lamp_recognition is not UNSET:
            field_dict["UIDLampRecognition"] = uid_lamp_recognition
        if boot_time is not UNSET:
            field_dict["bootTime"] = boot_time
        if zig_bee_version is not UNSET:
            field_dict["ZigBeeVersion"] = zig_bee_version
        if r3_version is not UNSET:
            field_dict["R3Version"] = r3_version
        if rx_version is not UNSET:
            field_dict["RxVersion"] = rx_version
        if bsp_version is not UNSET:
            field_dict["bspVersion"] = bsp_version
        if dsp_version is not UNSET:
            field_dict["dspVersion"] = dsp_version
        if local_ui_version is not UNSET:
            field_dict["localUIVersion"] = local_ui_version
        if is_reset_device_language is not UNSET:
            field_dict["isResetDeviceLanguage"] = is_reset_device_language
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus,
        )
        from ..models.root_type_for_xml_device_info_device_info_dock_station import (
            RootTypeForXMLDeviceInfoDeviceInfoDockStation,
        )
        from ..models.root_type_for_xml_device_info_device_info_is_reset_device_language import (
            RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage,
        )
        from ..models.root_type_for_xml_device_info_device_info_r3_version import (
            RootTypeForXMLDeviceInfoDeviceInfoR3Version,
        )
        from ..models.root_type_for_xml_device_info_device_info_rx_version import (
            RootTypeForXMLDeviceInfoDeviceInfoRxVersion,
        )
        from ..models.root_type_for_xml_device_info_device_info_uid_lamp_recognition import (
            RootTypeForXMLDeviceInfoDeviceInfoUIDLampRecognition,
        )
        from ..models.root_type_for_xml_device_info_device_info_zig_bee_version import (
            RootTypeForXMLDeviceInfoDeviceInfoZigBeeVersion,
        )

        d = src_dict.copy()
        device_name = d.pop("deviceName", UNSET)

        device_id = d.pop("deviceID", UNSET)

        device_description = d.pop("deviceDescription", UNSET)

        device_location = d.pop("deviceLocation", UNSET)

        device_status = d.pop("deviceStatus", UNSET)

        _detail_abnormal_status = d.pop("DetailAbnormalStatus", UNSET)
        detail_abnormal_status: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus]
        if isinstance(_detail_abnormal_status, Unset):
            detail_abnormal_status = UNSET
        else:
            detail_abnormal_status = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus.from_dict(
                _detail_abnormal_status
            )

        system_contact = d.pop("systemContact", UNSET)

        model = d.pop("model", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        firmware_released_date = d.pop("firmwareReleasedDate", UNSET)

        boot_version = d.pop("bootVersion", UNSET)

        boot_released_date = d.pop("bootReleasedDate", UNSET)

        hardware_version = d.pop("hardwareVersion", UNSET)

        encoder_version = d.pop("encoderVersion", UNSET)

        encoder_released_date = d.pop("encoderReleasedDate", UNSET)

        decoder_version = d.pop("decoderVersion", UNSET)

        decoder_released_date = d.pop("decoderReleasedDate", UNSET)

        software_version = d.pop("softwareVersion", UNSET)

        capacity = d.pop("capacity", UNSET)

        used_capacity = d.pop("usedCapacity", UNSET)

        device_type = d.pop("deviceType", UNSET)

        telecontrol_id = d.pop("telecontrolID", UNSET)

        support_beep = d.pop("supportBeep", UNSET)

        support_video_loss = d.pop("supportVideoLoss", UNSET)

        firmware_version_info = d.pop("firmwareVersionInfo", UNSET)

        actual_floor_num = d.pop("actualFloorNum", UNSET)

        sub_channel_enabled = d.pop("subChannelEnabled", UNSET)

        thr_channel_enabled = d.pop("thrChannelEnabled", UNSET)

        radar_version = d.pop("radarVersion", UNSET)

        camera_module_version = d.pop("cameraModuleVersion", UNSET)

        mainversion = d.pop("mainversion", UNSET)

        subversion = d.pop("subversion", UNSET)

        upgradeversion = d.pop("upgradeversion", UNSET)

        customizeversion = d.pop("customizeversion", UNSET)

        company_name = d.pop("companyName", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        system_name = d.pop("systemName", UNSET)

        system_status = d.pop("systemStatus", UNSET)

        is_leader_device = d.pop("isLeaderDevice", UNSET)

        cluster_version = d.pop("clusterVersion", UNSET)

        customized_info = d.pop("customizedInfo", UNSET)

        local_zone_num = d.pop("localZoneNum", UNSET)

        alarm_out_num = d.pop("alarmOutNum", UNSET)

        distance_resolution = d.pop("distanceResolution", UNSET)

        angle_resolution = d.pop("angleResolution", UNSET)

        speed_resolution = d.pop("speedResolution", UNSET)

        detect_distance = d.pop("detectDistance", UNSET)

        language_type = d.pop("languageType", UNSET)

        relay_num = d.pop("relayNum", UNSET)

        electro_lock_num = d.pop("electroLockNum", UNSET)

        rs485_num = d.pop("RS485Num", UNSET)

        power_on_mode = d.pop("powerOnMode", UNSET)

        _dock_station = d.pop("DockStation", UNSET)
        dock_station: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDockStation]
        if isinstance(_dock_station, Unset):
            dock_station = UNSET
        else:
            dock_station = RootTypeForXMLDeviceInfoDeviceInfoDockStation.from_dict(_dock_station)

        web_version = d.pop("webVersion", UNSET)

        device_rf_program_version = d.pop("deviceRFProgramVersion", UNSET)

        security_module_serial_no = d.pop("securityModuleSerialNo", UNSET)

        security_module_version = d.pop("securityModuleVersion", UNSET)

        security_chip_version = d.pop("securityChipVersion", UNSET)

        security_module_key_version = d.pop("securityModuleKeyVersion", UNSET)

        _uid_lamp_recognition = d.pop("UIDLampRecognition", UNSET)
        uid_lamp_recognition: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoUIDLampRecognition]
        if isinstance(_uid_lamp_recognition, Unset):
            uid_lamp_recognition = UNSET
        else:
            uid_lamp_recognition = RootTypeForXMLDeviceInfoDeviceInfoUIDLampRecognition.from_dict(_uid_lamp_recognition)

        boot_time = d.pop("bootTime", UNSET)

        _zig_bee_version = d.pop("ZigBeeVersion", UNSET)
        zig_bee_version: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoZigBeeVersion]
        if isinstance(_zig_bee_version, Unset):
            zig_bee_version = UNSET
        else:
            zig_bee_version = RootTypeForXMLDeviceInfoDeviceInfoZigBeeVersion.from_dict(_zig_bee_version)

        _r3_version = d.pop("R3Version", UNSET)
        r3_version: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoR3Version]
        if isinstance(_r3_version, Unset):
            r3_version = UNSET
        else:
            r3_version = RootTypeForXMLDeviceInfoDeviceInfoR3Version.from_dict(_r3_version)

        _rx_version = d.pop("RxVersion", UNSET)
        rx_version: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoRxVersion]
        if isinstance(_rx_version, Unset):
            rx_version = UNSET
        else:
            rx_version = RootTypeForXMLDeviceInfoDeviceInfoRxVersion.from_dict(_rx_version)

        bsp_version = d.pop("bspVersion", UNSET)

        dsp_version = d.pop("dspVersion", UNSET)

        local_ui_version = d.pop("localUIVersion", UNSET)

        _is_reset_device_language = d.pop("isResetDeviceLanguage", UNSET)
        is_reset_device_language: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage]
        if isinstance(_is_reset_device_language, Unset):
            is_reset_device_language = UNSET
        else:
            is_reset_device_language = RootTypeForXMLDeviceInfoDeviceInfoIsResetDeviceLanguage.from_dict(
                _is_reset_device_language
            )

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_device_info_device_info = cls(
            device_name=device_name,
            device_id=device_id,
            device_description=device_description,
            device_location=device_location,
            device_status=device_status,
            detail_abnormal_status=detail_abnormal_status,
            system_contact=system_contact,
            model=model,
            serial_number=serial_number,
            mac_address=mac_address,
            firmware_version=firmware_version,
            firmware_released_date=firmware_released_date,
            boot_version=boot_version,
            boot_released_date=boot_released_date,
            hardware_version=hardware_version,
            encoder_version=encoder_version,
            encoder_released_date=encoder_released_date,
            decoder_version=decoder_version,
            decoder_released_date=decoder_released_date,
            software_version=software_version,
            capacity=capacity,
            used_capacity=used_capacity,
            device_type=device_type,
            telecontrol_id=telecontrol_id,
            support_beep=support_beep,
            support_video_loss=support_video_loss,
            firmware_version_info=firmware_version_info,
            actual_floor_num=actual_floor_num,
            sub_channel_enabled=sub_channel_enabled,
            thr_channel_enabled=thr_channel_enabled,
            radar_version=radar_version,
            camera_module_version=camera_module_version,
            mainversion=mainversion,
            subversion=subversion,
            upgradeversion=upgradeversion,
            customizeversion=customizeversion,
            company_name=company_name,
            copyright_=copyright_,
            system_name=system_name,
            system_status=system_status,
            is_leader_device=is_leader_device,
            cluster_version=cluster_version,
            customized_info=customized_info,
            local_zone_num=local_zone_num,
            alarm_out_num=alarm_out_num,
            distance_resolution=distance_resolution,
            angle_resolution=angle_resolution,
            speed_resolution=speed_resolution,
            detect_distance=detect_distance,
            language_type=language_type,
            relay_num=relay_num,
            electro_lock_num=electro_lock_num,
            rs485_num=rs485_num,
            power_on_mode=power_on_mode,
            dock_station=dock_station,
            web_version=web_version,
            device_rf_program_version=device_rf_program_version,
            security_module_serial_no=security_module_serial_no,
            security_module_version=security_module_version,
            security_chip_version=security_chip_version,
            security_module_key_version=security_module_key_version,
            uid_lamp_recognition=uid_lamp_recognition,
            boot_time=boot_time,
            zig_bee_version=zig_bee_version,
            r3_version=r3_version,
            rx_version=rx_version,
            bsp_version=bsp_version,
            dsp_version=dsp_version,
            local_ui_version=local_ui_version,
            is_reset_device_language=is_reset_device_language,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_device_info_device_info.additional_properties = d
        return root_type_for_xml_device_info_device_info

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
