#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2021 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2021
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: MACDA
import binascii
import simplejson as json
from app import app
from codec.ty2statis import Ty2statis
from codec.ty2status import Ty2status
from core.settings import settings
from pipeline.batchparse.models import input_topic, output_topic
from utils.log import log as log

@app.agent(input_topic)
async def parse_signal(stream):
    async for datas in stream.take(settings.TSDB_PARSE_BATCH, within=settings.TSDB_PARSE_BATCH_TIME):
        log.debug("-------------------- Batch Get binary data --------------------")
        for data in datas:
            dev_mode = settings.DEV_MODE
            if len(data) > 200:
                log.debug('========******** Parse Statis singnal ********========')
                parsed_dict = Ty2statis.from_bytes_to_dict(data)
                log.debug(parsed_dict)
            else:
                log.debug('--------******** Parse Status singnal ********--------')
                log.debug(data)
                log.debug(len(data))
                parsed_dict = Ty2status.from_bytes_to_dict(data)
                log.debug(parsed_dict)




