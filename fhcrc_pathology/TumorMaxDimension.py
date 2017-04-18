# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:40:47 2017

@author: esilgard
"""
#
# Copyright (c) 2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class TumorMaxDimension(OneFieldPerReport):
    ''' find the maxiumum tumor dize in the templated pathology report '''
    __version__ = 'TumorMaxDimension1.0'
    def __init__(self):
        super(TumorMaxDimension, self).__init__()
        self.field_name = 'TumorMaxDimension'
        self.regex = r'[\(]largest focus[\)]:[\s]+([\d.]+[\s]?[cm]m)'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
