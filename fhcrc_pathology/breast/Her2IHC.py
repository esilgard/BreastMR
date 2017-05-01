# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:53:43 2017

@author: esilgard
"""
#
# Copyright (c) 2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class Her2IHC(OneFieldPerReport):
    ''' find the Her2-neu IHC results in the templated pathology report '''
    __version__ = 'Her2IHC1.0'
    def __init__(self):
        super(Her2IHC, self).__init__()
        self.field_name = 'Her2IHC'
        self.regex = r'neu[\)]? by IHC:[\s]+([PNE][ositivegativequivocal]{6,})'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
        self.good_section = r'SUMMARY CANCER|DIAGNOSIS'
