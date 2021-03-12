#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 04:54:46 2021

@author: supremegoldenmm
"""
from liveodds.racing import Racing
from utils.utils import get_date
from datetime import datetime

racing = Racing()
date_list = racing.dates()
meetings_list = racing.meetings(date_list[0], 'AUS')
time_list = meetings_list[1].times()
race_list = meetings_list[1].races()

print (race_list[0].odds())