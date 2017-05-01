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

class PositiveNonSentinelNodes(OneFieldPerReport):
    ''' find the number of positive non sentinel lymph nodes excised in the templated pathology report '''
    __version__ = 'PositiveNonSentinelNodes1.0'
    def __init__(self):
        super(PositiveNonSentinelNodes, self).__init__()
        self.field_name = 'PositiveNonSentinelNodes'
        self.regex = r'[Nn]on-(?:SLNs|sentinel nodes) with carcinoma[ :]+([\d]+)'
        self.confidence = .65
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
