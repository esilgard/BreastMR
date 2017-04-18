# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:06:54 2017

@author: esilgard
"""
#
# Copyright (c) 2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class ER(OneFieldPerReport):
    ''' find the Estrogen Receptor results in the templated pathology report '''
    __version__ = 'ER1.0'
    def __init__(self):
        super(ER, self).__init__()
        self.field_name = 'ER'
        self.regex = r'Estrogen receptor:[\s]+([PNE][ositivegativequivocal]+)'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
        self.good_section = r'SUMMARY CANCER|DIAGNOSIS'
