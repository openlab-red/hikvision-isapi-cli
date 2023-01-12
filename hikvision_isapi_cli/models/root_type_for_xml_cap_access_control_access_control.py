from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info import (
        RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_factory_reset import (
        RootTypeForXMLCapAccessControlAccessControlFactoryReset,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAcsCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_event import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEvent,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_event_total_num import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEventTotalNum,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_work_status import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAcsWorkStatus,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_anti_sneak_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAntiSneakCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_holiday_group import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayGroup,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_holiday_plan import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayPlan,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_rule import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceRule,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_status_mode_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusModeCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_status_rule_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusRuleCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_auth_code_info import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportAuthCodeInfo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_card_info import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureCardInfo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_face import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFace,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_finger_print import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFingerPrint,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_id_info import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureIDInfo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_infrared_face import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureInfraredFace,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_preset_param import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCapturePresetParam,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_rule import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureRule,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_operations import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCardOperations,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_reader_anti_sneak_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderAntiSneakCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_reader_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_reader_plan import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderPlan,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_right_holiday_plan_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightHolidayPlanCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_right_week_plan_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightWeekPlanCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_alarm_linkage import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmLinkage,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_alarm_out import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOut,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_alarm_out_control import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOutControl,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_type_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerTypeCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_anti_sneak import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneak,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_anti_sneak_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneakCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_card_record import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportClearCardRecord,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_event_card_linkage_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportClearEventCardLinkageCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_group_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportClearGroupCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_plans_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportClearPlansCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_submarine_back import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportClearSubmarineBack,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_department_param import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDepartmentParam,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_deploy_info_item import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDeployInfoItem,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDoorCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_holiday_group_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayGroupCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_holiday_plan_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayPlanCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_plan import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlan,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_plan_template import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlanTemplate,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_week_plan_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusWeekPlanCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_event_card_linkage_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardLinkageCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_event_card_no_list import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardNoList,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_event_optimization_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportEventOptimizationCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_face_recognize_mode import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportFaceRecognizeMode,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_finger_print_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_finger_print_delete import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintDelete,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_dial_and_info import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportGateDialAndInfo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_ir_status import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportGateIRStatus,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_related_parts_status import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportGateRelatedPartsStatus,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_status import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportGateStatus,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_group_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportGroupCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_identity_terminal import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportIdentityTerminal,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_ladder_control_relay import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportLadderControlRelay,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_log_mode_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportLogModeCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_m1_card_encrypt_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportM1CardEncryptCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_module_status import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportModuleStatus,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_multi_card_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportMultiCardCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_multi_door_inter_lock_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportMultiDoorInterLockCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_offline_capture import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportOfflineCapture,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_ordinary_class import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportOrdinaryClass,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_osdp_modify import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPModify,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_osdp_status import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPStatus,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_phone_door_right_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportPhoneDoorRightCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_reader_across_host import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportReaderAcrossHost,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_buzzer import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlBuzzer,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_door import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlDoor,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_pw_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_pw_chcek import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWChcek,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_right_controller_audio import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportRightControllerAudio,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_schedule_plan import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportSchedulePlan,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_server_device import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportServerDevice,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_sms_relative_param import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportSmsRelativeParam,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_snap_config import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportSNAPConfig,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_start_reader_info import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportStartReaderInfo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBack,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back_host_info import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackHostInfo,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back_mode import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackMode,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back_reader import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackReader,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_usb_manage import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportUSBManage,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_user_right_holiday_group_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightHolidayGroupCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_user_right_plan_template import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightPlanTemplate,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_holiday_group_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayGroupCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_holiday_plan_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayPlanCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_plan_template import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyPlanTemplate,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_week_plan_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyWeekPlanCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_wiegand_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_wiegand_rule_cfg import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandRuleCfg,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_is_support_working_class import (
        RootTypeForXMLCapAccessControlAccessControlIsSupportWorkingClass,
    )
    from ..models.root_type_for_xml_cap_access_control_access_control_local_controller import (
        RootTypeForXMLCapAccessControlAccessControlLocalController,
    )


T = TypeVar("T", bound="RootTypeForXMLCapAccessControlAccessControl")


@attr.s(auto_attribs=True)
class RootTypeForXMLCapAccessControlAccessControl:
    """
    Attributes:
        is_support_wiegand_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandCfg]):
        is_support_module_status (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportModuleStatus]):
        is_support_snap_config (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSNAPConfig]):
        local_controller (Union[Unset, RootTypeForXMLCapAccessControlAccessControlLocalController]):
        is_support_usb_manage (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportUSBManage]):
        is_support_identity_terminal (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportIdentityTerminal]):
        is_support_department_param (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDepartmentParam]):
        is_support_schedule_plan (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSchedulePlan]):
        is_support_attendance_rule (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceRule]):
        is_support_ordinary_class (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOrdinaryClass]):
        is_support_working_class (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportWorkingClass]):
        is_support_attendance_holiday_group (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayGroup]):
        is_support_attendance_holiday_plan (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayPlan]):
        is_support_ladder_control_relay (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportLadderControlRelay]):
        is_support_wiegand_rule_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandRuleCfg]):
        is_support_m1_card_encrypt_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportM1CardEncryptCfg]):
        is_support_deploy_info (Union[Unset,
            List['RootTypeForXMLCapAccessControlAccessControlIsSupportDeployInfoItem']]):
        is_support_submarine_back (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBack]):
        is_support_submarine_back_host_info (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackHostInfo]):
        is_support_start_reader_info (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportStartReaderInfo]):
        is_support_submarine_back_reader (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackReader]):
        is_support_server_device (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportServerDevice]):
        is_support_reader_across_host (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportReaderAcrossHost]):
        is_support_clear_card_record (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearCardRecord]):
        is_support_submarine_back_mode (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackMode]):
        is_support_clear_submarine_back (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearSubmarineBack]):
        is_support_remote_control_door (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlDoor]):
        is_support_user_info (Union[Unset, str]):
        employee_no_info (Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo]):
        is_support_card_info (Union[Unset, str]):
        is_support_user_info_detail_delete (Union[Unset, str]):
        is_support_auth_code_info (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAuthCodeInfo]):
        is_support_finger_print_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintCfg]):
        is_support_finger_print_delete (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintDelete]):
        is_support_capture_finger_print (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFingerPrint]):
        is_support_door_status_week_plan_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusWeekPlanCfg]):
        is_support_verify_week_plan_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyWeekPlanCfg]):
        is_support_card_right_week_plan_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightWeekPlanCfg]):
        is_support_door_status_holiday_plan_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayPlanCfg]):
        is_support_verify_holiday_plan_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayPlanCfg]):
        is_support_card_right_holiday_plan_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightHolidayPlanCfg]):
        is_support_door_status_holiday_group_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayGroupCfg]):
        is_support_verify_holiday_group_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayGroupCfg]):
        is_support_user_right_holiday_group_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightHolidayGroupCfg]):
        is_support_door_status_plan_template (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlanTemplate]):
        is_support_verify_plan_template (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyPlanTemplate]):
        is_support_user_right_plan_template (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightPlanTemplate]):
        is_support_door_status_plan (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlan]):
        is_support_card_reader_plan (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderPlan]):
        is_support_clear_plans_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearPlansCfg]):
        is_support_remote_control_buzzer (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlBuzzer]):
        is_support_event_card_no_list (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardNoList]):
        is_support_event_card_linkage_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardLinkageCfg]):
        is_support_clear_event_card_linkage_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearEventCardLinkageCfg]):
        is_support_acs_event (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEvent]):
        is_support_acs_event_total_num (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEventTotalNum]):
        is_support_event_optimization_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportEventOptimizationCfg]):
        is_support_acs_work_status (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAcsWorkStatus]):
        is_support_door_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorCfg]):
        is_support_card_reader_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderCfg]):
        is_support_acs_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAcsCfg]):
        is_support_group_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGroupCfg]):
        is_support_clear_group_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearGroupCfg]):
        is_support_multi_card_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportMultiCardCfg]):
        is_support_multi_door_inter_lock_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportMultiDoorInterLockCfg]):
        is_support_anti_sneak_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAntiSneakCfg]):
        is_support_card_reader_anti_sneak_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderAntiSneakCfg]):
        is_support_clear_anti_sneak_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneakCfg]):
        is_support_clear_anti_sneak (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneak]):
        is_support_sms_relative_param (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportSmsRelativeParam]):
        is_support_phone_door_right_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportPhoneDoorRightCfg]):
        is_support_osdp_status (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPStatus]):
        is_support_osdp_modify (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPModify]):
        is_support_log_mode_cfg (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportLogModeCfg]):
        factory_reset (Union[Unset, RootTypeForXMLCapAccessControlAccessControlFactoryReset]):
        is_support_nfc_cfg (Union[Unset, str]):
        is_support_rf_card_cfg (Union[Unset, str]):
        is_support_capture_face (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFace]):
        is_support_capture_infrared_face (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureInfraredFace]):
        is_support_face_recognize_mode (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportFaceRecognizeMode]):
        is_support_remote_control_pw_chcek (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWChcek]):
        is_support_remote_control_pw_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWCfg]):
        is_support_attendance_status_mode_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusModeCfg]):
        is_support_attendance_status_rule_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusRuleCfg]):
        is_support_capture_card_info (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureCardInfo]):
        is_support_capture_id_info (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureIDInfo]):
        is_support_capture_rule (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureRule]):
        is_support_capture_preset_param (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportCapturePresetParam]):
        is_support_offline_capture (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOfflineCapture]):
        is_support_card_operations (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardOperations]):
        is_support_right_controller_audio (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportRightControllerAudio]):
        is_support_channel_controller_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerCfg]):
        is_support_gate_dial_and_info (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportGateDialAndInfo]):
        is_support_gate_status (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGateStatus]):
        is_support_gate_ir_status (Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGateIRStatus]):
        is_support_gate_related_parts_status (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportGateRelatedPartsStatus]):
        is_support_channel_controller_alarm_linkage (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmLinkage]):
        is_support_channel_controller_alarm_out (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOut]):
        is_support_channel_controller_alarm_out_control (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOutControl]):
        is_support_channel_controller_type_cfg (Union[Unset,
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerTypeCfg]):
        is_support_tts_text (Union[Unset, str]):
        is_support_id_black_list_cfg (Union[Unset, str]):
        is_support_user_data_import (Union[Unset, str]):
        is_support_user_data_export (Union[Unset, str]):
        is_support_maintenance_data_export (Union[Unset, str]):
        is_support_lock_type_cfg (Union[Unset, str]):
        version (Union[Unset, str]):
        xmlns (Union[Unset, str]):
    """

    is_support_wiegand_cfg: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandCfg"] = UNSET
    is_support_module_status: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportModuleStatus"] = UNSET
    is_support_snap_config: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportSNAPConfig"] = UNSET
    local_controller: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlLocalController"] = UNSET
    is_support_usb_manage: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportUSBManage"] = UNSET
    is_support_identity_terminal: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportIdentityTerminal"
    ] = UNSET
    is_support_department_param: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportDepartmentParam"
    ] = UNSET
    is_support_schedule_plan: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportSchedulePlan"] = UNSET
    is_support_attendance_rule: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceRule"
    ] = UNSET
    is_support_ordinary_class: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportOrdinaryClass"] = UNSET
    is_support_working_class: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportWorkingClass"] = UNSET
    is_support_attendance_holiday_group: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayGroup"
    ] = UNSET
    is_support_attendance_holiday_plan: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayPlan"
    ] = UNSET
    is_support_ladder_control_relay: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportLadderControlRelay"
    ] = UNSET
    is_support_wiegand_rule_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandRuleCfg"
    ] = UNSET
    is_support_m1_card_encrypt_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportM1CardEncryptCfg"
    ] = UNSET
    is_support_deploy_info: Union[
        Unset, List["RootTypeForXMLCapAccessControlAccessControlIsSupportDeployInfoItem"]
    ] = UNSET
    is_support_submarine_back: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBack"] = UNSET
    is_support_submarine_back_host_info: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackHostInfo"
    ] = UNSET
    is_support_start_reader_info: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportStartReaderInfo"
    ] = UNSET
    is_support_submarine_back_reader: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackReader"
    ] = UNSET
    is_support_server_device: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportServerDevice"] = UNSET
    is_support_reader_across_host: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportReaderAcrossHost"
    ] = UNSET
    is_support_clear_card_record: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportClearCardRecord"
    ] = UNSET
    is_support_submarine_back_mode: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackMode"
    ] = UNSET
    is_support_clear_submarine_back: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportClearSubmarineBack"
    ] = UNSET
    is_support_remote_control_door: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlDoor"
    ] = UNSET
    is_support_user_info: Union[Unset, str] = UNSET
    employee_no_info: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo"] = UNSET
    is_support_card_info: Union[Unset, str] = UNSET
    is_support_user_info_detail_delete: Union[Unset, str] = UNSET
    is_support_auth_code_info: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAuthCodeInfo"] = UNSET
    is_support_finger_print_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintCfg"
    ] = UNSET
    is_support_finger_print_delete: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintDelete"
    ] = UNSET
    is_support_capture_finger_print: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFingerPrint"
    ] = UNSET
    is_support_door_status_week_plan_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusWeekPlanCfg"
    ] = UNSET
    is_support_verify_week_plan_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyWeekPlanCfg"
    ] = UNSET
    is_support_card_right_week_plan_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightWeekPlanCfg"
    ] = UNSET
    is_support_door_status_holiday_plan_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayPlanCfg"
    ] = UNSET
    is_support_verify_holiday_plan_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayPlanCfg"
    ] = UNSET
    is_support_card_right_holiday_plan_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightHolidayPlanCfg"
    ] = UNSET
    is_support_door_status_holiday_group_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayGroupCfg"
    ] = UNSET
    is_support_verify_holiday_group_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayGroupCfg"
    ] = UNSET
    is_support_user_right_holiday_group_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightHolidayGroupCfg"
    ] = UNSET
    is_support_door_status_plan_template: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlanTemplate"
    ] = UNSET
    is_support_verify_plan_template: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyPlanTemplate"
    ] = UNSET
    is_support_user_right_plan_template: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightPlanTemplate"
    ] = UNSET
    is_support_door_status_plan: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlan"
    ] = UNSET
    is_support_card_reader_plan: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderPlan"
    ] = UNSET
    is_support_clear_plans_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportClearPlansCfg"
    ] = UNSET
    is_support_remote_control_buzzer: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlBuzzer"
    ] = UNSET
    is_support_event_card_no_list: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardNoList"
    ] = UNSET
    is_support_event_card_linkage_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardLinkageCfg"
    ] = UNSET
    is_support_clear_event_card_linkage_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportClearEventCardLinkageCfg"
    ] = UNSET
    is_support_acs_event: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEvent"] = UNSET
    is_support_acs_event_total_num: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEventTotalNum"
    ] = UNSET
    is_support_event_optimization_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportEventOptimizationCfg"
    ] = UNSET
    is_support_acs_work_status: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAcsWorkStatus"
    ] = UNSET
    is_support_door_cfg: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportDoorCfg"] = UNSET
    is_support_card_reader_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderCfg"
    ] = UNSET
    is_support_acs_cfg: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAcsCfg"] = UNSET
    is_support_group_cfg: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportGroupCfg"] = UNSET
    is_support_clear_group_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportClearGroupCfg"
    ] = UNSET
    is_support_multi_card_cfg: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportMultiCardCfg"] = UNSET
    is_support_multi_door_inter_lock_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportMultiDoorInterLockCfg"
    ] = UNSET
    is_support_anti_sneak_cfg: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAntiSneakCfg"] = UNSET
    is_support_card_reader_anti_sneak_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderAntiSneakCfg"
    ] = UNSET
    is_support_clear_anti_sneak_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneakCfg"
    ] = UNSET
    is_support_clear_anti_sneak: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneak"
    ] = UNSET
    is_support_sms_relative_param: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportSmsRelativeParam"
    ] = UNSET
    is_support_phone_door_right_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportPhoneDoorRightCfg"
    ] = UNSET
    is_support_osdp_status: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPStatus"] = UNSET
    is_support_osdp_modify: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPModify"] = UNSET
    is_support_log_mode_cfg: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportLogModeCfg"] = UNSET
    factory_reset: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlFactoryReset"] = UNSET
    is_support_nfc_cfg: Union[Unset, str] = UNSET
    is_support_rf_card_cfg: Union[Unset, str] = UNSET
    is_support_capture_face: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFace"] = UNSET
    is_support_capture_infrared_face: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureInfraredFace"
    ] = UNSET
    is_support_face_recognize_mode: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportFaceRecognizeMode"
    ] = UNSET
    is_support_remote_control_pw_chcek: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWChcek"
    ] = UNSET
    is_support_remote_control_pw_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWCfg"
    ] = UNSET
    is_support_attendance_status_mode_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusModeCfg"
    ] = UNSET
    is_support_attendance_status_rule_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusRuleCfg"
    ] = UNSET
    is_support_capture_card_info: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureCardInfo"
    ] = UNSET
    is_support_capture_id_info: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureIDInfo"
    ] = UNSET
    is_support_capture_rule: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureRule"] = UNSET
    is_support_capture_preset_param: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCapturePresetParam"
    ] = UNSET
    is_support_offline_capture: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportOfflineCapture"
    ] = UNSET
    is_support_card_operations: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportCardOperations"
    ] = UNSET
    is_support_right_controller_audio: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportRightControllerAudio"
    ] = UNSET
    is_support_channel_controller_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerCfg"
    ] = UNSET
    is_support_gate_dial_and_info: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportGateDialAndInfo"
    ] = UNSET
    is_support_gate_status: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportGateStatus"] = UNSET
    is_support_gate_ir_status: Union[Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportGateIRStatus"] = UNSET
    is_support_gate_related_parts_status: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportGateRelatedPartsStatus"
    ] = UNSET
    is_support_channel_controller_alarm_linkage: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmLinkage"
    ] = UNSET
    is_support_channel_controller_alarm_out: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOut"
    ] = UNSET
    is_support_channel_controller_alarm_out_control: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOutControl"
    ] = UNSET
    is_support_channel_controller_type_cfg: Union[
        Unset, "RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerTypeCfg"
    ] = UNSET
    is_support_tts_text: Union[Unset, str] = UNSET
    is_support_id_black_list_cfg: Union[Unset, str] = UNSET
    is_support_user_data_import: Union[Unset, str] = UNSET
    is_support_user_data_export: Union[Unset, str] = UNSET
    is_support_maintenance_data_export: Union[Unset, str] = UNSET
    is_support_lock_type_cfg: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    xmlns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_support_wiegand_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_wiegand_cfg, Unset):
            is_support_wiegand_cfg = self.is_support_wiegand_cfg.to_dict()

        is_support_module_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_module_status, Unset):
            is_support_module_status = self.is_support_module_status.to_dict()

        is_support_snap_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_snap_config, Unset):
            is_support_snap_config = self.is_support_snap_config.to_dict()

        local_controller: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_controller, Unset):
            local_controller = self.local_controller.to_dict()

        is_support_usb_manage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_usb_manage, Unset):
            is_support_usb_manage = self.is_support_usb_manage.to_dict()

        is_support_identity_terminal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_identity_terminal, Unset):
            is_support_identity_terminal = self.is_support_identity_terminal.to_dict()

        is_support_department_param: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_department_param, Unset):
            is_support_department_param = self.is_support_department_param.to_dict()

        is_support_schedule_plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_schedule_plan, Unset):
            is_support_schedule_plan = self.is_support_schedule_plan.to_dict()

        is_support_attendance_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_attendance_rule, Unset):
            is_support_attendance_rule = self.is_support_attendance_rule.to_dict()

        is_support_ordinary_class: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_ordinary_class, Unset):
            is_support_ordinary_class = self.is_support_ordinary_class.to_dict()

        is_support_working_class: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_working_class, Unset):
            is_support_working_class = self.is_support_working_class.to_dict()

        is_support_attendance_holiday_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_attendance_holiday_group, Unset):
            is_support_attendance_holiday_group = self.is_support_attendance_holiday_group.to_dict()

        is_support_attendance_holiday_plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_attendance_holiday_plan, Unset):
            is_support_attendance_holiday_plan = self.is_support_attendance_holiday_plan.to_dict()

        is_support_ladder_control_relay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_ladder_control_relay, Unset):
            is_support_ladder_control_relay = self.is_support_ladder_control_relay.to_dict()

        is_support_wiegand_rule_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_wiegand_rule_cfg, Unset):
            is_support_wiegand_rule_cfg = self.is_support_wiegand_rule_cfg.to_dict()

        is_support_m1_card_encrypt_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_m1_card_encrypt_cfg, Unset):
            is_support_m1_card_encrypt_cfg = self.is_support_m1_card_encrypt_cfg.to_dict()

        is_support_deploy_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.is_support_deploy_info, Unset):
            is_support_deploy_info = []
            for is_support_deploy_info_item_data in self.is_support_deploy_info:
                is_support_deploy_info_item = is_support_deploy_info_item_data.to_dict()

                is_support_deploy_info.append(is_support_deploy_info_item)

        is_support_submarine_back: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_submarine_back, Unset):
            is_support_submarine_back = self.is_support_submarine_back.to_dict()

        is_support_submarine_back_host_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_submarine_back_host_info, Unset):
            is_support_submarine_back_host_info = self.is_support_submarine_back_host_info.to_dict()

        is_support_start_reader_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_start_reader_info, Unset):
            is_support_start_reader_info = self.is_support_start_reader_info.to_dict()

        is_support_submarine_back_reader: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_submarine_back_reader, Unset):
            is_support_submarine_back_reader = self.is_support_submarine_back_reader.to_dict()

        is_support_server_device: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_server_device, Unset):
            is_support_server_device = self.is_support_server_device.to_dict()

        is_support_reader_across_host: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_reader_across_host, Unset):
            is_support_reader_across_host = self.is_support_reader_across_host.to_dict()

        is_support_clear_card_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_clear_card_record, Unset):
            is_support_clear_card_record = self.is_support_clear_card_record.to_dict()

        is_support_submarine_back_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_submarine_back_mode, Unset):
            is_support_submarine_back_mode = self.is_support_submarine_back_mode.to_dict()

        is_support_clear_submarine_back: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_clear_submarine_back, Unset):
            is_support_clear_submarine_back = self.is_support_clear_submarine_back.to_dict()

        is_support_remote_control_door: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_remote_control_door, Unset):
            is_support_remote_control_door = self.is_support_remote_control_door.to_dict()

        is_support_user_info = self.is_support_user_info
        employee_no_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employee_no_info, Unset):
            employee_no_info = self.employee_no_info.to_dict()

        is_support_card_info = self.is_support_card_info
        is_support_user_info_detail_delete = self.is_support_user_info_detail_delete
        is_support_auth_code_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_auth_code_info, Unset):
            is_support_auth_code_info = self.is_support_auth_code_info.to_dict()

        is_support_finger_print_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_finger_print_cfg, Unset):
            is_support_finger_print_cfg = self.is_support_finger_print_cfg.to_dict()

        is_support_finger_print_delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_finger_print_delete, Unset):
            is_support_finger_print_delete = self.is_support_finger_print_delete.to_dict()

        is_support_capture_finger_print: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_capture_finger_print, Unset):
            is_support_capture_finger_print = self.is_support_capture_finger_print.to_dict()

        is_support_door_status_week_plan_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_door_status_week_plan_cfg, Unset):
            is_support_door_status_week_plan_cfg = self.is_support_door_status_week_plan_cfg.to_dict()

        is_support_verify_week_plan_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_verify_week_plan_cfg, Unset):
            is_support_verify_week_plan_cfg = self.is_support_verify_week_plan_cfg.to_dict()

        is_support_card_right_week_plan_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_card_right_week_plan_cfg, Unset):
            is_support_card_right_week_plan_cfg = self.is_support_card_right_week_plan_cfg.to_dict()

        is_support_door_status_holiday_plan_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_door_status_holiday_plan_cfg, Unset):
            is_support_door_status_holiday_plan_cfg = self.is_support_door_status_holiday_plan_cfg.to_dict()

        is_support_verify_holiday_plan_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_verify_holiday_plan_cfg, Unset):
            is_support_verify_holiday_plan_cfg = self.is_support_verify_holiday_plan_cfg.to_dict()

        is_support_card_right_holiday_plan_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_card_right_holiday_plan_cfg, Unset):
            is_support_card_right_holiday_plan_cfg = self.is_support_card_right_holiday_plan_cfg.to_dict()

        is_support_door_status_holiday_group_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_door_status_holiday_group_cfg, Unset):
            is_support_door_status_holiday_group_cfg = self.is_support_door_status_holiday_group_cfg.to_dict()

        is_support_verify_holiday_group_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_verify_holiday_group_cfg, Unset):
            is_support_verify_holiday_group_cfg = self.is_support_verify_holiday_group_cfg.to_dict()

        is_support_user_right_holiday_group_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_user_right_holiday_group_cfg, Unset):
            is_support_user_right_holiday_group_cfg = self.is_support_user_right_holiday_group_cfg.to_dict()

        is_support_door_status_plan_template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_door_status_plan_template, Unset):
            is_support_door_status_plan_template = self.is_support_door_status_plan_template.to_dict()

        is_support_verify_plan_template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_verify_plan_template, Unset):
            is_support_verify_plan_template = self.is_support_verify_plan_template.to_dict()

        is_support_user_right_plan_template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_user_right_plan_template, Unset):
            is_support_user_right_plan_template = self.is_support_user_right_plan_template.to_dict()

        is_support_door_status_plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_door_status_plan, Unset):
            is_support_door_status_plan = self.is_support_door_status_plan.to_dict()

        is_support_card_reader_plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_card_reader_plan, Unset):
            is_support_card_reader_plan = self.is_support_card_reader_plan.to_dict()

        is_support_clear_plans_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_clear_plans_cfg, Unset):
            is_support_clear_plans_cfg = self.is_support_clear_plans_cfg.to_dict()

        is_support_remote_control_buzzer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_remote_control_buzzer, Unset):
            is_support_remote_control_buzzer = self.is_support_remote_control_buzzer.to_dict()

        is_support_event_card_no_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_event_card_no_list, Unset):
            is_support_event_card_no_list = self.is_support_event_card_no_list.to_dict()

        is_support_event_card_linkage_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_event_card_linkage_cfg, Unset):
            is_support_event_card_linkage_cfg = self.is_support_event_card_linkage_cfg.to_dict()

        is_support_clear_event_card_linkage_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_clear_event_card_linkage_cfg, Unset):
            is_support_clear_event_card_linkage_cfg = self.is_support_clear_event_card_linkage_cfg.to_dict()

        is_support_acs_event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_acs_event, Unset):
            is_support_acs_event = self.is_support_acs_event.to_dict()

        is_support_acs_event_total_num: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_acs_event_total_num, Unset):
            is_support_acs_event_total_num = self.is_support_acs_event_total_num.to_dict()

        is_support_event_optimization_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_event_optimization_cfg, Unset):
            is_support_event_optimization_cfg = self.is_support_event_optimization_cfg.to_dict()

        is_support_acs_work_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_acs_work_status, Unset):
            is_support_acs_work_status = self.is_support_acs_work_status.to_dict()

        is_support_door_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_door_cfg, Unset):
            is_support_door_cfg = self.is_support_door_cfg.to_dict()

        is_support_card_reader_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_card_reader_cfg, Unset):
            is_support_card_reader_cfg = self.is_support_card_reader_cfg.to_dict()

        is_support_acs_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_acs_cfg, Unset):
            is_support_acs_cfg = self.is_support_acs_cfg.to_dict()

        is_support_group_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_group_cfg, Unset):
            is_support_group_cfg = self.is_support_group_cfg.to_dict()

        is_support_clear_group_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_clear_group_cfg, Unset):
            is_support_clear_group_cfg = self.is_support_clear_group_cfg.to_dict()

        is_support_multi_card_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_multi_card_cfg, Unset):
            is_support_multi_card_cfg = self.is_support_multi_card_cfg.to_dict()

        is_support_multi_door_inter_lock_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_multi_door_inter_lock_cfg, Unset):
            is_support_multi_door_inter_lock_cfg = self.is_support_multi_door_inter_lock_cfg.to_dict()

        is_support_anti_sneak_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_anti_sneak_cfg, Unset):
            is_support_anti_sneak_cfg = self.is_support_anti_sneak_cfg.to_dict()

        is_support_card_reader_anti_sneak_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_card_reader_anti_sneak_cfg, Unset):
            is_support_card_reader_anti_sneak_cfg = self.is_support_card_reader_anti_sneak_cfg.to_dict()

        is_support_clear_anti_sneak_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_clear_anti_sneak_cfg, Unset):
            is_support_clear_anti_sneak_cfg = self.is_support_clear_anti_sneak_cfg.to_dict()

        is_support_clear_anti_sneak: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_clear_anti_sneak, Unset):
            is_support_clear_anti_sneak = self.is_support_clear_anti_sneak.to_dict()

        is_support_sms_relative_param: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_sms_relative_param, Unset):
            is_support_sms_relative_param = self.is_support_sms_relative_param.to_dict()

        is_support_phone_door_right_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_phone_door_right_cfg, Unset):
            is_support_phone_door_right_cfg = self.is_support_phone_door_right_cfg.to_dict()

        is_support_osdp_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_osdp_status, Unset):
            is_support_osdp_status = self.is_support_osdp_status.to_dict()

        is_support_osdp_modify: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_osdp_modify, Unset):
            is_support_osdp_modify = self.is_support_osdp_modify.to_dict()

        is_support_log_mode_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_log_mode_cfg, Unset):
            is_support_log_mode_cfg = self.is_support_log_mode_cfg.to_dict()

        factory_reset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.factory_reset, Unset):
            factory_reset = self.factory_reset.to_dict()

        is_support_nfc_cfg = self.is_support_nfc_cfg
        is_support_rf_card_cfg = self.is_support_rf_card_cfg
        is_support_capture_face: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_capture_face, Unset):
            is_support_capture_face = self.is_support_capture_face.to_dict()

        is_support_capture_infrared_face: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_capture_infrared_face, Unset):
            is_support_capture_infrared_face = self.is_support_capture_infrared_face.to_dict()

        is_support_face_recognize_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_face_recognize_mode, Unset):
            is_support_face_recognize_mode = self.is_support_face_recognize_mode.to_dict()

        is_support_remote_control_pw_chcek: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_remote_control_pw_chcek, Unset):
            is_support_remote_control_pw_chcek = self.is_support_remote_control_pw_chcek.to_dict()

        is_support_remote_control_pw_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_remote_control_pw_cfg, Unset):
            is_support_remote_control_pw_cfg = self.is_support_remote_control_pw_cfg.to_dict()

        is_support_attendance_status_mode_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_attendance_status_mode_cfg, Unset):
            is_support_attendance_status_mode_cfg = self.is_support_attendance_status_mode_cfg.to_dict()

        is_support_attendance_status_rule_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_attendance_status_rule_cfg, Unset):
            is_support_attendance_status_rule_cfg = self.is_support_attendance_status_rule_cfg.to_dict()

        is_support_capture_card_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_capture_card_info, Unset):
            is_support_capture_card_info = self.is_support_capture_card_info.to_dict()

        is_support_capture_id_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_capture_id_info, Unset):
            is_support_capture_id_info = self.is_support_capture_id_info.to_dict()

        is_support_capture_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_capture_rule, Unset):
            is_support_capture_rule = self.is_support_capture_rule.to_dict()

        is_support_capture_preset_param: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_capture_preset_param, Unset):
            is_support_capture_preset_param = self.is_support_capture_preset_param.to_dict()

        is_support_offline_capture: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_offline_capture, Unset):
            is_support_offline_capture = self.is_support_offline_capture.to_dict()

        is_support_card_operations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_card_operations, Unset):
            is_support_card_operations = self.is_support_card_operations.to_dict()

        is_support_right_controller_audio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_right_controller_audio, Unset):
            is_support_right_controller_audio = self.is_support_right_controller_audio.to_dict()

        is_support_channel_controller_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_channel_controller_cfg, Unset):
            is_support_channel_controller_cfg = self.is_support_channel_controller_cfg.to_dict()

        is_support_gate_dial_and_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_gate_dial_and_info, Unset):
            is_support_gate_dial_and_info = self.is_support_gate_dial_and_info.to_dict()

        is_support_gate_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_gate_status, Unset):
            is_support_gate_status = self.is_support_gate_status.to_dict()

        is_support_gate_ir_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_gate_ir_status, Unset):
            is_support_gate_ir_status = self.is_support_gate_ir_status.to_dict()

        is_support_gate_related_parts_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_gate_related_parts_status, Unset):
            is_support_gate_related_parts_status = self.is_support_gate_related_parts_status.to_dict()

        is_support_channel_controller_alarm_linkage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_channel_controller_alarm_linkage, Unset):
            is_support_channel_controller_alarm_linkage = self.is_support_channel_controller_alarm_linkage.to_dict()

        is_support_channel_controller_alarm_out: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_channel_controller_alarm_out, Unset):
            is_support_channel_controller_alarm_out = self.is_support_channel_controller_alarm_out.to_dict()

        is_support_channel_controller_alarm_out_control: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_channel_controller_alarm_out_control, Unset):
            is_support_channel_controller_alarm_out_control = (
                self.is_support_channel_controller_alarm_out_control.to_dict()
            )

        is_support_channel_controller_type_cfg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_support_channel_controller_type_cfg, Unset):
            is_support_channel_controller_type_cfg = self.is_support_channel_controller_type_cfg.to_dict()

        is_support_tts_text = self.is_support_tts_text
        is_support_id_black_list_cfg = self.is_support_id_black_list_cfg
        is_support_user_data_import = self.is_support_user_data_import
        is_support_user_data_export = self.is_support_user_data_export
        is_support_maintenance_data_export = self.is_support_maintenance_data_export
        is_support_lock_type_cfg = self.is_support_lock_type_cfg
        version = self.version
        xmlns = self.xmlns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_support_wiegand_cfg is not UNSET:
            field_dict["isSupportWiegandCfg"] = is_support_wiegand_cfg
        if is_support_module_status is not UNSET:
            field_dict["isSupportModuleStatus"] = is_support_module_status
        if is_support_snap_config is not UNSET:
            field_dict["isSupportSNAPConfig"] = is_support_snap_config
        if local_controller is not UNSET:
            field_dict["LocalController"] = local_controller
        if is_support_usb_manage is not UNSET:
            field_dict["isSupportUSBManage"] = is_support_usb_manage
        if is_support_identity_terminal is not UNSET:
            field_dict["isSupportIdentityTerminal"] = is_support_identity_terminal
        if is_support_department_param is not UNSET:
            field_dict["isSupportDepartmentParam"] = is_support_department_param
        if is_support_schedule_plan is not UNSET:
            field_dict["isSupportSchedulePlan"] = is_support_schedule_plan
        if is_support_attendance_rule is not UNSET:
            field_dict["isSupportAttendanceRule"] = is_support_attendance_rule
        if is_support_ordinary_class is not UNSET:
            field_dict["isSupportOrdinaryClass"] = is_support_ordinary_class
        if is_support_working_class is not UNSET:
            field_dict["isSupportWorkingClass"] = is_support_working_class
        if is_support_attendance_holiday_group is not UNSET:
            field_dict["isSupportAttendanceHolidayGroup"] = is_support_attendance_holiday_group
        if is_support_attendance_holiday_plan is not UNSET:
            field_dict["isSupportAttendanceHolidayPlan"] = is_support_attendance_holiday_plan
        if is_support_ladder_control_relay is not UNSET:
            field_dict["isSupportLadderControlRelay"] = is_support_ladder_control_relay
        if is_support_wiegand_rule_cfg is not UNSET:
            field_dict["isSupportWiegandRuleCfg"] = is_support_wiegand_rule_cfg
        if is_support_m1_card_encrypt_cfg is not UNSET:
            field_dict["isSupportM1CardEncryptCfg"] = is_support_m1_card_encrypt_cfg
        if is_support_deploy_info is not UNSET:
            field_dict["isSupportDeployInfo"] = is_support_deploy_info
        if is_support_submarine_back is not UNSET:
            field_dict["isSupportSubmarineBack"] = is_support_submarine_back
        if is_support_submarine_back_host_info is not UNSET:
            field_dict["isSupportSubmarineBackHostInfo"] = is_support_submarine_back_host_info
        if is_support_start_reader_info is not UNSET:
            field_dict["isSupportStartReaderInfo"] = is_support_start_reader_info
        if is_support_submarine_back_reader is not UNSET:
            field_dict["isSupportSubmarineBackReader"] = is_support_submarine_back_reader
        if is_support_server_device is not UNSET:
            field_dict["isSupportServerDevice"] = is_support_server_device
        if is_support_reader_across_host is not UNSET:
            field_dict["isSupportReaderAcrossHost"] = is_support_reader_across_host
        if is_support_clear_card_record is not UNSET:
            field_dict["isSupportClearCardRecord"] = is_support_clear_card_record
        if is_support_submarine_back_mode is not UNSET:
            field_dict["isSupportSubmarineBackMode"] = is_support_submarine_back_mode
        if is_support_clear_submarine_back is not UNSET:
            field_dict["isSupportClearSubmarineBack"] = is_support_clear_submarine_back
        if is_support_remote_control_door is not UNSET:
            field_dict["isSupportRemoteControlDoor"] = is_support_remote_control_door
        if is_support_user_info is not UNSET:
            field_dict["isSupportUserInfo"] = is_support_user_info
        if employee_no_info is not UNSET:
            field_dict["EmployeeNoInfo"] = employee_no_info
        if is_support_card_info is not UNSET:
            field_dict["isSupportCardInfo"] = is_support_card_info
        if is_support_user_info_detail_delete is not UNSET:
            field_dict["isSupportUserInfoDetailDelete"] = is_support_user_info_detail_delete
        if is_support_auth_code_info is not UNSET:
            field_dict["isSupportAuthCodeInfo"] = is_support_auth_code_info
        if is_support_finger_print_cfg is not UNSET:
            field_dict["isSupportFingerPrintCfg"] = is_support_finger_print_cfg
        if is_support_finger_print_delete is not UNSET:
            field_dict["isSupportFingerPrintDelete"] = is_support_finger_print_delete
        if is_support_capture_finger_print is not UNSET:
            field_dict["isSupportCaptureFingerPrint"] = is_support_capture_finger_print
        if is_support_door_status_week_plan_cfg is not UNSET:
            field_dict["isSupportDoorStatusWeekPlanCfg"] = is_support_door_status_week_plan_cfg
        if is_support_verify_week_plan_cfg is not UNSET:
            field_dict["isSupportVerifyWeekPlanCfg"] = is_support_verify_week_plan_cfg
        if is_support_card_right_week_plan_cfg is not UNSET:
            field_dict["isSupportCardRightWeekPlanCfg"] = is_support_card_right_week_plan_cfg
        if is_support_door_status_holiday_plan_cfg is not UNSET:
            field_dict["isSupportDoorStatusHolidayPlanCfg"] = is_support_door_status_holiday_plan_cfg
        if is_support_verify_holiday_plan_cfg is not UNSET:
            field_dict["isSupportVerifyHolidayPlanCfg"] = is_support_verify_holiday_plan_cfg
        if is_support_card_right_holiday_plan_cfg is not UNSET:
            field_dict["isSupportCardRightHolidayPlanCfg"] = is_support_card_right_holiday_plan_cfg
        if is_support_door_status_holiday_group_cfg is not UNSET:
            field_dict["isSupportDoorStatusHolidayGroupCfg"] = is_support_door_status_holiday_group_cfg
        if is_support_verify_holiday_group_cfg is not UNSET:
            field_dict["isSupportVerifyHolidayGroupCfg"] = is_support_verify_holiday_group_cfg
        if is_support_user_right_holiday_group_cfg is not UNSET:
            field_dict["isSupportUserRightHolidayGroupCfg"] = is_support_user_right_holiday_group_cfg
        if is_support_door_status_plan_template is not UNSET:
            field_dict["isSupportDoorStatusPlanTemplate"] = is_support_door_status_plan_template
        if is_support_verify_plan_template is not UNSET:
            field_dict["isSupportVerifyPlanTemplate"] = is_support_verify_plan_template
        if is_support_user_right_plan_template is not UNSET:
            field_dict["isSupportUserRightPlanTemplate"] = is_support_user_right_plan_template
        if is_support_door_status_plan is not UNSET:
            field_dict["isSupportDoorStatusPlan"] = is_support_door_status_plan
        if is_support_card_reader_plan is not UNSET:
            field_dict["isSupportCardReaderPlan"] = is_support_card_reader_plan
        if is_support_clear_plans_cfg is not UNSET:
            field_dict["isSupportClearPlansCfg"] = is_support_clear_plans_cfg
        if is_support_remote_control_buzzer is not UNSET:
            field_dict["isSupportRemoteControlBuzzer"] = is_support_remote_control_buzzer
        if is_support_event_card_no_list is not UNSET:
            field_dict["isSupportEventCardNoList"] = is_support_event_card_no_list
        if is_support_event_card_linkage_cfg is not UNSET:
            field_dict["isSupportEventCardLinkageCfg"] = is_support_event_card_linkage_cfg
        if is_support_clear_event_card_linkage_cfg is not UNSET:
            field_dict["isSupportClearEventCardLinkageCfg"] = is_support_clear_event_card_linkage_cfg
        if is_support_acs_event is not UNSET:
            field_dict["isSupportAcsEvent"] = is_support_acs_event
        if is_support_acs_event_total_num is not UNSET:
            field_dict["isSupportAcsEventTotalNum"] = is_support_acs_event_total_num
        if is_support_event_optimization_cfg is not UNSET:
            field_dict["isSupportEventOptimizationCfg"] = is_support_event_optimization_cfg
        if is_support_acs_work_status is not UNSET:
            field_dict["isSupportAcsWorkStatus"] = is_support_acs_work_status
        if is_support_door_cfg is not UNSET:
            field_dict["isSupportDoorCfg"] = is_support_door_cfg
        if is_support_card_reader_cfg is not UNSET:
            field_dict["isSupportCardReaderCfg"] = is_support_card_reader_cfg
        if is_support_acs_cfg is not UNSET:
            field_dict["isSupportAcsCfg"] = is_support_acs_cfg
        if is_support_group_cfg is not UNSET:
            field_dict["isSupportGroupCfg"] = is_support_group_cfg
        if is_support_clear_group_cfg is not UNSET:
            field_dict["isSupportClearGroupCfg"] = is_support_clear_group_cfg
        if is_support_multi_card_cfg is not UNSET:
            field_dict["isSupportMultiCardCfg"] = is_support_multi_card_cfg
        if is_support_multi_door_inter_lock_cfg is not UNSET:
            field_dict["isSupportMultiDoorInterLockCfg"] = is_support_multi_door_inter_lock_cfg
        if is_support_anti_sneak_cfg is not UNSET:
            field_dict["isSupportAntiSneakCfg"] = is_support_anti_sneak_cfg
        if is_support_card_reader_anti_sneak_cfg is not UNSET:
            field_dict["isSupportCardReaderAntiSneakCfg"] = is_support_card_reader_anti_sneak_cfg
        if is_support_clear_anti_sneak_cfg is not UNSET:
            field_dict["isSupportClearAntiSneakCfg"] = is_support_clear_anti_sneak_cfg
        if is_support_clear_anti_sneak is not UNSET:
            field_dict["isSupportClearAntiSneak"] = is_support_clear_anti_sneak
        if is_support_sms_relative_param is not UNSET:
            field_dict["isSupportSmsRelativeParam"] = is_support_sms_relative_param
        if is_support_phone_door_right_cfg is not UNSET:
            field_dict["isSupportPhoneDoorRightCfg"] = is_support_phone_door_right_cfg
        if is_support_osdp_status is not UNSET:
            field_dict["isSupportOSDPStatus"] = is_support_osdp_status
        if is_support_osdp_modify is not UNSET:
            field_dict["isSupportOSDPModify"] = is_support_osdp_modify
        if is_support_log_mode_cfg is not UNSET:
            field_dict["isSupportLogModeCfg"] = is_support_log_mode_cfg
        if factory_reset is not UNSET:
            field_dict["FactoryReset"] = factory_reset
        if is_support_nfc_cfg is not UNSET:
            field_dict["isSupportNFCCfg"] = is_support_nfc_cfg
        if is_support_rf_card_cfg is not UNSET:
            field_dict["isSupportRFCardCfg"] = is_support_rf_card_cfg
        if is_support_capture_face is not UNSET:
            field_dict["isSupportCaptureFace"] = is_support_capture_face
        if is_support_capture_infrared_face is not UNSET:
            field_dict["isSupportCaptureInfraredFace"] = is_support_capture_infrared_face
        if is_support_face_recognize_mode is not UNSET:
            field_dict["isSupportFaceRecognizeMode"] = is_support_face_recognize_mode
        if is_support_remote_control_pw_chcek is not UNSET:
            field_dict["isSupportRemoteControlPWChcek"] = is_support_remote_control_pw_chcek
        if is_support_remote_control_pw_cfg is not UNSET:
            field_dict["isSupportRemoteControlPWCfg"] = is_support_remote_control_pw_cfg
        if is_support_attendance_status_mode_cfg is not UNSET:
            field_dict["isSupportAttendanceStatusModeCfg"] = is_support_attendance_status_mode_cfg
        if is_support_attendance_status_rule_cfg is not UNSET:
            field_dict["isSupportAttendanceStatusRuleCfg"] = is_support_attendance_status_rule_cfg
        if is_support_capture_card_info is not UNSET:
            field_dict["isSupportCaptureCardInfo"] = is_support_capture_card_info
        if is_support_capture_id_info is not UNSET:
            field_dict["isSupportCaptureIDInfo"] = is_support_capture_id_info
        if is_support_capture_rule is not UNSET:
            field_dict["isSupportCaptureRule"] = is_support_capture_rule
        if is_support_capture_preset_param is not UNSET:
            field_dict["isSupportCapturePresetParam"] = is_support_capture_preset_param
        if is_support_offline_capture is not UNSET:
            field_dict["isSupportOfflineCapture"] = is_support_offline_capture
        if is_support_card_operations is not UNSET:
            field_dict["isSupportCardOperations"] = is_support_card_operations
        if is_support_right_controller_audio is not UNSET:
            field_dict["isSupportRightControllerAudio"] = is_support_right_controller_audio
        if is_support_channel_controller_cfg is not UNSET:
            field_dict["isSupportChannelControllerCfg"] = is_support_channel_controller_cfg
        if is_support_gate_dial_and_info is not UNSET:
            field_dict["isSupportGateDialAndInfo"] = is_support_gate_dial_and_info
        if is_support_gate_status is not UNSET:
            field_dict["isSupportGateStatus"] = is_support_gate_status
        if is_support_gate_ir_status is not UNSET:
            field_dict["isSupportGateIRStatus"] = is_support_gate_ir_status
        if is_support_gate_related_parts_status is not UNSET:
            field_dict["isSupportGateRelatedPartsStatus"] = is_support_gate_related_parts_status
        if is_support_channel_controller_alarm_linkage is not UNSET:
            field_dict["isSupportChannelControllerAlarmLinkage"] = is_support_channel_controller_alarm_linkage
        if is_support_channel_controller_alarm_out is not UNSET:
            field_dict["isSupportChannelControllerAlarmOut"] = is_support_channel_controller_alarm_out
        if is_support_channel_controller_alarm_out_control is not UNSET:
            field_dict["isSupportChannelControllerAlarmOutControl"] = is_support_channel_controller_alarm_out_control
        if is_support_channel_controller_type_cfg is not UNSET:
            field_dict["isSupportChannelControllerTypeCfg"] = is_support_channel_controller_type_cfg
        if is_support_tts_text is not UNSET:
            field_dict["isSupportTTSText"] = is_support_tts_text
        if is_support_id_black_list_cfg is not UNSET:
            field_dict["isSupportIDBlackListCfg"] = is_support_id_black_list_cfg
        if is_support_user_data_import is not UNSET:
            field_dict["isSupportUserDataImport"] = is_support_user_data_import
        if is_support_user_data_export is not UNSET:
            field_dict["isSupportUserDataExport"] = is_support_user_data_export
        if is_support_maintenance_data_export is not UNSET:
            field_dict["isSupportMaintenanceDataExport"] = is_support_maintenance_data_export
        if is_support_lock_type_cfg is not UNSET:
            field_dict["isSupportLockTypeCfg"] = is_support_lock_type_cfg
        if version is not UNSET:
            field_dict["@version"] = version
        if xmlns is not UNSET:
            field_dict["@xmlns"] = xmlns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_cap_access_control_access_control_employee_no_info import (
            RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_factory_reset import (
            RootTypeForXMLCapAccessControlAccessControlFactoryReset,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAcsCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_event import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEvent,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_event_total_num import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEventTotalNum,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_acs_work_status import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAcsWorkStatus,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_anti_sneak_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAntiSneakCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_holiday_group import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayGroup,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_holiday_plan import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayPlan,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_rule import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceRule,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_status_mode_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusModeCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_attendance_status_rule_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusRuleCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_auth_code_info import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportAuthCodeInfo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_card_info import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureCardInfo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_face import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFace,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_finger_print import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFingerPrint,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_id_info import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureIDInfo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_infrared_face import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureInfraredFace,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_preset_param import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCapturePresetParam,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_capture_rule import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureRule,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_operations import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardOperations,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_reader_anti_sneak_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderAntiSneakCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_reader_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_reader_plan import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderPlan,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_right_holiday_plan_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightHolidayPlanCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_card_right_week_plan_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightWeekPlanCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_alarm_linkage import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmLinkage,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_alarm_out import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOut,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_alarm_out_control import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOutControl,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_channel_controller_type_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerTypeCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_anti_sneak import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneak,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_anti_sneak_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneakCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_card_record import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearCardRecord,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_event_card_linkage_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearEventCardLinkageCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_group_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearGroupCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_plans_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearPlansCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_clear_submarine_back import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportClearSubmarineBack,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_department_param import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDepartmentParam,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_deploy_info_item import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDeployInfoItem,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_holiday_group_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayGroupCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_holiday_plan_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayPlanCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_plan import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlan,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_plan_template import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlanTemplate,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_door_status_week_plan_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusWeekPlanCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_event_card_linkage_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardLinkageCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_event_card_no_list import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardNoList,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_event_optimization_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportEventOptimizationCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_face_recognize_mode import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportFaceRecognizeMode,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_finger_print_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_finger_print_delete import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintDelete,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_dial_and_info import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportGateDialAndInfo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_ir_status import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportGateIRStatus,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_related_parts_status import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportGateRelatedPartsStatus,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_gate_status import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportGateStatus,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_group_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportGroupCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_identity_terminal import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportIdentityTerminal,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_ladder_control_relay import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportLadderControlRelay,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_log_mode_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportLogModeCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_m1_card_encrypt_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportM1CardEncryptCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_module_status import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportModuleStatus,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_multi_card_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportMultiCardCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_multi_door_inter_lock_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportMultiDoorInterLockCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_offline_capture import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportOfflineCapture,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_ordinary_class import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportOrdinaryClass,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_osdp_modify import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPModify,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_osdp_status import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPStatus,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_phone_door_right_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportPhoneDoorRightCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_reader_across_host import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportReaderAcrossHost,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_buzzer import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlBuzzer,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_door import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlDoor,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_pw_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_remote_control_pw_chcek import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWChcek,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_right_controller_audio import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportRightControllerAudio,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_schedule_plan import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportSchedulePlan,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_server_device import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportServerDevice,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_sms_relative_param import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportSmsRelativeParam,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_snap_config import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportSNAPConfig,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_start_reader_info import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportStartReaderInfo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBack,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back_host_info import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackHostInfo,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back_mode import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackMode,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_submarine_back_reader import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackReader,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_usb_manage import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportUSBManage,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_user_right_holiday_group_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightHolidayGroupCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_user_right_plan_template import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightPlanTemplate,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_holiday_group_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayGroupCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_holiday_plan_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayPlanCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_plan_template import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyPlanTemplate,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_verify_week_plan_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyWeekPlanCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_wiegand_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_wiegand_rule_cfg import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandRuleCfg,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_is_support_working_class import (
            RootTypeForXMLCapAccessControlAccessControlIsSupportWorkingClass,
        )
        from ..models.root_type_for_xml_cap_access_control_access_control_local_controller import (
            RootTypeForXMLCapAccessControlAccessControlLocalController,
        )

        d = src_dict.copy()
        _is_support_wiegand_cfg = d.pop("isSupportWiegandCfg", UNSET)
        is_support_wiegand_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandCfg]
        if isinstance(_is_support_wiegand_cfg, Unset):
            is_support_wiegand_cfg = UNSET
        else:
            is_support_wiegand_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandCfg.from_dict(
                _is_support_wiegand_cfg
            )

        _is_support_module_status = d.pop("isSupportModuleStatus", UNSET)
        is_support_module_status: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportModuleStatus]
        if isinstance(_is_support_module_status, Unset):
            is_support_module_status = UNSET
        else:
            is_support_module_status = RootTypeForXMLCapAccessControlAccessControlIsSupportModuleStatus.from_dict(
                _is_support_module_status
            )

        _is_support_snap_config = d.pop("isSupportSNAPConfig", UNSET)
        is_support_snap_config: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSNAPConfig]
        if isinstance(_is_support_snap_config, Unset):
            is_support_snap_config = UNSET
        else:
            is_support_snap_config = RootTypeForXMLCapAccessControlAccessControlIsSupportSNAPConfig.from_dict(
                _is_support_snap_config
            )

        _local_controller = d.pop("LocalController", UNSET)
        local_controller: Union[Unset, RootTypeForXMLCapAccessControlAccessControlLocalController]
        if isinstance(_local_controller, Unset):
            local_controller = UNSET
        else:
            local_controller = RootTypeForXMLCapAccessControlAccessControlLocalController.from_dict(_local_controller)

        _is_support_usb_manage = d.pop("isSupportUSBManage", UNSET)
        is_support_usb_manage: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportUSBManage]
        if isinstance(_is_support_usb_manage, Unset):
            is_support_usb_manage = UNSET
        else:
            is_support_usb_manage = RootTypeForXMLCapAccessControlAccessControlIsSupportUSBManage.from_dict(
                _is_support_usb_manage
            )

        _is_support_identity_terminal = d.pop("isSupportIdentityTerminal", UNSET)
        is_support_identity_terminal: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportIdentityTerminal]
        if isinstance(_is_support_identity_terminal, Unset):
            is_support_identity_terminal = UNSET
        else:
            is_support_identity_terminal = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportIdentityTerminal.from_dict(
                    _is_support_identity_terminal
                )
            )

        _is_support_department_param = d.pop("isSupportDepartmentParam", UNSET)
        is_support_department_param: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDepartmentParam]
        if isinstance(_is_support_department_param, Unset):
            is_support_department_param = UNSET
        else:
            is_support_department_param = RootTypeForXMLCapAccessControlAccessControlIsSupportDepartmentParam.from_dict(
                _is_support_department_param
            )

        _is_support_schedule_plan = d.pop("isSupportSchedulePlan", UNSET)
        is_support_schedule_plan: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSchedulePlan]
        if isinstance(_is_support_schedule_plan, Unset):
            is_support_schedule_plan = UNSET
        else:
            is_support_schedule_plan = RootTypeForXMLCapAccessControlAccessControlIsSupportSchedulePlan.from_dict(
                _is_support_schedule_plan
            )

        _is_support_attendance_rule = d.pop("isSupportAttendanceRule", UNSET)
        is_support_attendance_rule: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceRule]
        if isinstance(_is_support_attendance_rule, Unset):
            is_support_attendance_rule = UNSET
        else:
            is_support_attendance_rule = RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceRule.from_dict(
                _is_support_attendance_rule
            )

        _is_support_ordinary_class = d.pop("isSupportOrdinaryClass", UNSET)
        is_support_ordinary_class: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOrdinaryClass]
        if isinstance(_is_support_ordinary_class, Unset):
            is_support_ordinary_class = UNSET
        else:
            is_support_ordinary_class = RootTypeForXMLCapAccessControlAccessControlIsSupportOrdinaryClass.from_dict(
                _is_support_ordinary_class
            )

        _is_support_working_class = d.pop("isSupportWorkingClass", UNSET)
        is_support_working_class: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportWorkingClass]
        if isinstance(_is_support_working_class, Unset):
            is_support_working_class = UNSET
        else:
            is_support_working_class = RootTypeForXMLCapAccessControlAccessControlIsSupportWorkingClass.from_dict(
                _is_support_working_class
            )

        _is_support_attendance_holiday_group = d.pop("isSupportAttendanceHolidayGroup", UNSET)
        is_support_attendance_holiday_group: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayGroup
        ]
        if isinstance(_is_support_attendance_holiday_group, Unset):
            is_support_attendance_holiday_group = UNSET
        else:
            is_support_attendance_holiday_group = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayGroup.from_dict(
                    _is_support_attendance_holiday_group
                )
            )

        _is_support_attendance_holiday_plan = d.pop("isSupportAttendanceHolidayPlan", UNSET)
        is_support_attendance_holiday_plan: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayPlan
        ]
        if isinstance(_is_support_attendance_holiday_plan, Unset):
            is_support_attendance_holiday_plan = UNSET
        else:
            is_support_attendance_holiday_plan = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceHolidayPlan.from_dict(
                    _is_support_attendance_holiday_plan
                )
            )

        _is_support_ladder_control_relay = d.pop("isSupportLadderControlRelay", UNSET)
        is_support_ladder_control_relay: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportLadderControlRelay
        ]
        if isinstance(_is_support_ladder_control_relay, Unset):
            is_support_ladder_control_relay = UNSET
        else:
            is_support_ladder_control_relay = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportLadderControlRelay.from_dict(
                    _is_support_ladder_control_relay
                )
            )

        _is_support_wiegand_rule_cfg = d.pop("isSupportWiegandRuleCfg", UNSET)
        is_support_wiegand_rule_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandRuleCfg]
        if isinstance(_is_support_wiegand_rule_cfg, Unset):
            is_support_wiegand_rule_cfg = UNSET
        else:
            is_support_wiegand_rule_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportWiegandRuleCfg.from_dict(
                _is_support_wiegand_rule_cfg
            )

        _is_support_m1_card_encrypt_cfg = d.pop("isSupportM1CardEncryptCfg", UNSET)
        is_support_m1_card_encrypt_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportM1CardEncryptCfg
        ]
        if isinstance(_is_support_m1_card_encrypt_cfg, Unset):
            is_support_m1_card_encrypt_cfg = UNSET
        else:
            is_support_m1_card_encrypt_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportM1CardEncryptCfg.from_dict(
                    _is_support_m1_card_encrypt_cfg
                )
            )

        is_support_deploy_info = []
        _is_support_deploy_info = d.pop("isSupportDeployInfo", UNSET)
        for is_support_deploy_info_item_data in _is_support_deploy_info or []:
            is_support_deploy_info_item = RootTypeForXMLCapAccessControlAccessControlIsSupportDeployInfoItem.from_dict(
                is_support_deploy_info_item_data
            )

            is_support_deploy_info.append(is_support_deploy_info_item)

        _is_support_submarine_back = d.pop("isSupportSubmarineBack", UNSET)
        is_support_submarine_back: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBack]
        if isinstance(_is_support_submarine_back, Unset):
            is_support_submarine_back = UNSET
        else:
            is_support_submarine_back = RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBack.from_dict(
                _is_support_submarine_back
            )

        _is_support_submarine_back_host_info = d.pop("isSupportSubmarineBackHostInfo", UNSET)
        is_support_submarine_back_host_info: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackHostInfo
        ]
        if isinstance(_is_support_submarine_back_host_info, Unset):
            is_support_submarine_back_host_info = UNSET
        else:
            is_support_submarine_back_host_info = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackHostInfo.from_dict(
                    _is_support_submarine_back_host_info
                )
            )

        _is_support_start_reader_info = d.pop("isSupportStartReaderInfo", UNSET)
        is_support_start_reader_info: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportStartReaderInfo]
        if isinstance(_is_support_start_reader_info, Unset):
            is_support_start_reader_info = UNSET
        else:
            is_support_start_reader_info = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportStartReaderInfo.from_dict(
                    _is_support_start_reader_info
                )
            )

        _is_support_submarine_back_reader = d.pop("isSupportSubmarineBackReader", UNSET)
        is_support_submarine_back_reader: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackReader
        ]
        if isinstance(_is_support_submarine_back_reader, Unset):
            is_support_submarine_back_reader = UNSET
        else:
            is_support_submarine_back_reader = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackReader.from_dict(
                    _is_support_submarine_back_reader
                )
            )

        _is_support_server_device = d.pop("isSupportServerDevice", UNSET)
        is_support_server_device: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportServerDevice]
        if isinstance(_is_support_server_device, Unset):
            is_support_server_device = UNSET
        else:
            is_support_server_device = RootTypeForXMLCapAccessControlAccessControlIsSupportServerDevice.from_dict(
                _is_support_server_device
            )

        _is_support_reader_across_host = d.pop("isSupportReaderAcrossHost", UNSET)
        is_support_reader_across_host: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportReaderAcrossHost
        ]
        if isinstance(_is_support_reader_across_host, Unset):
            is_support_reader_across_host = UNSET
        else:
            is_support_reader_across_host = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportReaderAcrossHost.from_dict(
                    _is_support_reader_across_host
                )
            )

        _is_support_clear_card_record = d.pop("isSupportClearCardRecord", UNSET)
        is_support_clear_card_record: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearCardRecord]
        if isinstance(_is_support_clear_card_record, Unset):
            is_support_clear_card_record = UNSET
        else:
            is_support_clear_card_record = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportClearCardRecord.from_dict(
                    _is_support_clear_card_record
                )
            )

        _is_support_submarine_back_mode = d.pop("isSupportSubmarineBackMode", UNSET)
        is_support_submarine_back_mode: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackMode
        ]
        if isinstance(_is_support_submarine_back_mode, Unset):
            is_support_submarine_back_mode = UNSET
        else:
            is_support_submarine_back_mode = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportSubmarineBackMode.from_dict(
                    _is_support_submarine_back_mode
                )
            )

        _is_support_clear_submarine_back = d.pop("isSupportClearSubmarineBack", UNSET)
        is_support_clear_submarine_back: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearSubmarineBack
        ]
        if isinstance(_is_support_clear_submarine_back, Unset):
            is_support_clear_submarine_back = UNSET
        else:
            is_support_clear_submarine_back = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportClearSubmarineBack.from_dict(
                    _is_support_clear_submarine_back
                )
            )

        _is_support_remote_control_door = d.pop("isSupportRemoteControlDoor", UNSET)
        is_support_remote_control_door: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlDoor
        ]
        if isinstance(_is_support_remote_control_door, Unset):
            is_support_remote_control_door = UNSET
        else:
            is_support_remote_control_door = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlDoor.from_dict(
                    _is_support_remote_control_door
                )
            )

        is_support_user_info = d.pop("isSupportUserInfo", UNSET)

        _employee_no_info = d.pop("EmployeeNoInfo", UNSET)
        employee_no_info: Union[Unset, RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo]
        if isinstance(_employee_no_info, Unset):
            employee_no_info = UNSET
        else:
            employee_no_info = RootTypeForXMLCapAccessControlAccessControlEmployeeNoInfo.from_dict(_employee_no_info)

        is_support_card_info = d.pop("isSupportCardInfo", UNSET)

        is_support_user_info_detail_delete = d.pop("isSupportUserInfoDetailDelete", UNSET)

        _is_support_auth_code_info = d.pop("isSupportAuthCodeInfo", UNSET)
        is_support_auth_code_info: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAuthCodeInfo]
        if isinstance(_is_support_auth_code_info, Unset):
            is_support_auth_code_info = UNSET
        else:
            is_support_auth_code_info = RootTypeForXMLCapAccessControlAccessControlIsSupportAuthCodeInfo.from_dict(
                _is_support_auth_code_info
            )

        _is_support_finger_print_cfg = d.pop("isSupportFingerPrintCfg", UNSET)
        is_support_finger_print_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintCfg]
        if isinstance(_is_support_finger_print_cfg, Unset):
            is_support_finger_print_cfg = UNSET
        else:
            is_support_finger_print_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintCfg.from_dict(
                _is_support_finger_print_cfg
            )

        _is_support_finger_print_delete = d.pop("isSupportFingerPrintDelete", UNSET)
        is_support_finger_print_delete: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintDelete
        ]
        if isinstance(_is_support_finger_print_delete, Unset):
            is_support_finger_print_delete = UNSET
        else:
            is_support_finger_print_delete = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportFingerPrintDelete.from_dict(
                    _is_support_finger_print_delete
                )
            )

        _is_support_capture_finger_print = d.pop("isSupportCaptureFingerPrint", UNSET)
        is_support_capture_finger_print: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFingerPrint
        ]
        if isinstance(_is_support_capture_finger_print, Unset):
            is_support_capture_finger_print = UNSET
        else:
            is_support_capture_finger_print = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFingerPrint.from_dict(
                    _is_support_capture_finger_print
                )
            )

        _is_support_door_status_week_plan_cfg = d.pop("isSupportDoorStatusWeekPlanCfg", UNSET)
        is_support_door_status_week_plan_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusWeekPlanCfg
        ]
        if isinstance(_is_support_door_status_week_plan_cfg, Unset):
            is_support_door_status_week_plan_cfg = UNSET
        else:
            is_support_door_status_week_plan_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusWeekPlanCfg.from_dict(
                    _is_support_door_status_week_plan_cfg
                )
            )

        _is_support_verify_week_plan_cfg = d.pop("isSupportVerifyWeekPlanCfg", UNSET)
        is_support_verify_week_plan_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyWeekPlanCfg
        ]
        if isinstance(_is_support_verify_week_plan_cfg, Unset):
            is_support_verify_week_plan_cfg = UNSET
        else:
            is_support_verify_week_plan_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyWeekPlanCfg.from_dict(
                    _is_support_verify_week_plan_cfg
                )
            )

        _is_support_card_right_week_plan_cfg = d.pop("isSupportCardRightWeekPlanCfg", UNSET)
        is_support_card_right_week_plan_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightWeekPlanCfg
        ]
        if isinstance(_is_support_card_right_week_plan_cfg, Unset):
            is_support_card_right_week_plan_cfg = UNSET
        else:
            is_support_card_right_week_plan_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightWeekPlanCfg.from_dict(
                    _is_support_card_right_week_plan_cfg
                )
            )

        _is_support_door_status_holiday_plan_cfg = d.pop("isSupportDoorStatusHolidayPlanCfg", UNSET)
        is_support_door_status_holiday_plan_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayPlanCfg
        ]
        if isinstance(_is_support_door_status_holiday_plan_cfg, Unset):
            is_support_door_status_holiday_plan_cfg = UNSET
        else:
            is_support_door_status_holiday_plan_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayPlanCfg.from_dict(
                    _is_support_door_status_holiday_plan_cfg
                )
            )

        _is_support_verify_holiday_plan_cfg = d.pop("isSupportVerifyHolidayPlanCfg", UNSET)
        is_support_verify_holiday_plan_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayPlanCfg
        ]
        if isinstance(_is_support_verify_holiday_plan_cfg, Unset):
            is_support_verify_holiday_plan_cfg = UNSET
        else:
            is_support_verify_holiday_plan_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayPlanCfg.from_dict(
                    _is_support_verify_holiday_plan_cfg
                )
            )

        _is_support_card_right_holiday_plan_cfg = d.pop("isSupportCardRightHolidayPlanCfg", UNSET)
        is_support_card_right_holiday_plan_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightHolidayPlanCfg
        ]
        if isinstance(_is_support_card_right_holiday_plan_cfg, Unset):
            is_support_card_right_holiday_plan_cfg = UNSET
        else:
            is_support_card_right_holiday_plan_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportCardRightHolidayPlanCfg.from_dict(
                    _is_support_card_right_holiday_plan_cfg
                )
            )

        _is_support_door_status_holiday_group_cfg = d.pop("isSupportDoorStatusHolidayGroupCfg", UNSET)
        is_support_door_status_holiday_group_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayGroupCfg
        ]
        if isinstance(_is_support_door_status_holiday_group_cfg, Unset):
            is_support_door_status_holiday_group_cfg = UNSET
        else:
            is_support_door_status_holiday_group_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusHolidayGroupCfg.from_dict(
                    _is_support_door_status_holiday_group_cfg
                )
            )

        _is_support_verify_holiday_group_cfg = d.pop("isSupportVerifyHolidayGroupCfg", UNSET)
        is_support_verify_holiday_group_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayGroupCfg
        ]
        if isinstance(_is_support_verify_holiday_group_cfg, Unset):
            is_support_verify_holiday_group_cfg = UNSET
        else:
            is_support_verify_holiday_group_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyHolidayGroupCfg.from_dict(
                    _is_support_verify_holiday_group_cfg
                )
            )

        _is_support_user_right_holiday_group_cfg = d.pop("isSupportUserRightHolidayGroupCfg", UNSET)
        is_support_user_right_holiday_group_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightHolidayGroupCfg
        ]
        if isinstance(_is_support_user_right_holiday_group_cfg, Unset):
            is_support_user_right_holiday_group_cfg = UNSET
        else:
            is_support_user_right_holiday_group_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightHolidayGroupCfg.from_dict(
                    _is_support_user_right_holiday_group_cfg
                )
            )

        _is_support_door_status_plan_template = d.pop("isSupportDoorStatusPlanTemplate", UNSET)
        is_support_door_status_plan_template: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlanTemplate
        ]
        if isinstance(_is_support_door_status_plan_template, Unset):
            is_support_door_status_plan_template = UNSET
        else:
            is_support_door_status_plan_template = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlanTemplate.from_dict(
                    _is_support_door_status_plan_template
                )
            )

        _is_support_verify_plan_template = d.pop("isSupportVerifyPlanTemplate", UNSET)
        is_support_verify_plan_template: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyPlanTemplate
        ]
        if isinstance(_is_support_verify_plan_template, Unset):
            is_support_verify_plan_template = UNSET
        else:
            is_support_verify_plan_template = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportVerifyPlanTemplate.from_dict(
                    _is_support_verify_plan_template
                )
            )

        _is_support_user_right_plan_template = d.pop("isSupportUserRightPlanTemplate", UNSET)
        is_support_user_right_plan_template: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightPlanTemplate
        ]
        if isinstance(_is_support_user_right_plan_template, Unset):
            is_support_user_right_plan_template = UNSET
        else:
            is_support_user_right_plan_template = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportUserRightPlanTemplate.from_dict(
                    _is_support_user_right_plan_template
                )
            )

        _is_support_door_status_plan = d.pop("isSupportDoorStatusPlan", UNSET)
        is_support_door_status_plan: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlan]
        if isinstance(_is_support_door_status_plan, Unset):
            is_support_door_status_plan = UNSET
        else:
            is_support_door_status_plan = RootTypeForXMLCapAccessControlAccessControlIsSupportDoorStatusPlan.from_dict(
                _is_support_door_status_plan
            )

        _is_support_card_reader_plan = d.pop("isSupportCardReaderPlan", UNSET)
        is_support_card_reader_plan: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderPlan]
        if isinstance(_is_support_card_reader_plan, Unset):
            is_support_card_reader_plan = UNSET
        else:
            is_support_card_reader_plan = RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderPlan.from_dict(
                _is_support_card_reader_plan
            )

        _is_support_clear_plans_cfg = d.pop("isSupportClearPlansCfg", UNSET)
        is_support_clear_plans_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearPlansCfg]
        if isinstance(_is_support_clear_plans_cfg, Unset):
            is_support_clear_plans_cfg = UNSET
        else:
            is_support_clear_plans_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportClearPlansCfg.from_dict(
                _is_support_clear_plans_cfg
            )

        _is_support_remote_control_buzzer = d.pop("isSupportRemoteControlBuzzer", UNSET)
        is_support_remote_control_buzzer: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlBuzzer
        ]
        if isinstance(_is_support_remote_control_buzzer, Unset):
            is_support_remote_control_buzzer = UNSET
        else:
            is_support_remote_control_buzzer = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlBuzzer.from_dict(
                    _is_support_remote_control_buzzer
                )
            )

        _is_support_event_card_no_list = d.pop("isSupportEventCardNoList", UNSET)
        is_support_event_card_no_list: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardNoList]
        if isinstance(_is_support_event_card_no_list, Unset):
            is_support_event_card_no_list = UNSET
        else:
            is_support_event_card_no_list = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardNoList.from_dict(
                    _is_support_event_card_no_list
                )
            )

        _is_support_event_card_linkage_cfg = d.pop("isSupportEventCardLinkageCfg", UNSET)
        is_support_event_card_linkage_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardLinkageCfg
        ]
        if isinstance(_is_support_event_card_linkage_cfg, Unset):
            is_support_event_card_linkage_cfg = UNSET
        else:
            is_support_event_card_linkage_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportEventCardLinkageCfg.from_dict(
                    _is_support_event_card_linkage_cfg
                )
            )

        _is_support_clear_event_card_linkage_cfg = d.pop("isSupportClearEventCardLinkageCfg", UNSET)
        is_support_clear_event_card_linkage_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearEventCardLinkageCfg
        ]
        if isinstance(_is_support_clear_event_card_linkage_cfg, Unset):
            is_support_clear_event_card_linkage_cfg = UNSET
        else:
            is_support_clear_event_card_linkage_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportClearEventCardLinkageCfg.from_dict(
                    _is_support_clear_event_card_linkage_cfg
                )
            )

        _is_support_acs_event = d.pop("isSupportAcsEvent", UNSET)
        is_support_acs_event: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEvent]
        if isinstance(_is_support_acs_event, Unset):
            is_support_acs_event = UNSET
        else:
            is_support_acs_event = RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEvent.from_dict(
                _is_support_acs_event
            )

        _is_support_acs_event_total_num = d.pop("isSupportAcsEventTotalNum", UNSET)
        is_support_acs_event_total_num: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEventTotalNum
        ]
        if isinstance(_is_support_acs_event_total_num, Unset):
            is_support_acs_event_total_num = UNSET
        else:
            is_support_acs_event_total_num = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportAcsEventTotalNum.from_dict(
                    _is_support_acs_event_total_num
                )
            )

        _is_support_event_optimization_cfg = d.pop("isSupportEventOptimizationCfg", UNSET)
        is_support_event_optimization_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportEventOptimizationCfg
        ]
        if isinstance(_is_support_event_optimization_cfg, Unset):
            is_support_event_optimization_cfg = UNSET
        else:
            is_support_event_optimization_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportEventOptimizationCfg.from_dict(
                    _is_support_event_optimization_cfg
                )
            )

        _is_support_acs_work_status = d.pop("isSupportAcsWorkStatus", UNSET)
        is_support_acs_work_status: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAcsWorkStatus]
        if isinstance(_is_support_acs_work_status, Unset):
            is_support_acs_work_status = UNSET
        else:
            is_support_acs_work_status = RootTypeForXMLCapAccessControlAccessControlIsSupportAcsWorkStatus.from_dict(
                _is_support_acs_work_status
            )

        _is_support_door_cfg = d.pop("isSupportDoorCfg", UNSET)
        is_support_door_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportDoorCfg]
        if isinstance(_is_support_door_cfg, Unset):
            is_support_door_cfg = UNSET
        else:
            is_support_door_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportDoorCfg.from_dict(
                _is_support_door_cfg
            )

        _is_support_card_reader_cfg = d.pop("isSupportCardReaderCfg", UNSET)
        is_support_card_reader_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderCfg]
        if isinstance(_is_support_card_reader_cfg, Unset):
            is_support_card_reader_cfg = UNSET
        else:
            is_support_card_reader_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderCfg.from_dict(
                _is_support_card_reader_cfg
            )

        _is_support_acs_cfg = d.pop("isSupportAcsCfg", UNSET)
        is_support_acs_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAcsCfg]
        if isinstance(_is_support_acs_cfg, Unset):
            is_support_acs_cfg = UNSET
        else:
            is_support_acs_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportAcsCfg.from_dict(
                _is_support_acs_cfg
            )

        _is_support_group_cfg = d.pop("isSupportGroupCfg", UNSET)
        is_support_group_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGroupCfg]
        if isinstance(_is_support_group_cfg, Unset):
            is_support_group_cfg = UNSET
        else:
            is_support_group_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportGroupCfg.from_dict(
                _is_support_group_cfg
            )

        _is_support_clear_group_cfg = d.pop("isSupportClearGroupCfg", UNSET)
        is_support_clear_group_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearGroupCfg]
        if isinstance(_is_support_clear_group_cfg, Unset):
            is_support_clear_group_cfg = UNSET
        else:
            is_support_clear_group_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportClearGroupCfg.from_dict(
                _is_support_clear_group_cfg
            )

        _is_support_multi_card_cfg = d.pop("isSupportMultiCardCfg", UNSET)
        is_support_multi_card_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportMultiCardCfg]
        if isinstance(_is_support_multi_card_cfg, Unset):
            is_support_multi_card_cfg = UNSET
        else:
            is_support_multi_card_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportMultiCardCfg.from_dict(
                _is_support_multi_card_cfg
            )

        _is_support_multi_door_inter_lock_cfg = d.pop("isSupportMultiDoorInterLockCfg", UNSET)
        is_support_multi_door_inter_lock_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportMultiDoorInterLockCfg
        ]
        if isinstance(_is_support_multi_door_inter_lock_cfg, Unset):
            is_support_multi_door_inter_lock_cfg = UNSET
        else:
            is_support_multi_door_inter_lock_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportMultiDoorInterLockCfg.from_dict(
                    _is_support_multi_door_inter_lock_cfg
                )
            )

        _is_support_anti_sneak_cfg = d.pop("isSupportAntiSneakCfg", UNSET)
        is_support_anti_sneak_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAntiSneakCfg]
        if isinstance(_is_support_anti_sneak_cfg, Unset):
            is_support_anti_sneak_cfg = UNSET
        else:
            is_support_anti_sneak_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportAntiSneakCfg.from_dict(
                _is_support_anti_sneak_cfg
            )

        _is_support_card_reader_anti_sneak_cfg = d.pop("isSupportCardReaderAntiSneakCfg", UNSET)
        is_support_card_reader_anti_sneak_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderAntiSneakCfg
        ]
        if isinstance(_is_support_card_reader_anti_sneak_cfg, Unset):
            is_support_card_reader_anti_sneak_cfg = UNSET
        else:
            is_support_card_reader_anti_sneak_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportCardReaderAntiSneakCfg.from_dict(
                    _is_support_card_reader_anti_sneak_cfg
                )
            )

        _is_support_clear_anti_sneak_cfg = d.pop("isSupportClearAntiSneakCfg", UNSET)
        is_support_clear_anti_sneak_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneakCfg
        ]
        if isinstance(_is_support_clear_anti_sneak_cfg, Unset):
            is_support_clear_anti_sneak_cfg = UNSET
        else:
            is_support_clear_anti_sneak_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneakCfg.from_dict(
                    _is_support_clear_anti_sneak_cfg
                )
            )

        _is_support_clear_anti_sneak = d.pop("isSupportClearAntiSneak", UNSET)
        is_support_clear_anti_sneak: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneak]
        if isinstance(_is_support_clear_anti_sneak, Unset):
            is_support_clear_anti_sneak = UNSET
        else:
            is_support_clear_anti_sneak = RootTypeForXMLCapAccessControlAccessControlIsSupportClearAntiSneak.from_dict(
                _is_support_clear_anti_sneak
            )

        _is_support_sms_relative_param = d.pop("isSupportSmsRelativeParam", UNSET)
        is_support_sms_relative_param: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportSmsRelativeParam
        ]
        if isinstance(_is_support_sms_relative_param, Unset):
            is_support_sms_relative_param = UNSET
        else:
            is_support_sms_relative_param = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportSmsRelativeParam.from_dict(
                    _is_support_sms_relative_param
                )
            )

        _is_support_phone_door_right_cfg = d.pop("isSupportPhoneDoorRightCfg", UNSET)
        is_support_phone_door_right_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportPhoneDoorRightCfg
        ]
        if isinstance(_is_support_phone_door_right_cfg, Unset):
            is_support_phone_door_right_cfg = UNSET
        else:
            is_support_phone_door_right_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportPhoneDoorRightCfg.from_dict(
                    _is_support_phone_door_right_cfg
                )
            )

        _is_support_osdp_status = d.pop("isSupportOSDPStatus", UNSET)
        is_support_osdp_status: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPStatus]
        if isinstance(_is_support_osdp_status, Unset):
            is_support_osdp_status = UNSET
        else:
            is_support_osdp_status = RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPStatus.from_dict(
                _is_support_osdp_status
            )

        _is_support_osdp_modify = d.pop("isSupportOSDPModify", UNSET)
        is_support_osdp_modify: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPModify]
        if isinstance(_is_support_osdp_modify, Unset):
            is_support_osdp_modify = UNSET
        else:
            is_support_osdp_modify = RootTypeForXMLCapAccessControlAccessControlIsSupportOSDPModify.from_dict(
                _is_support_osdp_modify
            )

        _is_support_log_mode_cfg = d.pop("isSupportLogModeCfg", UNSET)
        is_support_log_mode_cfg: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportLogModeCfg]
        if isinstance(_is_support_log_mode_cfg, Unset):
            is_support_log_mode_cfg = UNSET
        else:
            is_support_log_mode_cfg = RootTypeForXMLCapAccessControlAccessControlIsSupportLogModeCfg.from_dict(
                _is_support_log_mode_cfg
            )

        _factory_reset = d.pop("FactoryReset", UNSET)
        factory_reset: Union[Unset, RootTypeForXMLCapAccessControlAccessControlFactoryReset]
        if isinstance(_factory_reset, Unset):
            factory_reset = UNSET
        else:
            factory_reset = RootTypeForXMLCapAccessControlAccessControlFactoryReset.from_dict(_factory_reset)

        is_support_nfc_cfg = d.pop("isSupportNFCCfg", UNSET)

        is_support_rf_card_cfg = d.pop("isSupportRFCardCfg", UNSET)

        _is_support_capture_face = d.pop("isSupportCaptureFace", UNSET)
        is_support_capture_face: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFace]
        if isinstance(_is_support_capture_face, Unset):
            is_support_capture_face = UNSET
        else:
            is_support_capture_face = RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureFace.from_dict(
                _is_support_capture_face
            )

        _is_support_capture_infrared_face = d.pop("isSupportCaptureInfraredFace", UNSET)
        is_support_capture_infrared_face: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureInfraredFace
        ]
        if isinstance(_is_support_capture_infrared_face, Unset):
            is_support_capture_infrared_face = UNSET
        else:
            is_support_capture_infrared_face = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureInfraredFace.from_dict(
                    _is_support_capture_infrared_face
                )
            )

        _is_support_face_recognize_mode = d.pop("isSupportFaceRecognizeMode", UNSET)
        is_support_face_recognize_mode: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportFaceRecognizeMode
        ]
        if isinstance(_is_support_face_recognize_mode, Unset):
            is_support_face_recognize_mode = UNSET
        else:
            is_support_face_recognize_mode = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportFaceRecognizeMode.from_dict(
                    _is_support_face_recognize_mode
                )
            )

        _is_support_remote_control_pw_chcek = d.pop("isSupportRemoteControlPWChcek", UNSET)
        is_support_remote_control_pw_chcek: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWChcek
        ]
        if isinstance(_is_support_remote_control_pw_chcek, Unset):
            is_support_remote_control_pw_chcek = UNSET
        else:
            is_support_remote_control_pw_chcek = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWChcek.from_dict(
                    _is_support_remote_control_pw_chcek
                )
            )

        _is_support_remote_control_pw_cfg = d.pop("isSupportRemoteControlPWCfg", UNSET)
        is_support_remote_control_pw_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWCfg
        ]
        if isinstance(_is_support_remote_control_pw_cfg, Unset):
            is_support_remote_control_pw_cfg = UNSET
        else:
            is_support_remote_control_pw_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportRemoteControlPWCfg.from_dict(
                    _is_support_remote_control_pw_cfg
                )
            )

        _is_support_attendance_status_mode_cfg = d.pop("isSupportAttendanceStatusModeCfg", UNSET)
        is_support_attendance_status_mode_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusModeCfg
        ]
        if isinstance(_is_support_attendance_status_mode_cfg, Unset):
            is_support_attendance_status_mode_cfg = UNSET
        else:
            is_support_attendance_status_mode_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusModeCfg.from_dict(
                    _is_support_attendance_status_mode_cfg
                )
            )

        _is_support_attendance_status_rule_cfg = d.pop("isSupportAttendanceStatusRuleCfg", UNSET)
        is_support_attendance_status_rule_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusRuleCfg
        ]
        if isinstance(_is_support_attendance_status_rule_cfg, Unset):
            is_support_attendance_status_rule_cfg = UNSET
        else:
            is_support_attendance_status_rule_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportAttendanceStatusRuleCfg.from_dict(
                    _is_support_attendance_status_rule_cfg
                )
            )

        _is_support_capture_card_info = d.pop("isSupportCaptureCardInfo", UNSET)
        is_support_capture_card_info: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureCardInfo]
        if isinstance(_is_support_capture_card_info, Unset):
            is_support_capture_card_info = UNSET
        else:
            is_support_capture_card_info = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureCardInfo.from_dict(
                    _is_support_capture_card_info
                )
            )

        _is_support_capture_id_info = d.pop("isSupportCaptureIDInfo", UNSET)
        is_support_capture_id_info: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureIDInfo]
        if isinstance(_is_support_capture_id_info, Unset):
            is_support_capture_id_info = UNSET
        else:
            is_support_capture_id_info = RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureIDInfo.from_dict(
                _is_support_capture_id_info
            )

        _is_support_capture_rule = d.pop("isSupportCaptureRule", UNSET)
        is_support_capture_rule: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureRule]
        if isinstance(_is_support_capture_rule, Unset):
            is_support_capture_rule = UNSET
        else:
            is_support_capture_rule = RootTypeForXMLCapAccessControlAccessControlIsSupportCaptureRule.from_dict(
                _is_support_capture_rule
            )

        _is_support_capture_preset_param = d.pop("isSupportCapturePresetParam", UNSET)
        is_support_capture_preset_param: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCapturePresetParam
        ]
        if isinstance(_is_support_capture_preset_param, Unset):
            is_support_capture_preset_param = UNSET
        else:
            is_support_capture_preset_param = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportCapturePresetParam.from_dict(
                    _is_support_capture_preset_param
                )
            )

        _is_support_offline_capture = d.pop("isSupportOfflineCapture", UNSET)
        is_support_offline_capture: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportOfflineCapture]
        if isinstance(_is_support_offline_capture, Unset):
            is_support_offline_capture = UNSET
        else:
            is_support_offline_capture = RootTypeForXMLCapAccessControlAccessControlIsSupportOfflineCapture.from_dict(
                _is_support_offline_capture
            )

        _is_support_card_operations = d.pop("isSupportCardOperations", UNSET)
        is_support_card_operations: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportCardOperations]
        if isinstance(_is_support_card_operations, Unset):
            is_support_card_operations = UNSET
        else:
            is_support_card_operations = RootTypeForXMLCapAccessControlAccessControlIsSupportCardOperations.from_dict(
                _is_support_card_operations
            )

        _is_support_right_controller_audio = d.pop("isSupportRightControllerAudio", UNSET)
        is_support_right_controller_audio: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportRightControllerAudio
        ]
        if isinstance(_is_support_right_controller_audio, Unset):
            is_support_right_controller_audio = UNSET
        else:
            is_support_right_controller_audio = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportRightControllerAudio.from_dict(
                    _is_support_right_controller_audio
                )
            )

        _is_support_channel_controller_cfg = d.pop("isSupportChannelControllerCfg", UNSET)
        is_support_channel_controller_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerCfg
        ]
        if isinstance(_is_support_channel_controller_cfg, Unset):
            is_support_channel_controller_cfg = UNSET
        else:
            is_support_channel_controller_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerCfg.from_dict(
                    _is_support_channel_controller_cfg
                )
            )

        _is_support_gate_dial_and_info = d.pop("isSupportGateDialAndInfo", UNSET)
        is_support_gate_dial_and_info: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGateDialAndInfo]
        if isinstance(_is_support_gate_dial_and_info, Unset):
            is_support_gate_dial_and_info = UNSET
        else:
            is_support_gate_dial_and_info = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportGateDialAndInfo.from_dict(
                    _is_support_gate_dial_and_info
                )
            )

        _is_support_gate_status = d.pop("isSupportGateStatus", UNSET)
        is_support_gate_status: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGateStatus]
        if isinstance(_is_support_gate_status, Unset):
            is_support_gate_status = UNSET
        else:
            is_support_gate_status = RootTypeForXMLCapAccessControlAccessControlIsSupportGateStatus.from_dict(
                _is_support_gate_status
            )

        _is_support_gate_ir_status = d.pop("isSupportGateIRStatus", UNSET)
        is_support_gate_ir_status: Union[Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGateIRStatus]
        if isinstance(_is_support_gate_ir_status, Unset):
            is_support_gate_ir_status = UNSET
        else:
            is_support_gate_ir_status = RootTypeForXMLCapAccessControlAccessControlIsSupportGateIRStatus.from_dict(
                _is_support_gate_ir_status
            )

        _is_support_gate_related_parts_status = d.pop("isSupportGateRelatedPartsStatus", UNSET)
        is_support_gate_related_parts_status: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportGateRelatedPartsStatus
        ]
        if isinstance(_is_support_gate_related_parts_status, Unset):
            is_support_gate_related_parts_status = UNSET
        else:
            is_support_gate_related_parts_status = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportGateRelatedPartsStatus.from_dict(
                    _is_support_gate_related_parts_status
                )
            )

        _is_support_channel_controller_alarm_linkage = d.pop("isSupportChannelControllerAlarmLinkage", UNSET)
        is_support_channel_controller_alarm_linkage: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmLinkage
        ]
        if isinstance(_is_support_channel_controller_alarm_linkage, Unset):
            is_support_channel_controller_alarm_linkage = UNSET
        else:
            is_support_channel_controller_alarm_linkage = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmLinkage.from_dict(
                    _is_support_channel_controller_alarm_linkage
                )
            )

        _is_support_channel_controller_alarm_out = d.pop("isSupportChannelControllerAlarmOut", UNSET)
        is_support_channel_controller_alarm_out: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOut
        ]
        if isinstance(_is_support_channel_controller_alarm_out, Unset):
            is_support_channel_controller_alarm_out = UNSET
        else:
            is_support_channel_controller_alarm_out = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOut.from_dict(
                    _is_support_channel_controller_alarm_out
                )
            )

        _is_support_channel_controller_alarm_out_control = d.pop("isSupportChannelControllerAlarmOutControl", UNSET)
        is_support_channel_controller_alarm_out_control: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOutControl
        ]
        if isinstance(_is_support_channel_controller_alarm_out_control, Unset):
            is_support_channel_controller_alarm_out_control = UNSET
        else:
            is_support_channel_controller_alarm_out_control = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerAlarmOutControl.from_dict(
                    _is_support_channel_controller_alarm_out_control
                )
            )

        _is_support_channel_controller_type_cfg = d.pop("isSupportChannelControllerTypeCfg", UNSET)
        is_support_channel_controller_type_cfg: Union[
            Unset, RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerTypeCfg
        ]
        if isinstance(_is_support_channel_controller_type_cfg, Unset):
            is_support_channel_controller_type_cfg = UNSET
        else:
            is_support_channel_controller_type_cfg = (
                RootTypeForXMLCapAccessControlAccessControlIsSupportChannelControllerTypeCfg.from_dict(
                    _is_support_channel_controller_type_cfg
                )
            )

        is_support_tts_text = d.pop("isSupportTTSText", UNSET)

        is_support_id_black_list_cfg = d.pop("isSupportIDBlackListCfg", UNSET)

        is_support_user_data_import = d.pop("isSupportUserDataImport", UNSET)

        is_support_user_data_export = d.pop("isSupportUserDataExport", UNSET)

        is_support_maintenance_data_export = d.pop("isSupportMaintenanceDataExport", UNSET)

        is_support_lock_type_cfg = d.pop("isSupportLockTypeCfg", UNSET)

        version = d.pop("@version", UNSET)

        xmlns = d.pop("@xmlns", UNSET)

        root_type_for_xml_cap_access_control_access_control = cls(
            is_support_wiegand_cfg=is_support_wiegand_cfg,
            is_support_module_status=is_support_module_status,
            is_support_snap_config=is_support_snap_config,
            local_controller=local_controller,
            is_support_usb_manage=is_support_usb_manage,
            is_support_identity_terminal=is_support_identity_terminal,
            is_support_department_param=is_support_department_param,
            is_support_schedule_plan=is_support_schedule_plan,
            is_support_attendance_rule=is_support_attendance_rule,
            is_support_ordinary_class=is_support_ordinary_class,
            is_support_working_class=is_support_working_class,
            is_support_attendance_holiday_group=is_support_attendance_holiday_group,
            is_support_attendance_holiday_plan=is_support_attendance_holiday_plan,
            is_support_ladder_control_relay=is_support_ladder_control_relay,
            is_support_wiegand_rule_cfg=is_support_wiegand_rule_cfg,
            is_support_m1_card_encrypt_cfg=is_support_m1_card_encrypt_cfg,
            is_support_deploy_info=is_support_deploy_info,
            is_support_submarine_back=is_support_submarine_back,
            is_support_submarine_back_host_info=is_support_submarine_back_host_info,
            is_support_start_reader_info=is_support_start_reader_info,
            is_support_submarine_back_reader=is_support_submarine_back_reader,
            is_support_server_device=is_support_server_device,
            is_support_reader_across_host=is_support_reader_across_host,
            is_support_clear_card_record=is_support_clear_card_record,
            is_support_submarine_back_mode=is_support_submarine_back_mode,
            is_support_clear_submarine_back=is_support_clear_submarine_back,
            is_support_remote_control_door=is_support_remote_control_door,
            is_support_user_info=is_support_user_info,
            employee_no_info=employee_no_info,
            is_support_card_info=is_support_card_info,
            is_support_user_info_detail_delete=is_support_user_info_detail_delete,
            is_support_auth_code_info=is_support_auth_code_info,
            is_support_finger_print_cfg=is_support_finger_print_cfg,
            is_support_finger_print_delete=is_support_finger_print_delete,
            is_support_capture_finger_print=is_support_capture_finger_print,
            is_support_door_status_week_plan_cfg=is_support_door_status_week_plan_cfg,
            is_support_verify_week_plan_cfg=is_support_verify_week_plan_cfg,
            is_support_card_right_week_plan_cfg=is_support_card_right_week_plan_cfg,
            is_support_door_status_holiday_plan_cfg=is_support_door_status_holiday_plan_cfg,
            is_support_verify_holiday_plan_cfg=is_support_verify_holiday_plan_cfg,
            is_support_card_right_holiday_plan_cfg=is_support_card_right_holiday_plan_cfg,
            is_support_door_status_holiday_group_cfg=is_support_door_status_holiday_group_cfg,
            is_support_verify_holiday_group_cfg=is_support_verify_holiday_group_cfg,
            is_support_user_right_holiday_group_cfg=is_support_user_right_holiday_group_cfg,
            is_support_door_status_plan_template=is_support_door_status_plan_template,
            is_support_verify_plan_template=is_support_verify_plan_template,
            is_support_user_right_plan_template=is_support_user_right_plan_template,
            is_support_door_status_plan=is_support_door_status_plan,
            is_support_card_reader_plan=is_support_card_reader_plan,
            is_support_clear_plans_cfg=is_support_clear_plans_cfg,
            is_support_remote_control_buzzer=is_support_remote_control_buzzer,
            is_support_event_card_no_list=is_support_event_card_no_list,
            is_support_event_card_linkage_cfg=is_support_event_card_linkage_cfg,
            is_support_clear_event_card_linkage_cfg=is_support_clear_event_card_linkage_cfg,
            is_support_acs_event=is_support_acs_event,
            is_support_acs_event_total_num=is_support_acs_event_total_num,
            is_support_event_optimization_cfg=is_support_event_optimization_cfg,
            is_support_acs_work_status=is_support_acs_work_status,
            is_support_door_cfg=is_support_door_cfg,
            is_support_card_reader_cfg=is_support_card_reader_cfg,
            is_support_acs_cfg=is_support_acs_cfg,
            is_support_group_cfg=is_support_group_cfg,
            is_support_clear_group_cfg=is_support_clear_group_cfg,
            is_support_multi_card_cfg=is_support_multi_card_cfg,
            is_support_multi_door_inter_lock_cfg=is_support_multi_door_inter_lock_cfg,
            is_support_anti_sneak_cfg=is_support_anti_sneak_cfg,
            is_support_card_reader_anti_sneak_cfg=is_support_card_reader_anti_sneak_cfg,
            is_support_clear_anti_sneak_cfg=is_support_clear_anti_sneak_cfg,
            is_support_clear_anti_sneak=is_support_clear_anti_sneak,
            is_support_sms_relative_param=is_support_sms_relative_param,
            is_support_phone_door_right_cfg=is_support_phone_door_right_cfg,
            is_support_osdp_status=is_support_osdp_status,
            is_support_osdp_modify=is_support_osdp_modify,
            is_support_log_mode_cfg=is_support_log_mode_cfg,
            factory_reset=factory_reset,
            is_support_nfc_cfg=is_support_nfc_cfg,
            is_support_rf_card_cfg=is_support_rf_card_cfg,
            is_support_capture_face=is_support_capture_face,
            is_support_capture_infrared_face=is_support_capture_infrared_face,
            is_support_face_recognize_mode=is_support_face_recognize_mode,
            is_support_remote_control_pw_chcek=is_support_remote_control_pw_chcek,
            is_support_remote_control_pw_cfg=is_support_remote_control_pw_cfg,
            is_support_attendance_status_mode_cfg=is_support_attendance_status_mode_cfg,
            is_support_attendance_status_rule_cfg=is_support_attendance_status_rule_cfg,
            is_support_capture_card_info=is_support_capture_card_info,
            is_support_capture_id_info=is_support_capture_id_info,
            is_support_capture_rule=is_support_capture_rule,
            is_support_capture_preset_param=is_support_capture_preset_param,
            is_support_offline_capture=is_support_offline_capture,
            is_support_card_operations=is_support_card_operations,
            is_support_right_controller_audio=is_support_right_controller_audio,
            is_support_channel_controller_cfg=is_support_channel_controller_cfg,
            is_support_gate_dial_and_info=is_support_gate_dial_and_info,
            is_support_gate_status=is_support_gate_status,
            is_support_gate_ir_status=is_support_gate_ir_status,
            is_support_gate_related_parts_status=is_support_gate_related_parts_status,
            is_support_channel_controller_alarm_linkage=is_support_channel_controller_alarm_linkage,
            is_support_channel_controller_alarm_out=is_support_channel_controller_alarm_out,
            is_support_channel_controller_alarm_out_control=is_support_channel_controller_alarm_out_control,
            is_support_channel_controller_type_cfg=is_support_channel_controller_type_cfg,
            is_support_tts_text=is_support_tts_text,
            is_support_id_black_list_cfg=is_support_id_black_list_cfg,
            is_support_user_data_import=is_support_user_data_import,
            is_support_user_data_export=is_support_user_data_export,
            is_support_maintenance_data_export=is_support_maintenance_data_export,
            is_support_lock_type_cfg=is_support_lock_type_cfg,
            version=version,
            xmlns=xmlns,
        )

        root_type_for_xml_cap_access_control_access_control.additional_properties = d
        return root_type_for_xml_cap_access_control_access_control

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
