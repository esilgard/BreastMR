# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:43:08 2017

@author: esilgard
"""

#
# Copyright (c) 2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class PositiveSentinelNodes(OneFieldPerReport):
    ''' find the number of positive sentinel lymph nodes excised in the templated pathology report '''
    __version__ = 'PositiveSentinelNodes1.0'
    def __init__(self):
        super(PositiveSentinelNodes, self).__init__()
        self.field_name = 'PositiveSentinelNodes'
        self.regex = r'[SNLsetil nod]+ with carcinoma[ :]+([\d]+)'
        self.confidence = .65
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
