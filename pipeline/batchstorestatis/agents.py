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
from pipeline.batchstorestatis.models import input_topic
from utils.log import log as log
from utils.sensorpolyfit import SensorPolyfit
from utils.tsutil import TSutil


@app.agent(input_topic)
async def store_signal(stream):
    tu = TSutil()
    sp = SensorPolyfit()
    async for datas in stream.take(settings.TSDB_BATCH, within=settings.TSDB_BATCH_TIME):
        log.debug("==================== Get parsed data batch ====================")
        dev_mode = settings.DEV_MODE
        tu.batchinsert('statis_macda', 'msg_calc_dvc_time', datas)
        log.debug("Saved data with batch length: %s" % len(datas))
