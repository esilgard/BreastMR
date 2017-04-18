# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:14:47 2017

@author: esilgard
"""
#
# Copyright (c) 2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class Ki67(OneFieldPerReport):
    ''' find the Ki67 score in the templated pathology report '''
    __version__ = 'Ki671.0'
    def __init__(self):
        super(Ki67, self).__init__()
        self.field_name = 'Ki67'
        self.regex = r'Ki-67 proliferative index:[\s]+([\d ]+[%])'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
        self.good_section = r'SUMMARY CANCER|DIAGNOSIS'
