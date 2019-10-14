"""
Resource Constraining and Resource Allocation
"""

import pandas
import re


class ResourceAllocation:
    # Given a file name (xlsx) extracts data necessary for calculations
    def __init__(self, file):

        # getting contents of excel file
        data = pandas.read_excel(file)

        # getting data for each column
        self.activity = data.iloc[:, 0:1]['Activity'].values
        self.duration = data.iloc[:, 1:2]['Duration'].values
        self.depends_on = data.iloc[:, 2:3]['Depends on'].values
        self.relationship = data.iloc[:, 3:4]['Relationship/lag'].values
        self.resource_req_per_day = data.iloc[:, 4:5]['Resource Requirement/day'].values
        self.state = {"es": 0, "ef": 0, "ls": 0, "duration": 0, "lf": 0}

    def utility(self, index, acitivity, state_block):

        if index == 0:
            # initializing first acitivity.
            # setting ES and LS as zero
            state_block[activity]['es'] = state_block[activity]['ls'] = 0
            state_block[acitivity]['duration'] = self.duration[index]
            state_block[activity]['ef'] = state_block[activity]['lf'] = self.duration[index]

        else:
            # if current activity is not first activity
            # calculate ES, LS , EF, LF based on relation
            if self.relationship[index] != 'nan':
                # regular expression to extract relation type, dependencies between activities
                relation_type = re.findall("[A-Z]{2}", self.relationship[index])
                relation_between_activity = re.findall("([A-Z], [A-Z])", self.relationship[index])
                relation_value = re.findall("[0-9]", self.relationship[index])


if __name__ == "__main__":

    # getting file name from user
    print("Enter file name: ", end='')
    file_name = input()

    # maintains representation states of all the activities
    states = {}

    model = ResourceAllocation(file_name)

    # creating state for all activities
    for activity in model.activity:
        states[activity] = {"es": 0, "ef": 0, "ls": 0, "duration": 0, "lf": 0}
        model.utility(model.activity.tolist().index(activity), activity, states)