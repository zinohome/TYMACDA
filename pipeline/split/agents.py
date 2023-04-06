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
import re
import simplejson as json
import pandas as pd
from app import app
from codec.nb5 import Nb5
from core.settings import settings
from pipeline.split.models import input_topic, output_topic
from utils.log import log as log

@app.agent(input_topic)
async def split_signal(stream):
    async for data in stream:
        log.debug("-------------------- Get binary file data --------------------")
        asciistr = binascii.b2a_hex(data).decode()
        asciidatalist = asciistr.split('00000000000000000201')
        cdatalist = []
        count = 0
        for astr in asciidatalist:
            count += 1
            if count == 1:
                astr = astr.removesuffix('000000')
                cdatalist.append(astr)
            else:
                astr = f"0201{astr}".removesuffix('000000')
                cdatalist.append(astr)
        for cstr in cdatalist:
            clen = len(cstr)
            if clen > 200:
                if clen // 454 > 0:
                    text_arr = re.findall(r'.{%d}' % int(454), cstr)
                    for text in text_arr:
                        #log.debug(len(binascii.a2b_hex(text)))
                        await output_topic.send(value=binascii.a2b_hex(text))
            else:
                #log.debug(len(binascii.a2b_hex(cstr)))
                await output_topic.send(value=binascii.a2b_hex(cstr))
