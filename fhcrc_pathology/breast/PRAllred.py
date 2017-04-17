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

class PRAllred(OneFieldPerReport):
    ''' find the Progesterone Allred score in the templated pathology report '''
    __version__ = 'PRAllred1.0'
    def __init__(self):
        super(PRAllred, self).__init__()
        self.field_name = 'PRAllred'
        self.regex = r'Progesterone receptor:[\s\A-Za-z]+[\(]Allred score = ([\d]) of 8[\)]'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
