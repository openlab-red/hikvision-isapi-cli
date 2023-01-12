from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_cap_access_control_access_control import RootTypeForXMLCapAccessControlAccessControl


T = TypeVar("T", bound="RootTypeForXMLCapAccessControl")


@attr.s(auto_attribs=True)
class RootTypeForXMLCapAccessControl:
    """AccessControl capability message in XML format

    Example:
        {'AccessControl': {'isSupportWiegandCfg': {}, 'isSupportModuleStatus': {}, 'isSupportSNAPConfig': {},
            'LocalController': {'isSupportLocalControllerManage': {}, 'isSupportLocalControllerControl': {}},
            'isSupportUSBManage': {}, 'isSupportIdentityTerminal': {}, 'isSupportDepartmentParam': {},
            'isSupportSchedulePlan': {}, 'isSupportAttendanceRule': {}, 'isSupportOrdinaryClass': {},
            'isSupportWorkingClass': {}, 'isSupportAttendanceHolidayGroup': {}, 'isSupportAttendanceHolidayPlan': {},
            'isSupportLadderControlRelay': {}, 'isSupportWiegandRuleCfg': {}, 'isSupportM1CardEncryptCfg': {},
            'isSupportDeployInfo': [{}, {}], 'isSupportSubmarineBack': {}, 'isSupportSubmarineBackHostInfo': {},
            'isSupportStartReaderInfo': {}, 'isSupportSubmarineBackReader': {}, 'isSupportServerDevice': {},
            'isSupportReaderAcrossHost': {}, 'isSupportClearCardRecord': {}, 'isSupportSubmarineBackMode': {},
            'isSupportClearSubmarineBack': {}, 'isSupportRemoteControlDoor': {}, 'isSupportUserInfo': '', 'EmployeeNoInfo':
            {'employeeNo': {'@min': '', '@max': ''}, 'characterType': {'@opt': 'any,number'}, 'isSupportCompress': {}},
            'isSupportCardInfo': '', 'isSupportUserInfoDetailDelete': '', 'isSupportAuthCodeInfo': {},
            'isSupportFingerPrintCfg': {}, 'isSupportFingerPrintDelete': {}, 'isSupportCaptureFingerPrint': {},
            'isSupportDoorStatusWeekPlanCfg': {}, 'isSupportVerifyWeekPlanCfg': {}, 'isSupportCardRightWeekPlanCfg': {},
            'isSupportDoorStatusHolidayPlanCfg': {}, 'isSupportVerifyHolidayPlanCfg': {},
            'isSupportCardRightHolidayPlanCfg': {}, 'isSupportDoorStatusHolidayGroupCfg': {},
            'isSupportVerifyHolidayGroupCfg': {}, 'isSupportUserRightHolidayGroupCfg': {},
            'isSupportDoorStatusPlanTemplate': {}, 'isSupportVerifyPlanTemplate': {}, 'isSupportUserRightPlanTemplate': {},
            'isSupportDoorStatusPlan': {}, 'isSupportCardReaderPlan': {}, 'isSupportClearPlansCfg': {},
            'isSupportRemoteControlBuzzer': {}, 'isSupportEventCardNoList': {}, 'isSupportEventCardLinkageCfg': {},
            'isSupportClearEventCardLinkageCfg': {}, 'isSupportAcsEvent': {}, 'isSupportAcsEventTotalNum': {},
            'isSupportEventOptimizationCfg': {}, 'isSupportAcsWorkStatus': {}, 'isSupportDoorCfg': {},
            'isSupportCardReaderCfg': {}, 'isSupportAcsCfg': {}, 'isSupportGroupCfg': {}, 'isSupportClearGroupCfg': {},
            'isSupportMultiCardCfg': {}, 'isSupportMultiDoorInterLockCfg': {}, 'isSupportAntiSneakCfg': {},
            'isSupportCardReaderAntiSneakCfg': {}, 'isSupportClearAntiSneakCfg': {}, 'isSupportClearAntiSneak': {},
            'isSupportSmsRelativeParam': {}, 'isSupportPhoneDoorRightCfg': {}, 'isSupportOSDPStatus': {},
            'isSupportOSDPModify': {}, 'isSupportLogModeCfg': {}, 'FactoryReset': {'isSupportFactoryReset': '', 'mode':
            {'@opt': 'full,basic,part'}}, 'isSupportNFCCfg': '', 'isSupportRFCardCfg': '', 'isSupportCaptureFace': {},
            'isSupportCaptureInfraredFace': {}, 'isSupportFaceRecognizeMode': {}, 'isSupportRemoteControlPWChcek': {},
            'isSupportRemoteControlPWCfg': {}, 'isSupportAttendanceStatusModeCfg': {}, 'isSupportAttendanceStatusRuleCfg':
            {}, 'isSupportCaptureCardInfo': {}, 'isSupportCaptureIDInfo': {}, 'isSupportCaptureRule': {},
            'isSupportCapturePresetParam': {}, 'isSupportOfflineCapture': {}, 'isSupportCardOperations': {},
            'isSupportRightControllerAudio': {}, 'isSupportChannelControllerCfg': {}, 'isSupportGateDialAndInfo': {},
            'isSupportGateStatus': {}, 'isSupportGateIRStatus': {}, 'isSupportGateRelatedPartsStatus': {},
            'isSupportChannelControllerAlarmLinkage': {}, 'isSupportChannelControllerAlarmOut': {},
            'isSupportChannelControllerAlarmOutControl': {}, 'isSupportChannelControllerTypeCfg': {}, 'isSupportTTSText':
            '', 'isSupportIDBlackListCfg': '', 'isSupportUserDataImport': '', 'isSupportUserDataExport': '',
            'isSupportMaintenanceDataExport': '', 'isSupportLockTypeCfg': '', '@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema'}}

    Attributes:
        access_control (Union[Unset, RootTypeForXMLCapAccessControlAccessControl]):
    """

    access_control: Union[Unset, "RootTypeForXMLCapAccessControlAccessControl"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_control: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_control, Unset):
            access_control = self.access_control.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_control is not UNSET:
            field_dict["AccessControl"] = access_control

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_cap_access_control_access_control import (
            RootTypeForXMLCapAccessControlAccessControl,
        )

        d = src_dict.copy()
        _access_control = d.pop("AccessControl", UNSET)
        access_control: Union[Unset, RootTypeForXMLCapAccessControlAccessControl]
        if isinstance(_access_control, Unset):
            access_control = UNSET
        else:
            access_control = RootTypeForXMLCapAccessControlAccessControl.from_dict(_access_control)

        root_type_for_xml_cap_access_control = cls(
            access_control=access_control,
        )

        root_type_for_xml_cap_access_control.additional_properties = d
        return root_type_for_xml_cap_access_control

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
