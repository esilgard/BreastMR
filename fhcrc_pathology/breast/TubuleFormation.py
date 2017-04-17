# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:39:47 2017

@author: esilgard
"""
#
# Copyright (c) 2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class TubuleFormation(OneFieldPerReport):
    ''' find the invasive nuclear pleomorphism in the templated pathology report '''
    __version__ = 'TubuleFormation1.0'
    def __init__(self):
        super(TubuleFormation, self).__init__()
        self.field_name = 'TubuleFormation'
        self.regex = r'Tubule Formation:[\s]+([123\-]+)[\s]+point'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
