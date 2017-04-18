'''author@esilgard'''
#
# Copyright (c) 2013-2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

from OneFieldPerSpecimen import OneFieldPerSpecimen
import global_strings as gb

class PathFindingSide(OneFieldPerSpecimen):
    ''' extract the laterality (side) of each specimen finding specifically '''
    __version__ = 'PathFindingSide1.0'

    def __init__(self):
        super(PathFindingSide, self).__init__()
        self.overall_field_name = 'PathFindingSide'
        self.overall_table = gb.PATHOLOGY_TABLE
        self.specimen_confidence = 0.77
        self.unlabled_specimen_confidence = 0.7
        ## reference lists & dictionaries ##
        self.file_name_string = 'sides'
        ## relevant sections of the report ##
        self.good_section = r'IMPRESSION|DIAGNOSIS|DX'
        self.bad_section = r'CLINICAL|Note|SPECIMEN|Specimen|DESCRIPTION|DESC|GROSS'
        ## ability to infer new value from one or more existing ones
        self.inference_flag = True
        self.pre_negation = r'(  near|above|below| from).{,75}'

    def infer(self, finding_set):
        ''' infer 'bilateral' if the finding set is specifically only 'right' and 'left' '''
        if finding_set == set(['Right', 'Left']):
            finding_set = set(['Bilateral'])
        return finding_set
