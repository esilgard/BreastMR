# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:38:13 2017

@author: esilgard
"""
#
# Copyright (c) 2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class NuclearPleomorphism(OneFieldPerReport):
    ''' find the invasive nuclear pleomorphism in the templated pathology report '''
    __version__ = 'NuclearPleomorphism1.0'
    def __init__(self):
        super(NuclearPleomorphism, self).__init__()
        self.field_name = 'NuclearPleomorphism'
        self.regex = r'Nuclear Pleomorphism:[\s]+([123\-]+)[\s]+point'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
        self.good_section = r'SUMMARY CANCER|DIAGNOSIS'
