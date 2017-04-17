'''author@esilgard'''
#
# Copyright (c) 2013-2016 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from fhcrc_pathology.OneFieldPerSpecimen import OneFieldPerSpecimen
import global_strings as gb

class MalignantFinding(OneFieldPerSpecimen):
    ''' extract histologic findings'''
    __version__ = 'OtherFinding1.0'
    def __init__(self):
        super(MalignantFinding, self).__init__()       
        self.overall_field_name = 'MalignantFinding'
        self.overall_table = gb.PATHOLOGY_TABLE
        self.specimen_confidence = 0.9
        self.match_style = 'all'
        ## reference lists & dictionaries ##
        self.file_name_string = 'malignant'
        ## relevant sections of the report ##
        self.good_section = r'IMPRESSION|FINAL DIAGNOSIS|COMMENT|FINAL DX|SUMMARY CANCER'
        self.bad_section = r'CLINICAL|Note'
        ## there is a secondary data element that should be searched for
        ## based on either position or value of the first e.g. PathGrade
        self.has_secondary_data_element = True
        self.secondary_data_elements = ['PathGrade']