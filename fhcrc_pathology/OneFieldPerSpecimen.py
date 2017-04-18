''' author@esilgard'''
#
# Copyright (c) 2013-2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

import re, os
import global_strings as gb
PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep

class OneFieldPerSpecimen(object):
    '''
    extract the value of a field which has one or more values per specimen the from path text
    '''
    __version__ = 'OneFieldPerSpecimen1.0'
    pre_negation = r'( not | no |negative |previous|free of |without|against |(hx|history) of | \
                        to rule out|preclud| insufficient|suboptimal).{,75}'
    
    post_negation = r'.{,50}( unlikely| not (likely|identif)| negative)'
    ## default False flag; true means the slgorithm will infer some other value based on given input
    inference_flag = False
    ## default False secondary element; true means there's another data element that should
    ## be searched for based on either position or value of the first
    has_secondary_data_element = False
    secondary_data_elements = None
    def __init__(self):
        self.overall_field_name = 'Default'
        self.overall_table = gb.PATHOLOGY_TABLE
        self.specimen_confidence = 0.0
        self.unlabled_specimen_confidence = 0.0
        self.return_d_list = []

        ## reference lists & dictionaries ##
        self.file_name_string = 'Default'
        self.dz_specific_list = []
        self.dz_specific_standardizations = {}
        self.general_list = []
        self.general_standardizations = {}

        ## relevant sections and negations of the report ##
        self.good_section = 'Default'
        self.bad_section = 'Default'

    def get_version(self):
        ''' return algorithm version '''
        return self.__version__

    def get_dictionaries(self, reference_file_name_string):
        '''
        get data element relevant resource files
        '''
        string_list = []
        standardizations = {}
        for line in open(PATH + reference_file_name_string + '.txt', 'r').readlines():
            strings = line.split(';')
            for each in strings:
                each = each.strip().lower()
                standardizations[each] = strings[0].strip()
                string_list.append(each)
        string_list = sorted(string_list, key=lambda x: len(x), reverse=True)
        return string_list, standardizations

    ## loop through relevant sections findings PER SPECIMEN
    def get_specimen_finding(self, specimen, string_list, standardizations, d):
        ''' loop through specimens in the specimenSource to get data elements for each '''
        specimen_finding_set = set([])
        specimen_start_stops_set = set([])
        def find_string_match(text):
            ''' helper method for finding the string match instances '''
            text = text.lower()
            text = re.sub(r'[.,:;\\\/\-]', ' ', text)
            for finding in string_list:         
                if re.search(r'([\W]|^)' + '(' + finding + ')' + r'([\W]|$)', text) and \
                   not re.search(self.pre_negation + '(' + finding + ')' + r'([\W]|$)', text) and \
                   not re.search(r'([\W]|^)' + finding + self.post_negation, text):
                    ## only return character offsets for the regular path text (not SpecimenSource)
                    if line_onset:
                        start = text.find(finding) + line_onset
                        stop = start + len(finding)
                        ## only add char off sets if there is not a longer (overlapping) string
                        ## this works because the finding list is sorted by length
                        substring = False
                        for offsets in specimen_start_stops_set:
                            if start >= offsets[0] and start <= offsets[1]:
                                substring = True
                        if substring == False:
                            specimen_finding_set.add(standardizations[finding])
                            specimen_start_stops_set.add((start, stop))
                    else:
                        specimen_finding_set.add(standardizations[finding])
        for section in sorted(d):
            section_specimen = section[3]
            line_onset = section[2]
            header = section[1]
            if re.search(self.good_section, header) and not re.search(self.bad_section, header):                
                for index, results in sorted(d[section].items(), key=lambda x: int(x[0])):
                    ## this is a special case for getting info from the SpecimenSource
                    ## this is a metadata field, not in the path text itself
                    if section == (0, 'SpecimenSource', 0, None):
                        if d[section][0].get(specimen):
                            find_string_match(d[section][0].get(specimen))
                    ## meant to weed out references to literature/papers,
                    ## publication info like this: 2001;30:1-14.
                    ## these can contain confusing general statements that don't really apply
                    elif re.search(r'[\d]{4}[;,][ ]*[\d]{1,4}:[\d\-]{1,6}', results):
                        pass
                    elif specimen in section_specimen:
                        find_string_match(results)
        return specimen_finding_set, specimen_start_stops_set

    def add_secondary_data_elements(self, each_field_d, full_text):
        '''
        if current class has an inferred or secondary class (like histology:grade or metastasis
        call the secondary class and add returned data elements to return list
        '''
        for each_secondary_element in self.secondary_data_elements:
            module = __import__(each_secondary_element, globals(), locals(), [])
            field_class = getattr(module, each_secondary_element)
            instance = field_class()
            return_d = instance.get(each_field_d, full_text)
            if return_d:
                self.return_d_list.append(return_d)

    def get(self, disease_group, d):
        '''
        get values for data elements which potentially have seperate values per specimen
        aggregate values for a report level reporting as well
        '''
       
        self.dz_specific_list, self.dz_specific_standardizations = self.get_dictionaries\
                                            (disease_group + os.path.sep + self.file_name_string)
        ## general sets to track and aggregate overall findings for the report
        finding_set = set([])
        start_stops_set = set([])
       
        specimen_finding_set, specimen_start_stops_set = self.get_specimen_finding\
                    ('', self.dz_specific_list, self.dz_specific_standardizations, d)
        if specimen_finding_set:
            finding_set = finding_set.union(specimen_finding_set)
            if self.inference_flag:
                specimen_finding_set = self.infer(specimen_finding_set)
            start_stops_set = start_stops_set.union(specimen_start_stops_set)
            ## drop confidence level for multiple finds
            if len(specimen_finding_set) > 1:
                self.unlabled_specimen_confidence = self.unlabled_specimen_confidence * .8
            unk_finding_d = {gb.NAME: self.overall_field_name, gb.KEY: gb.ALL, \
                             gb.TABLE: self.overall_table, gb.VERSION: self.get_version(), \
                             gb.VALUE: ';'.join(sorted(specimen_finding_set)), gb.CONFIDENCE: \
                             ("%.2f" % self.unlabled_specimen_confidence), gb.STARTSTOPS: \
                             [{gb.START: char[0], gb.STOP:char[1]} for \
                              char in specimen_start_stops_set]}
            self.return_d_list.append(unk_finding_d)
            if self.has_secondary_data_element == True:
                self.add_secondary_data_elements(unk_finding_d, d[(-1, 'FullText', 0, None)])
        
        return (self.return_d_list, list)
