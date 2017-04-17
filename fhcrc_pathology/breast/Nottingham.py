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

class Nottingham(OneFieldPerReport):
    ''' find the Nottingham grade in the templated pathology report '''
    __version__ = 'Nottingham1.0'
    def __init__(self):
        super(Nottingham, self).__init__()
        self.field_name = 'Nottingham'
        self.regex = r'Nottingham [gG]rade:[\s]+Grade ([I]+)'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
