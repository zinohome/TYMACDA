#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: MACDA

from app import app
from core.settings import settings
from pipeline.statisreport.models import input_topic
from utils.alertutil import Alertutil
from utils.log import log as log
from utils.tsutil import TSutil
import time


@app.timer(interval=settings.SEND_STATS_INTERVAL)
async def on_started():
    coachdict = {'1':'Tc1','2':'Mp1','3':'M1','4':'M2','5':'Mp2','6':'Tc2',}
    log.debug("==========********** Get Statistic report data batch ==========**********")
    tu = TSutil()
    au = Alertutil()
    dev_mode = settings.DEV_MODE
    if dev_mode:
        statis_data = tu.get_statis_data('dev')
    else:
        statis_data = tu.get_statis_data('pro')
    # Generata statis data
    statis_data_list = []
    if statis_data['len'] > 0:
        for item in statis_data['data']:
            dvc_no = item['msg_calc_dvc_no']
            dvc_no_list = [i for i in dvc_no.split('0') if i != '']
            if len(dvc_no_list) == 3:
                line_no = dvc_no_list[0]
                train_no = dvc_no_list[1]
                carbin_no = dvc_no_list[2]
                trainNo = f"0{line_no}0{str(train_no).zfill(2)}"
                partCodepre = f"0{line_no}0{str(int(carbin_no) - 1).zfill(2)}"
                # log.debug('line_no: %s, train_no: %s, carbin_no: %s' % (line_no, train_no, carbin_no))
                for code in au.partcodefield:
                    sdata = {}
                    sdata['lineName'] = str(line_no)
                    sdata['trainType'] = 'B2'
                    sdata['trainNo'] = trainNo
                    sdata['partCode'] = str(au.getvalue('partcode', code, 'part_code')).replace('500', partCodepre)
                    if 'rad' in code or 'fad' in code:
                        sdata['serviceTime'] = 0
                        sdata['serviceValue'] = item[f"dvc_{code}"]
                    else:
                        sdata['serviceTime'] = item[f"dvc_{code}"]
                        sdata['serviceValue'] = 0
                    sdata['mileage'] = 0
                    statis_data_list.append(sdata)
    #log.debug('statis_data_list is : %s' % statis_data_list)
    au.send_statistics(statis_data_list)
