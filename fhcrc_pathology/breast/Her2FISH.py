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

class Her2FISH(OneFieldPerReport):
    ''' find the Her2-neu FISH results in the templated pathology report '''
    __version__ = 'Her2FISH1.0'
    def __init__(self):
        super(Her2FISH, self).__init__()
        self.field_name = 'Her2FISH'
        self.regex = r'Her-2/neu by FISH:[\s]([A-Za-z\/]+)'
        self.confidence = .75
        self.match_style = 'first'
        self.table = gb.PATHOLOGY_TABLE
        self.value_type = 'match'
