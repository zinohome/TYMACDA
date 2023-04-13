# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import time
from core.settings import settings
from utils.log import log as log

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

#div10list = ['i_inner_temp','i_set_temp','w_passen_load','i_seat_temp','i_veh_temp','i_seat_hum','i_veh_hum','i_fat_u1','i_rat_u1','i_dft_u11','i_dft_u12','i_sat_u11','i_sat_u12','i_suck_temp_u11','i_suck_pres_u11','i_sup_heat_u11','i_eev_pos_u11','i_suck_temp_u12','i_suck_pres_u12','i_sup_heat_u12','i_eev_pos_u12','i_fat_u2','i_rat_u2','i_dft_u21','i_dft_u22','i_sat_u21','i_sat_u22','i_suck_temp_u21','i_suck_pres_u21','i_sup_heat_u21','i_eev_pos_u21','i_suck_temp_u22','i_suck_pres_u22','i_sup_heat_u22','i_eev_pos_u22']
div10list = ['i_inner_temp','i_set_temp','i_seat_temp','i_veh_temp','i_fat_u1','i_rat_u1','i_dft_u11','i_dft_u12','i_sat_u11','i_sat_u12','i_suck_temp_u11','i_suck_pres_u11','i_sup_heat_u11','i_eev_pos_u11','i_suck_temp_u12','i_suck_pres_u12','i_sup_heat_u12','i_eev_pos_u12','i_fat_u2','i_rat_u2','i_dft_u21','i_dft_u22','i_sat_u21','i_sat_u22','i_suck_temp_u21','i_suck_pres_u21','i_sup_heat_u21','i_eev_pos_u21','i_suck_temp_u22','i_suck_pres_u22','i_sup_heat_u22','i_eev_pos_u22']
div100list = []

class Ty2status(KaitaiStruct):
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
        self.i_inner_temp = self._io.read_s2be()
        self.i_set_temp = self._io.read_s2be()
        self.w_passen_load = self._io.read_u2be()
        self.i_seat_temp = self._io.read_s2be()
        self.i_veh_temp = self._io.read_s2be()
        self.i_seat_hum = self._io.read_s2be()
        self.i_veh_hum = self._io.read_s2be()
        self.w_opmode_u1 = self._io.read_u2be()
        self.i_fat_u1 = self._io.read_s2be()
        self.i_rat_u1 = self._io.read_s2be()
        self.i_dft_u11 = self._io.read_s2be()
        self.i_dft_u12 = self._io.read_s2be()
        self.i_sat_u11 = self._io.read_s2be()
        self.i_sat_u12 = self._io.read_s2be()
        self.i_suck_temp_u11 = self._io.read_s2be()
        self.i_suck_pres_u11 = self._io.read_s2be()
        self.i_sup_heat_u11 = self._io.read_s2be()
        self.i_eev_pos_u11 = self._io.read_u2be()
        self.i_suck_temp_u12 = self._io.read_s2be()
        self.i_suck_pres_u12 = self._io.read_s2be()
        self.i_sup_heat_u12 = self._io.read_s2be()
        self.i_eev_pos_u12 = self._io.read_u2be()
        self.w_opmode_u2 = self._io.read_u2be()
        self.i_fat_u2 = self._io.read_s2be()
        self.i_rat_u2 = self._io.read_s2be()
        self.i_dft_u21 = self._io.read_s2be()
        self.i_dft_u22 = self._io.read_s2be()
        self.i_sat_u21 = self._io.read_s2be()
        self.i_sat_u22 = self._io.read_s2be()
        self.i_suck_temp_u21 = self._io.read_s2be()
        self.i_suck_pres_u21 = self._io.read_s2be()
        self.i_sup_heat_u21 = self._io.read_s2be()
        self.i_eev_pos_u21 = self._io.read_u2be()
        self.i_suck_temp_u22 = self._io.read_s2be()
        self.i_suck_pres_u22 = self._io.read_s2be()
        self.i_sup_heat_u22 = self._io.read_s2be()
        self.i_eev_pos_u22 = self._io.read_u2be()
        self.i_train_id = self._io.read_s2be()
        self.i_car_id = self._io.read_s2be()
        self.msg_reverse_3 = self._io.read_s2be()
        self.msg_reverse_4 = self._io.read_s2be()
        self.cfbk_eh_u22 = self._io.read_bits_int_be(1) != 0
        self.cfbk_eh_u21 = self._io.read_bits_int_be(1) != 0
        self.cfbk_eh_u12 = self._io.read_bits_int_be(1) != 0
        self.cfbk_eh_u11 = self._io.read_bits_int_be(1) != 0
        self.cfbk_comp_u22 = self._io.read_bits_int_be(1) != 0
        self.cfbk_comp_u21 = self._io.read_bits_int_be(1) != 0
        self.cfbk_comp_u12 = self._io.read_bits_int_be(1) != 0
        self.cfbk_comp_u11 = self._io.read_bits_int_be(1) != 0
        self._io.align_to_byte()
        self.msg_reverse_5 = self._io.read_u1()
        self.b_cpflt_comp_u12 = self._io.read_bits_int_be(1) != 0
        self.b_scflt_comp_u11 = self._io.read_bits_int_be(1) != 0
        self.b_lpflt_comp_u11 = self._io.read_bits_int_be(1) != 0
        self.b_cpflt_comp_u11 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_cf_u12 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_cf_u11 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_ef_u12 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_ef_u11 = self._io.read_bits_int_be(1) != 0
        self.b_flt_rad_u1 = self._io.read_bits_int_be(1) != 0
        self.b_flt_fad_u1 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eev_u12 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eev_u11 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eh_u12 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eh_u11 = self._io.read_bits_int_be(1) != 0
        self.b_scflt_comp_u12 = self._io.read_bits_int_be(1) != 0
        self.b_lpflt_comp_u12 = self._io.read_bits_int_be(1) != 0
        self.b_flt_expboard_u1 = self._io.read_bits_int_be(1) != 0
        self.b_flt_airclean_u1 = self._io.read_bits_int_be(1) != 0
        self.b_flt_dftemp_u12 = self._io.read_bits_int_be(1) != 0
        self.b_flt_dftemp_u11 = self._io.read_bits_int_be(1) != 0
        self.b_flt_rnttemp_u1 = self._io.read_bits_int_be(1) != 0
        self.b_flt_suplytemp_u12 = self._io.read_bits_int_be(1) != 0
        self.b_flt_suplytemp_u11 = self._io.read_bits_int_be(1) != 0
        self.b_flt_frstemp_u1 = self._io.read_bits_int_be(1) != 0
        self.b_cpflt_comp_u22 = self._io.read_bits_int_be(1) != 0
        self.b_scflt_comp_u21 = self._io.read_bits_int_be(1) != 0
        self.b_lpflt_comp_u21 = self._io.read_bits_int_be(1) != 0
        self.b_cpflt_comp_u21 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_cf_u22 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_cf_u21 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_ef_u22 = self._io.read_bits_int_be(1) != 0
        self.b_ocflt_ef_u21 = self._io.read_bits_int_be(1) != 0
        self.b_flt_rad_u2 = self._io.read_bits_int_be(1) != 0
        self.b_flt_fad_u2 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eev_u22 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eev_u21 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eh_u22 = self._io.read_bits_int_be(1) != 0
        self.b_flt_eh_u21 = self._io.read_bits_int_be(1) != 0
        self.b_scflt_comp_u22 = self._io.read_bits_int_be(1) != 0
        self.b_lpflt_comp_u22 = self._io.read_bits_int_be(1) != 0
        self.b_flt_expboard_u2 = self._io.read_bits_int_be(1) != 0
        self.b_flt_airclean_u2 = self._io.read_bits_int_be(1) != 0
        self.b_flt_dftemp_u22 = self._io.read_bits_int_be(1) != 0
        self.b_flt_dftemp_u21 = self._io.read_bits_int_be(1) != 0
        self.b_flt_rnttemp_u2 = self._io.read_bits_int_be(1) != 0
        self.b_flt_suplytemp_u22 = self._io.read_bits_int_be(1) != 0
        self.b_flt_suplytemp_u21 = self._io.read_bits_int_be(1) != 0
        self.b_flt_frstemp_u2 = self._io.read_bits_int_be(1) != 0
        self.msg_reverse_6 = self._io.read_bits_int_be(1) != 0
        self.msg_reverse_7 = self._io.read_bits_int_be(1) != 0
        self.msg_reverse_8 = self._io.read_bits_int_be(1) != 0
        self.msg_reverse_9 = self._io.read_bits_int_be(1) != 0
        self.b_flt_mvb_bus = self._io.read_bits_int_be(1) != 0
        self.b_flt_emerg_ivt = self._io.read_bits_int_be(1) != 0
        self.b_flt_seat_temp = self._io.read_bits_int_be(1) != 0
        self.b_flt_veh_temp = self._io.read_bits_int_be(1) != 0


    def from_bytes_to_dict(bytesobj):
        dev_mode = settings.DEV_MODE
        nb5dict = Ty2status.from_bytes(bytesobj).__dict__.copy()
        nb5dict[
            'msg_calc_dvc_no'] = f"0{nb5dict['msg_header_lineid']}0{str(nb5dict['i_train_id']).zfill(2)}0{nb5dict['i_car_id']}"
        nb5dict[
            'msg_calc_train_no'] = f"0{nb5dict['msg_header_lineid']}0{str(nb5dict['i_train_id']).zfill(2)}"
        nb5dict[
            'msg_calc_dvc_time'] = f"20{nb5dict['msg_header_date_year']}-{nb5dict['msg_header_date_month']}-{nb5dict['msg_header_date_day']} {nb5dict['msg_header_date_hour']}:{nb5dict['msg_header_date_minute']}:{nb5dict['msg_header_date_second']}"
        nb5dict['msg_calc_parse_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for key in ('_io', '_parent', '_root',
                    'msg_reverse_2', 'msg_reverse_3', 'msg_reverse_4', 'msg_reverse_5', 'msg_reverse_6',
                    'msg_reverse_7', 'msg_reverse_8', 'msg_reverse_8', 'msg_reverse_1', 'msg_reverse_10',
                    'dvc_cfbk_revers0', 'dvc_cfbk_revers1', 'dvc_cfbk_revers2',
                    'msg_header_date_year', 'msg_header_date_month', 'msg_header_date_day',
                    'msg_header_date_hour', 'msg_header_date_minute', 'msg_header_date_second', 'msg_header_date_msecond'):
            if key in nb5dict:
                del nb5dict[key]
        for key,value in nb5dict.items():
            if isinstance(value, bool):
                if value:
                    nb5dict[key] = 1
                else:
                    nb5dict[key] = 0
            if key in div100list:
                if value / 100 == value // 100:
                    nb5dict[key] = value // 100
                else:
                    nb5dict[key] = round(value / 100, 2)
            if key in div10list:
                if value / 10 == value // 10:
                    nb5dict[key] = value // 10
                else:
                    nb5dict[key] = round(value / 10, 1)
        return nb5dict
