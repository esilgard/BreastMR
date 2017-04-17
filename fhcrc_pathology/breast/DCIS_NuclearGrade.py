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

class DCIS_NuclearGrade(OneFieldPerReport):
    ''' find the invasive nuclear pleomorphism in the templated pathology report '''
    __version__ = 'DCIS_NuclearGrade1.0'
    def __init__(self):
        super(DCIS_NuclearGrade, self).__init__()
        self.field_name = 'DCIS_NuclearGrade'
        self.regex = r'Nuclear grade of DCIS:[\s]+([A-Za-z]+)'
        self.confidence = .65
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
