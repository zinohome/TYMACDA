# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

div10list = ['dw_temp_min_out','dw_temp_max_out','dw_temp_ave_out','dw_temp_min_inn','dw_temp_max_inn','dw_temp_ave_inn']
div100list = []


class Ty2statis(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.msg_header_lineid = self._io.read_u1()
        self.msg_header_traintype = self._io.read_u1()
        self.msg_header_trainid = self._io.read_u1()
        self.msg_header_date_year = self._io.read_u1()
        self.msg_header_date_month = self._io.read_u1()
        self.msg_header_date_day = self._io.read_u1()
        self.msg_header_date_hour = self._io.read_u1()
        self.msg_header_date_minute = self._io.read_u1()
        self.msg_header_date_second = self._io.read_u1()
        self.msg_header_date_msecond = self._io.read_s2be()
        self.dw_temp_min_out = self._io.read_s2be()
        self.dw_temp_max_out = self._io.read_s2be()
        self.dw_temp_ave_out = self._io.read_s2be()
        self.dw_temp_min_inn = self._io.read_s2be()
        self.dw_temp_max_inn = self._io.read_s2be()
        self.dw_temp_ave_inn = self._io.read_s2be()
        self.dw_optime_emerg_ivt = self._io.read_u4be()
        self.dw_oppdtime_emmerg_ivt = self._io.read_u4be()
        self.dw_opcount_emerg_ivt = self._io.read_u4be()
        self.dw_oppdcount_emerg_ivt = self._io.read_u4be()
        self.dw_optime_ef_u1 = self._io.read_u4be()
        self.dw_optime_cf_u1 = self._io.read_u4be()
        self.dw_optime_comp_u11 = self._io.read_u4be()
        self.dw_optime_comp_u12 = self._io.read_u4be()
        self.dw_optime_eh_u11 = self._io.read_u4be()
        self.dw_optime_eh_u12 = self._io.read_u4be()
        self.dw_oppdtime_ef_u1 = self._io.read_u4be()
        self.dw_oppdtime_cf_u1 = self._io.read_u4be()
        self.dw_oppdtime_comp_u11 = self._io.read_u4be()
        self.dw_oppdtime_comp_u12 = self._io.read_u4be()
        self.dw_opcount_cp_u11 = self._io.read_u4be()
        self.dw_opcount_cp_u12 = self._io.read_u4be()
        self.dw_opcount_eh_u11 = self._io.read_u4be()
        self.dw_opcount_eh_u12 = self._io.read_u4be()
        self.dw_opcount_fad_u1 = self._io.read_u4be()
        self.dw_opcount_rad_u1 = self._io.read_u4be()
        self.dw_oppdcount_ef_u1 = self._io.read_u4be()
        self.dw_oppdcount_cp_u11 = self._io.read_u4be()
        self.dw_oppdcount_cp_u12 = self._io.read_u4be()
        self.dw_oppdcount_eh_u11 = self._io.read_u4be()
        self.dw_oppdcount_eh_u12 = self._io.read_u4be()
        self.dw_oppdcount_fad_u1 = self._io.read_u4be()
        self.dw_oppdcount_rad_u1 = self._io.read_u4be()
        self.dw_optime_ef_u2 = self._io.read_u4be()
        self.dw_optime_cf_u2 = self._io.read_u4be()
        self.dw_optime_comp_u21 = self._io.read_u4be()
        self.dw_optime_comp_u22 = self._io.read_u4be()
        self.dw_optime_eh_u21 = self._io.read_u4be()
        self.dw_optime_eh_u22 = self._io.read_u4be()
        self.dw_oppdtime_ef_u2 = self._io.read_u4be()
        self.dw_oppdtime_cf_u2 = self._io.read_u4be()
        self.dw_oppdtime_comp_u21 = self._io.read_u4be()
        self.dw_oppdtime_comp_u22 = self._io.read_u4be()
        self.dw_opcount_cp_u21 = self._io.read_u4be()
        self.dw_opcount_cp_u22 = self._io.read_u4be()
        self.dw_opcount_eh_u21 = self._io.read_u4be()
        self.dw_opcount_eh_u22 = self._io.read_u4be()
        self.dw_opcount_fad_u2 = self._io.read_u4be()
        self.dw_opcount_rad_u2 = self._io.read_u4be()
        self.dw_oppdcount_ef_u2 = self._io.read_u4be()
        self.dw_oppdcount_cp_u21 = self._io.read_u4be()
        self.dw_oppdcount_cp_u22 = self._io.read_u4be()
        self.dw_oppdcount_eh_u21 = self._io.read_u4be()
        self.dw_oppdcount_eh_u22 = self._io.read_u4be()
        self.dw_oppdcount_fad_u2 = self._io.read_u4be()
        self.dw_oppdcount_rad_u2 = self._io.read_u4be()
        self.i_train_id = self._io.read_s2be()
        self.i_car_id = self._io.read_s2be()


