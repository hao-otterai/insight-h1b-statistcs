import sys
import logging

from csv import reader
from collections import Counter


def getFieldIdx(fields):
    """
    This function takes field names from the 1st line of table as input,
    and return a dictionary of indices for the specific field names listed in FIELDKEYS.
    In case the field names vary across different years, alternative field names listed in
    FIELDKEYS_ALTER are also checked.

    input: 
        fields - field names from the 1st line of the csv table
    output: 
        fIdx - a dictionary of index values for the field names specified in FIELDKEYS.
    """

    FIELDKEYS = ['SOC_NAME', 'SOC_CODE', 'WORKSITE_STATE', 'CASE_STATUS', ]  # 'VISA_CLASS']
    FIELDKEYS_ALTER = {
        'SOC_NAME': ['LCA_CASE_SOC_NAME', 'OCCUPATIONAL_TITLE', ],
        'SOC_CODE': ['LCA_CASE_SOC_CODE', 'JOB_CODE', ],
        'WORKSITE_STATE': ['LCA_CASE_WORKLOC1_STATE', 'STATE_1', 'WORK_LOCATION_STATE1'],
        'CASE_STATUS': ['STATUS', 'APPROVAL_STATUS', ],
        #'VISA_CLASS': [],
    }

    fIdx = dict()
    for key0 in FIELDKEYS:
        try:
            key = key0
            if key0 not in fields:
                for key2 in FIELDKEYS_ALTER[key]:
                    if key2 in fields:
                        key = key2
                        break
            fIdx[key0] = fields.index(key)
        except ValueError as e:
            logging.warning(e)
            return

    return fIdx


def read_csv(filename):
    """
    read_csv takes the filename directory of a ";" delimited .csv file as input,
    and outputs the Counter for occupations and state, as well as the total number
    of certified cases. 
    - input
    filename: filename directory of a ";" delimited .csv file
    - output
    'occupNameLookup': a dictionary consisting of a counter of soc_names for each soc_code  
        'occupCounter': counter of soc_code of all certified cases. 
        'stateCounter': counter of state of all certified cases. 
        'numCertified': total number of certified cases.
    """
    occupNameLookup = dict()
    occupCounter = Counter()
    stateCounter = Counter()
    numCertified = 0

    with open(filename, encoding='utf-8') as csvfile:
        lineNum = 0
    # iterate over the csvfile by line, get fileds delimited by ";"
        for fields in reader(csvfile, delimiter=';'):
            if lineNum == 0:
                # for the first line, get all field names and indices of
                # particular fields of interest, as defined in getFieldIdx()
                numFields = len(fields)
                fIdx = getFieldIdx(fields)

            else:
                # skip lines with missing values
                if len(fields) != numFields:
                    continue

        # may need to check visa class
                #visa_class = fields[fIdx['VISA_CLASS']].strip().upper()
                # if not ('H-1B' in visa_class or 'E-3' in visa_class):
                #    continue

        # if case status is not certified, continue to next line.
                if fields[fIdx['CASE_STATUS']].strip().replace(' ', '').upper() != 'CERTIFIED':
                    continue

        # find the soc_code (xx-xxxx), there are potentially formatting issues, like missing '-'
        # in the soc_code, or '.', '/' were used instead of '-'
                soc_code = fields[fIdx['SOC_CODE']].strip().upper()
                try:
                    if soc_code[2] == '.' or soc_code[2] == '/':
                        soc_code = soc_code[:2] + '-' + soc_code[3:]
                    elif '-' not in soc_code:
                        soc_code = soc_code[:2] + '-' + soc_code[2:]
                except IndexError as e:
                    continue

        # soc_name is problematic, as there can be slightly different soc names meant for the same
        # soc_code, for example, product manager vs product managers.
        # The following code counts the different soc_names for the same soc_code, and the result
        # is saved as a dictionary of Counter() in occupNameLookup for later use.
                soc_name = fields[fIdx['SOC_NAME']].strip().upper().replace('*', '')
                if soc_code not in occupCounter:
                    occupNameLookup[soc_code] = Counter()
                occupNameLookup[soc_code][soc_name] += 1
                occupCounter[soc_code] += 1

        # count the state
                stateCounter[fields[fIdx['WORKSITE_STATE']].strip().upper()] += 1

                numCertified += 1

            lineNum += 1

        return {
            'occupNameLookup': occupNameLookup,
            'occupCounter': occupCounter,
            'stateCounter': stateCounter,
            'numCertified': numCertified,
        }


def get_top_state(data, top_k, output_dir):
    """
    calculate the top K state, and output result to file.
    states are sorted first by counts, then by state name if there are ties
    """
    state_top_k = data['stateCounter'].most_common(top_k)
    state_top_k.sort(key=lambda x: (-x[1], x[0]), reverse=False)
    state_top_k = dict(state_top_k)

    # output top states to output_dir
    with open(output_dir, 'w') as f:
        f.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        for state in state_top_k:
            f.write(str(state) + ';' + str(state_top_k[state]) + ';' + str(round(state_top_k[state] * 100 / data['numCertified'], 1)) + '%\n')


def get_top_occup(data, top_k, output_dir):
    """
    calculate the top K occupation name, and output result to file.
    occupations are sorted first by counts, then by name if there are ties
    """
    occup_top_k = dict()
    for soc_code, count in data['occupCounter'].most_common(top_k):
        # remember that each soc_code may have multiple soc_name variations,
        # here the soc_name with the highest count is selected as the name of the corresponding soc_code
        soc_name = max(data['occupNameLookup'][soc_code], key=data['occupNameLookup'][soc_code].get)
        occup_top_k[soc_name] = count

    occup_top_k = dict(sorted(occup_top_k.items(), key=lambda x: (-x[1], x[0]), reverse=False))

    # output top occupations to output_dir
    with open(output_dir, 'w') as f:
        f.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        for occup in occup_top_k:
            f.write(str(occup) + ';' + str(occup_top_k[occup]) + ';' + str(round(occup_top_k[occup] * 100 / data['numCertified'], 1)) + '%\n')


if __name__ == '__main__':

    # get the input
    input_file = sys.argv[1]
    output2file_occup = sys.argv[2]
    output2file_state = sys.argv[3]

    # read the input
    data = read_csv(input_file)

    # calculate top occupantion and output to file
    get_top_occup(data, 10, output2file_occup)

    # calculate top states and output to file
    get_top_state(data, 10, output2file_state)
