from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_ethernet_broken import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusEthernetBroken,
    )
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_hard_disk_error import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskError,
    )
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_hard_disk_full import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskFull,
    )
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_illegal_access import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIllegalAccess,
    )
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_ipaddr_conflict import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIpaddrConflict,
    )
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_raid_logic_disk_error import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRaidLogicDiskError,
    )
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_record_error import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRecordError,
    )
    from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_spare_work_device_error import (
        RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusSpareWorkDeviceError,
    )


T = TypeVar("T", bound="RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus")


@attr.s(auto_attribs=True)
class RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatus:
    """
    Attributes:
        hard_disk_full (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskFull]):
        hard_disk_error (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskError]):
        ethernet_broken (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusEthernetBroken]):
        ipaddr_conflict (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIpaddrConflict]):
        illegal_access (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIllegalAccess]):
        record_error (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRecordError]):
        raid_logic_disk_error (Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRaidLogicDiskError]):
        spare_work_device_error (Union[Unset,
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusSpareWorkDeviceError]):
    """

    hard_disk_full: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskFull"] = UNSET
    hard_disk_error: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskError"] = UNSET
    ethernet_broken: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusEthernetBroken"] = UNSET
    ipaddr_conflict: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIpaddrConflict"] = UNSET
    illegal_access: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIllegalAccess"] = UNSET
    record_error: Union[Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRecordError"] = UNSET
    raid_logic_disk_error: Union[
        Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRaidLogicDiskError"
    ] = UNSET
    spare_work_device_error: Union[
        Unset, "RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusSpareWorkDeviceError"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hard_disk_full: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hard_disk_full, Unset):
            hard_disk_full = self.hard_disk_full.to_dict()

        hard_disk_error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hard_disk_error, Unset):
            hard_disk_error = self.hard_disk_error.to_dict()

        ethernet_broken: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ethernet_broken, Unset):
            ethernet_broken = self.ethernet_broken.to_dict()

        ipaddr_conflict: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ipaddr_conflict, Unset):
            ipaddr_conflict = self.ipaddr_conflict.to_dict()

        illegal_access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.illegal_access, Unset):
            illegal_access = self.illegal_access.to_dict()

        record_error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_error, Unset):
            record_error = self.record_error.to_dict()

        raid_logic_disk_error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.raid_logic_disk_error, Unset):
            raid_logic_disk_error = self.raid_logic_disk_error.to_dict()

        spare_work_device_error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spare_work_device_error, Unset):
            spare_work_device_error = self.spare_work_device_error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hard_disk_full is not UNSET:
            field_dict["hardDiskFull"] = hard_disk_full
        if hard_disk_error is not UNSET:
            field_dict["hardDiskError"] = hard_disk_error
        if ethernet_broken is not UNSET:
            field_dict["ethernetBroken"] = ethernet_broken
        if ipaddr_conflict is not UNSET:
            field_dict["ipaddrConflict"] = ipaddr_conflict
        if illegal_access is not UNSET:
            field_dict["illegalAccess"] = illegal_access
        if record_error is not UNSET:
            field_dict["recordError"] = record_error
        if raid_logic_disk_error is not UNSET:
            field_dict["raidLogicDiskError"] = raid_logic_disk_error
        if spare_work_device_error is not UNSET:
            field_dict["spareWorkDeviceError"] = spare_work_device_error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_ethernet_broken import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusEthernetBroken,
        )
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_hard_disk_error import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskError,
        )
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_hard_disk_full import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskFull,
        )
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_illegal_access import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIllegalAccess,
        )
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_ipaddr_conflict import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIpaddrConflict,
        )
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_raid_logic_disk_error import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRaidLogicDiskError,
        )
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_record_error import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRecordError,
        )
        from ..models.root_type_for_xml_device_info_device_info_detail_abnormal_status_spare_work_device_error import (
            RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusSpareWorkDeviceError,
        )

        d = src_dict.copy()
        _hard_disk_full = d.pop("hardDiskFull", UNSET)
        hard_disk_full: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskFull]
        if isinstance(_hard_disk_full, Unset):
            hard_disk_full = UNSET
        else:
            hard_disk_full = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskFull.from_dict(
                _hard_disk_full
            )

        _hard_disk_error = d.pop("hardDiskError", UNSET)
        hard_disk_error: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskError]
        if isinstance(_hard_disk_error, Unset):
            hard_disk_error = UNSET
        else:
            hard_disk_error = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusHardDiskError.from_dict(
                _hard_disk_error
            )

        _ethernet_broken = d.pop("ethernetBroken", UNSET)
        ethernet_broken: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusEthernetBroken]
        if isinstance(_ethernet_broken, Unset):
            ethernet_broken = UNSET
        else:
            ethernet_broken = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusEthernetBroken.from_dict(
                _ethernet_broken
            )

        _ipaddr_conflict = d.pop("ipaddrConflict", UNSET)
        ipaddr_conflict: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIpaddrConflict]
        if isinstance(_ipaddr_conflict, Unset):
            ipaddr_conflict = UNSET
        else:
            ipaddr_conflict = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIpaddrConflict.from_dict(
                _ipaddr_conflict
            )

        _illegal_access = d.pop("illegalAccess", UNSET)
        illegal_access: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIllegalAccess]
        if isinstance(_illegal_access, Unset):
            illegal_access = UNSET
        else:
            illegal_access = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusIllegalAccess.from_dict(
                _illegal_access
            )

        _record_error = d.pop("recordError", UNSET)
        record_error: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRecordError]
        if isinstance(_record_error, Unset):
            record_error = UNSET
        else:
            record_error = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRecordError.from_dict(_record_error)

        _raid_logic_disk_error = d.pop("raidLogicDiskError", UNSET)
        raid_logic_disk_error: Union[Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRaidLogicDiskError]
        if isinstance(_raid_logic_disk_error, Unset):
            raid_logic_disk_error = UNSET
        else:
            raid_logic_disk_error = RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusRaidLogicDiskError.from_dict(
                _raid_logic_disk_error
            )

        _spare_work_device_error = d.pop("spareWorkDeviceError", UNSET)
        spare_work_device_error: Union[
            Unset, RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusSpareWorkDeviceError
        ]
        if isinstance(_spare_work_device_error, Unset):
            spare_work_device_error = UNSET
        else:
            spare_work_device_error = (
                RootTypeForXMLDeviceInfoDeviceInfoDetailAbnormalStatusSpareWorkDeviceError.from_dict(
                    _spare_work_device_error
                )
            )

        root_type_for_xml_device_info_device_info_detail_abnormal_status = cls(
            hard_disk_full=hard_disk_full,
            hard_disk_error=hard_disk_error,
            ethernet_broken=ethernet_broken,
            ipaddr_conflict=ipaddr_conflict,
            illegal_access=illegal_access,
            record_error=record_error,
            raid_logic_disk_error=raid_logic_disk_error,
            spare_work_device_error=spare_work_device_error,
        )

        root_type_for_xml_device_info_device_info_detail_abnormal_status.additional_properties = d
        return root_type_for_xml_device_info_device_info_detail_abnormal_status

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
