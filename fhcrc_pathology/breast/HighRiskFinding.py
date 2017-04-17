'''author@esilgard'''
#
# Copyright (c) 2013-2016 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerSpecimen import OneFieldPerSpecimen
import global_strings as gb

class HighRiskFinding(OneFieldPerSpecimen):
    ''' extract other, high risk findings (atypia, etc) '''
    __version__ = 'HighRiskFinding1.0'
    def __init__(self):
        super(HighRiskFinding, self).__init__()    
        self.overall_field_name = 'HighRiskFinding'
        self.overall_table = gb.PATHOLOGY_TABLE
        self.specimen_confidence = 0.9
        self.match_style = 'all'
        ## reference lists & dictionaries ##
        self.file_name_string = 'high_risk'
        ## relevant sections of the report ##
        self.good_section = r'IMPRESSION|FINAL DIAGNOSIS|COMMENT|FINAL DX|SUMMARY CANCER'
        self.bad_section = r'CLINICAL|Note'
