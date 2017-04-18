'''author@esilgard'''
#
# Copyright (c) 2013-2017 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from . import global_strings as gb
__version__ = 'final_pathology_logic1.0'

def get(table_list):
    '''
    use all the extracted pathology elements from a given report to apply final logic
    add/delete values for the final output
    table_list = list of table dictionaries where
    table dictionary: tableName and a dictionary
    '''
    return_list = []
    overall_findings = {'BenignFinding':(1,'Benign'),'HighRiskFinding':(2,'High Risk'),'MalignantFinding':(3,'Malignant')}
    max_index = None
    max_overall = None
    chars = None
    conf = None
    ## iterate through the tables
    for table in table_list:
        field_list = []
        
        ## iterate Pathology values, collapse specimen (recordKey) data
        for fields in table[gb.FIELDS]:  
            if fields[gb.VALUE] and fields not in field_list:
                # for Breast MR audit only - collapse multiple sites into just "breast"
                if fields[gb.NAME] == 'PathSite' and \
                    len(fields[gb.VALUE].split(';')) > 3:
                        fields[gb.VALUE] = 'Breast'
                field_list.append(fields)
                if fields[gb.NAME] in overall_findings:
                    index = overall_findings[fields[gb.NAME]][0]
                    if index > max_index:
                        max_index = overall_findings[fields[gb.NAME]][0]
                        chars = fields[gb.STARTSTOPS]
                        conf = fields[gb.CONFIDENCE]
                        max_overall = overall_findings[fields[gb.NAME]][1]
        # make overall findings align with the worst set of findings
        if max_index:
            field_list.append(
                {gb.NAME: 'OverallFinding', gb.KEY: gb.ALL, \
                 gb.TABLE: 'Pathology', gb.VERSION: 'OverallFinding1.0', \
                 gb.VALUE: max_overall, \
                 gb.STARTSTOPS: chars, gb.CONFIDENCE: conf})
        else:
            ## there were no findings - label the report benign
            field_list.append(
                {gb.NAME: 'OverallFinding', gb.KEY: gb.ALL, \
                 gb.TABLE: 'Pathology', gb.VERSION: 'OverallFinding1.0', \
                 gb.VALUE: 'Benign', \
                 gb.STARTSTOPS: [], gb.CONFIDENCE: '.60'})
        if field_list:
            ## don't return a table that doesn't have any field value
            table[gb.FIELDS] = field_list
            return_list.append(table)
    return return_list
