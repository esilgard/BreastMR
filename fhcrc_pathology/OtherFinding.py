'''author@esilgard'''
#
# Copyright (c) 2013-2016 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from OneFieldPerReport import OneFieldPerReport
import global_strings as gb

class OtherFinding(OneFieldPerReport):
    ''' extract other, non histologic findings (necrosis, inflammation, etc) '''
    __version__ = 'OtherFinding1.0'
    def __init__(self):
        super(OtherFinding, self).__init__()       
        self.overall_field_name = 'OtherFinding'
        self.overall_table = gb.PATHOLOGY_TABLE
        self.specimen_confidence = 0.9
        ## reference lists & dictionaries ##
        self.file_name_string = 'other_findings'
        ## relevant sections of the report ##
        self.good_section = r'IMPRESSION|FINAL DIAGNOSIS|COMMENT|FINAL DX|SUMMARY CANCER'
        self.bad_section = r'CLINICAL|Note'
