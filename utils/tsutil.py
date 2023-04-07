#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: MACDA
import traceback
import weakref
import psycopg2
from datetime import datetime
from pgcopy import CopyManager
from psycopg2 import pool
from core.settings import settings
from utils.log import log as log
from collections import Counter
import simplejson as json
import binascii


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj
class TSutil(metaclass=Cached):
    def __init__(self):
        log.debug('Connect to timescaledb uri [ %s ]' % settings.TSDB_URL)
        self.conn_pool = psycopg2.pool.SimpleConnectionPool(1, settings.TSDB_POOL_SIZE, settings.TSDB_URL)
        if (self.conn_pool):
            log.debug("Connection pool created successfully")
        try:
            log.debug("Check tsdb table ...")
            conn = self.conn_pool.getconn()
            create_status_table = "CREATE TABLE IF NOT EXISTS status_macda (msg_calc_dvc_time TIMESTAMPTZ NOT NULL, msg_calc_parse_time TEXT NOT NULL, msg_calc_dvc_no TEXT NOT NULL, msg_calc_train_no TEXT NOT NULL, i_inner_temp DOUBLE PRECISION NULL, i_set_temp DOUBLE PRECISION NULL, w_passen_load DOUBLE PRECISION NULL, i_seat_temp DOUBLE PRECISION NULL, i_veh_temp DOUBLE PRECISION NULL, i_seat_hum DOUBLE PRECISION NULL, i_veh_hum DOUBLE PRECISION NULL, w_opmode_u1 DOUBLE PRECISION NULL, i_fat_u1 DOUBLE PRECISION NULL, i_rat_u1 DOUBLE PRECISION NULL, i_dft_u11 DOUBLE PRECISION NULL, i_dft_u12 DOUBLE PRECISION NULL, i_sat_u11 DOUBLE PRECISION NULL, i_sat_u12 DOUBLE PRECISION NULL, i_suck_temp_u11 DOUBLE PRECISION NULL, i_suck_pres_u11 DOUBLE PRECISION NULL, i_sup_heat_u11 DOUBLE PRECISION NULL, i_eev_pos_u11 DOUBLE PRECISION NULL, i_suck_temp_u12 DOUBLE PRECISION NULL, i_suck_pres_u12 DOUBLE PRECISION NULL, i_sup_heat_u12 DOUBLE PRECISION NULL, i_eev_pos_u12 DOUBLE PRECISION NULL, w_opmode_u2 DOUBLE PRECISION NULL, i_fat_u2 DOUBLE PRECISION NULL, i_rat_u2 DOUBLE PRECISION NULL, i_dft_u21 DOUBLE PRECISION NULL, i_dft_u22 DOUBLE PRECISION NULL, i_sat_u21 DOUBLE PRECISION NULL, i_sat_u22 DOUBLE PRECISION NULL, i_suck_temp_u21 DOUBLE PRECISION NULL, i_suck_pres_u21 DOUBLE PRECISION NULL, i_sup_heat_u21 DOUBLE PRECISION NULL, i_eev_pos_u21 DOUBLE PRECISION NULL, i_suck_temp_u22 DOUBLE PRECISION NULL, i_suck_pres_u22 DOUBLE PRECISION NULL, i_sup_heat_u22 DOUBLE PRECISION NULL, i_eev_pos_u22 DOUBLE PRECISION NULL, i_train_id DOUBLE PRECISION NULL, i_car_id DOUBLE PRECISION NULL, msg_reverse_3 DOUBLE PRECISION NULL, msg_reverse_4 DOUBLE PRECISION NULL, cfbk_eh_u22 DOUBLE PRECISION NULL, cfbk_eh_u21 DOUBLE PRECISION NULL, cfbk_eh_u12 DOUBLE PRECISION NULL, cfbk_eh_u11 DOUBLE PRECISION NULL, cfbk_comp_u22 DOUBLE PRECISION NULL, cfbk_comp_u21 DOUBLE PRECISION NULL, cfbk_comp_u12 DOUBLE PRECISION NULL, cfbk_comp_u11 DOUBLE PRECISION NULL, msg_reverse_5 DOUBLE PRECISION NULL, b_cpflt_comp_u12 DOUBLE PRECISION NULL, b_scflt_comp_u11 DOUBLE PRECISION NULL, b_lpflt_comp_u11 DOUBLE PRECISION NULL, b_cpflt_comp_u11 DOUBLE PRECISION NULL, b_ocflt_cf_u12 DOUBLE PRECISION NULL, b_ocflt_cf_u11 DOUBLE PRECISION NULL, b_ocflt_ef_u12 DOUBLE PRECISION NULL, b_ocflt_ef_u11 DOUBLE PRECISION NULL, b_flt_rad_u1 DOUBLE PRECISION NULL, b_flt_fad_u1 DOUBLE PRECISION NULL, b_flt_eev_u12 DOUBLE PRECISION NULL, b_flt_eev_u11 DOUBLE PRECISION NULL, b_flt_eh_u12 DOUBLE PRECISION NULL, b_flt_eh_u11 DOUBLE PRECISION NULL, b_scflt_comp_u12 DOUBLE PRECISION NULL, b_lpflt_comp_u12 DOUBLE PRECISION NULL, b_flt_expboard_u1 DOUBLE PRECISION NULL, b_flt_airclean_u1 DOUBLE PRECISION NULL, b_flt_dftemp_u12 DOUBLE PRECISION NULL, b_flt_dftemp_u11 DOUBLE PRECISION NULL, b_flt_rnttemp_u1 DOUBLE PRECISION NULL, b_flt_suplytemp_u12 DOUBLE PRECISION NULL, b_flt_suplytemp_u11 DOUBLE PRECISION NULL, b_flt_frstemp_u1 DOUBLE PRECISION NULL, b_cpflt_comp_u22 DOUBLE PRECISION NULL, b_scflt_comp_u21 DOUBLE PRECISION NULL, b_lpflt_comp_u21 DOUBLE PRECISION NULL, b_cpflt_comp_u21 DOUBLE PRECISION NULL, b_ocflt_cf_u22 DOUBLE PRECISION NULL, b_ocflt_cf_u21 DOUBLE PRECISION NULL, b_ocflt_ef_u22 DOUBLE PRECISION NULL, b_ocflt_ef_u21 DOUBLE PRECISION NULL, b_flt_rad_u2 DOUBLE PRECISION NULL, b_flt_fad_u2 DOUBLE PRECISION NULL, b_flt_eev_u22 DOUBLE PRECISION NULL, b_flt_eev_u21 DOUBLE PRECISION NULL, b_flt_eh_u22 DOUBLE PRECISION NULL, b_flt_eh_u21 DOUBLE PRECISION NULL, b_scflt_comp_u22 DOUBLE PRECISION NULL, b_lpflt_comp_u22 DOUBLE PRECISION NULL, b_flt_expboard_u2 DOUBLE PRECISION NULL, b_flt_airclean_u2 DOUBLE PRECISION NULL, b_flt_dftemp_u22 DOUBLE PRECISION NULL, b_flt_dftemp_u21 DOUBLE PRECISION NULL, b_flt_rnttemp_u2 DOUBLE PRECISION NULL, b_flt_suplytemp_u22 DOUBLE PRECISION NULL, b_flt_suplytemp_u21 DOUBLE PRECISION NULL, b_flt_frstemp_u2 DOUBLE PRECISION NULL, msg_reverse_6 DOUBLE PRECISION NULL, msg_reverse_7 DOUBLE PRECISION NULL, msg_reverse_8 DOUBLE PRECISION NULL, msg_reverse_9 DOUBLE PRECISION NULL, b_flt_mvb_bus DOUBLE PRECISION NULL, b_flt_emerg_ivt DOUBLE PRECISION NULL, b_flt_seat_temp DOUBLE PRECISION NULL, b_flt_veh_temp DOUBLE PRECISION NULL);"
            create_statis_table = "CREATE TABLE IF NOT EXISTS statis_macda (msg_calc_dvc_time TIMESTAMPTZ NOT NULL, msg_calc_parse_time TEXT NOT NULL, msg_calc_dvc_no TEXT NOT NULL, msg_calc_train_no TEXT NOT NULL, dw_temp_min_out DOUBLE PRECISION NULL, dw_temp_max_out DOUBLE PRECISION NULL, dw_temp_ave_out DOUBLE PRECISION NULL, dw_temp_min_inn DOUBLE PRECISION NULL, dw_temp_max_inn DOUBLE PRECISION NULL, dw_temp_ave_inn DOUBLE PRECISION NULL, dw_optime_emerg_ivt DOUBLE PRECISION NULL, dw_oppdtime_emmerg_ivt DOUBLE PRECISION NULL, dw_opcount_emerg_ivt DOUBLE PRECISION NULL, dw_oppdcount_emerg_ivt DOUBLE PRECISION NULL, dw_optime_ef_u1 DOUBLE PRECISION NULL, dw_optime_cf_u1 DOUBLE PRECISION NULL, dw_optime_comp_u11 DOUBLE PRECISION NULL, dw_optime_comp_u12 DOUBLE PRECISION NULL, dw_optime_eh_u11 DOUBLE PRECISION NULL, dw_optime_eh_u12 DOUBLE PRECISION NULL, dw_oppdtime_ef_u1 DOUBLE PRECISION NULL, dw_oppdtime_cf_u1 DOUBLE PRECISION NULL, dw_oppdtime_comp_u11 DOUBLE PRECISION NULL, dw_oppdtime_comp_u12 DOUBLE PRECISION NULL, dw_opcount_cp_u11 DOUBLE PRECISION NULL, dw_opcount_cp_u12 DOUBLE PRECISION NULL, dw_opcount_eh_u11 DOUBLE PRECISION NULL, dw_opcount_eh_u12 DOUBLE PRECISION NULL, dw_opcount_fad_u1 DOUBLE PRECISION NULL, dw_opcount_rad_u1 DOUBLE PRECISION NULL, dw_oppdcount_ef_u1 DOUBLE PRECISION NULL, dw_oppdcount_cp_u11 DOUBLE PRECISION NULL, dw_oppdcount_cp_u12 DOUBLE PRECISION NULL, dw_oppdcount_eh_u11 DOUBLE PRECISION NULL, dw_oppdcount_eh_u12 DOUBLE PRECISION NULL, dw_oppdcount_fad_u1 DOUBLE PRECISION NULL, dw_oppdcount_rad_u1 DOUBLE PRECISION NULL, dw_optime_ef_u2 DOUBLE PRECISION NULL, dw_optime_cf_u2 DOUBLE PRECISION NULL, dw_optime_comp_u21 DOUBLE PRECISION NULL, dw_optime_comp_u22 DOUBLE PRECISION NULL, dw_optime_eh_u21 DOUBLE PRECISION NULL, dw_optime_eh_u22 DOUBLE PRECISION NULL, dw_oppdtime_ef_u2 DOUBLE PRECISION NULL, dw_oppdtime_cf_u2 DOUBLE PRECISION NULL, dw_oppdtime_comp_u21 DOUBLE PRECISION NULL, dw_oppdtime_comp_u22 DOUBLE PRECISION NULL, dw_opcount_cp_u21 DOUBLE PRECISION NULL, dw_opcount_cp_u22 DOUBLE PRECISION NULL, dw_opcount_eh_u21 DOUBLE PRECISION NULL, dw_opcount_eh_u22 DOUBLE PRECISION NULL, dw_opcount_fad_u2 DOUBLE PRECISION NULL, dw_opcount_rad_u2 DOUBLE PRECISION NULL, dw_oppdcount_ef_u2 DOUBLE PRECISION NULL, dw_oppdcount_cp_u21 DOUBLE PRECISION NULL, dw_oppdcount_cp_u22 DOUBLE PRECISION NULL, dw_oppdcount_eh_u21 DOUBLE PRECISION NULL, dw_oppdcount_eh_u22 DOUBLE PRECISION NULL, dw_oppdcount_fad_u2 DOUBLE PRECISION NULL, dw_oppdcount_rad_u2 DOUBLE PRECISION NULL, i_train_id DOUBLE PRECISION NULL, i_car_id DOUBLE PRECISION NULL);"
            cur = conn.cursor()
            cur.execute(create_status_table)
            cur.execute(create_statis_table)
            cur.execute("SELECT create_hypertable('status_macda', 'msg_calc_dvc_time', chunk_time_interval => 86400000000, if_not_exists => TRUE);")
            cur.execute("SELECT add_retention_policy('status_macda', INTERVAL '5 year', if_not_exists => true);")
            cur.execute("SELECT create_hypertable('statis_macda', 'msg_calc_dvc_time', chunk_time_interval => 86400000000, if_not_exists => TRUE);")
            cur.execute("SELECT add_retention_policy('statis_macda', INTERVAL '5 year', if_not_exists => true);")
            conn.commit()
            cur.close()
            self.conn_pool.putconn(conn)
            log.debug("Check tsdb table ... Success !")
        except Exception as exp:
            log.error('Exception at tsutil.__init__() %s ' % exp)
            traceback.print_exc()

    def insert(self, tablename, jsonobj):
        keylst = []
        valuelst = []
        masklst = []
        ignorekeys = ['msg_header_lineid', 'msg_header_traintype', 'msg_header_trainid', 'msg_header_date_year',
                      'msg_header_date_month','msg_msgtype',
                      'msg_header_date_day', 'msg_header_date_hour', 'msg_header_date_minute', 'msg_header_date_second',
                      'msg_header_date_msecond']
        for (key, value) in jsonobj.items():
            if not key in ignorekeys:
                keylst.append(key)
                valuelst.append(str(value))
                masklst.append('%s')
        keystr = ','.join(keylst)
        maskstr = ','.join(masklst)
        insertsql = f"INSERT INTO {tablename} ({keystr}) VALUES ({maskstr})"
        # log.debug(insertsql)
        try:
            conn = self.conn_pool.getconn()
            cur = conn.cursor()
            cur.execute(insertsql, valuelst)
            conn.commit()
            cur.close()
            self.conn_pool.putconn(conn)
        except Exception as exp:
            log.error('Exception at tsutil.insert() %s ' % exp)
            traceback.print_exc()

    def batchinsert(self, tablename, timefieldname, jsonobjlst):
        ignorekeys = ['msg_header_lineid', 'msg_header_traintype', 'msg_header_trainid', 'msg_header_date_year',
                      'msg_header_date_month', 'msg_msgtype',
                      'msg_header_date_day', 'msg_header_date_hour', 'msg_header_date_minute', 'msg_header_date_second',
                      'msg_header_date_msecond']
        jsonobj = jsonobjlst[0]
        cols = []
        for (key, value) in jsonobj.items():
            if not key in ignorekeys:
                cols.append(key)
        #log.debug(cols)
        records = []
        for jsonobj in jsonobjlst:
            record = []
            for (key, value) in jsonobj.items():
                if not key in ignorekeys:
                    if key == timefieldname:
                        record.append(self.parse_time(value))
                    else:
                        record.append(value)
            records.append(record)
        #log.debug(records)
        try:
            conn = self.conn_pool.getconn()
            cur = conn.cursor()
            mgr = CopyManager(conn, tablename, cols)
            mgr.copy(records)
            conn.commit()
            log.debug("========== Batch Commited")
            cur.close()
            self.conn_pool.putconn(conn)
        except Exception as exp:
            log.error('Exception at tsutil.batchinsert() %s ' % exp)
            traceback.print_exc()

    def __del__(self):
        if self.conn_pool:
            self.conn_pool.closeall
        log.debug("PostgreSQL connection pool is closed")

    def parse_time(self, txt):
        date_s,time_s = txt.split(' ')
        year_s, mon_s, day_s = date_s.split('-')
        hour_s, minute_s, second_s = time_s.split(':')
        return datetime(int(year_s), int(mon_s), int(day_s), int(hour_s), int(minute_s), int(second_s))

if __name__ == '__main__':
    tu = TSutil()
