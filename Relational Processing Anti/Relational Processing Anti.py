import pandas as pd
import os
import random

# Direct to project file
os.getcwd()
os.chdir('./Relational Processing Anti')

# Create general stimulus pool
AllStimuli = pd.read_excel('AllStimuli.xlsx')
# Concatenate all columns from AllStimuli into one united column
stimList = []
for iter in range(len(AllStimuli.columns)):
    currentList = AllStimuli.iloc[:, iter].tolist()
    stimList = stimList + currentList

df_stimList = pd.DataFrame(stimList)


# ======================================================================================================================
# Create 200 trials for easy - all stimuli in consecutive trial allowed - max 2 diff. stim
# ======================================================================================================================
# Create empty trials easy df
trials_easy = pd.DataFrame(index = range(240), columns = range(37))

# Fill all rows for the first 100 and second 100 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):
        # Allocate list for the stimuli presented in one trial
        stimList = []
        # first stim is sampled
        firstStim = df_stimList.sample()
        # Append first stim to list of 3 stimuli in total for one trial
        stimList.append(firstStim)

        # sample the one other stim type
        for i in range(1):

            stimFound = False
            while stimFound == False:
                otherStim = df_stimList.sample()
                # compare new sampled stim with firstStim
                if otherStim.iloc[0,0] != firstStim.iloc[0,0]:
                    # append
                    stimList.append(otherStim)
                    stimFound = True
                else:
                    stimFound = False

        # Append list with all other stimuli according to the previous drawn ones in a randomly drawn ratio
        ratio_list = [[1]]
        ratio = random.sample(ratio_list,1)
        ratio[0][0]

        for i in range(ratio[0][0]):
            stimList.append(stimList[1])

        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],3)
            fieldList = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 3)
            fieldList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

        # Check that each stimulus position is at least one field away from each other
        noChange = False
        while noChange == False:
            countNoChange = 0
            for l in range(len(fieldNumberList)):
                if abs(fieldNumberList[0]-fieldNumberList[l]) <= 2 and l != 0 or abs(fieldNumberList[0] - fieldNumberList[l]) >= 30:
                     fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[1]-fieldNumberList[l]) <= 2 and l != 1 or abs(fieldNumberList[1] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[2] - fieldNumberList[l]) <= 2 and l != 2 or abs(fieldNumberList[2] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 9:
                noChange = True

        # Assign every stim to its field according to the sampled random numbers in fieldNumberList
        for i in range(len(stimList)):
            trials_easy.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0,0]
        # Save correct answer to real df
        trials_easy.loc[i, 36] = stimList[1].iloc[0, 0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_easy.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_easy.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_easy.iloc[i, 34] = 6
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_easy.iloc[i, 35] = 1
        else:
            trials_easy.iloc[i, 35] = 0

# Save df as spreadsheet
trials_easy.to_excel('spreadsheetEasy_RelationalProcessing_Anti.xlsx')


# ======================================================================================================================
# Create 200 trials for normal - Only similiar colors in consecutive trials - max 3 diff. stim
# ======================================================================================================================
# Create empty trials normal df
trials_normal = pd.DataFrame(index = range(240), columns = range(37))

def assignFunc_color(color1, color2):

    if splitted_otherStim_Color == color1 or splitted_otherStim_Color == color2:
        # append
        stimList.append(otherStim)
        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

# Create dictionary for colors with their similar connections
colorDict = {
    '360_0': '337_5-22_5',
    '337_5': '292_5-360_0',
    '292_5': '225_0-337_5',
    '225_0': '180_0-292_5',
    '180_0': '135_0-225_0',
    '135_0': '67_5-180_0',
    '67_5': '22_5-135_0',
    '22_5': '360_0-67_5'
}

# Fill all rows for the first 100 and second 100 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):
        # Allocate list for the stimuli presented in one trial
        stimList = []
        # first stim is sampled
        firstStim = df_stimList.sample()
        # Split new sampled stim for comparison
        splitted_firstStim_Color = firstStim.iloc[0,0].split('w')[0]
        # colors to look for w.r.t. first Stim
        outfirstStim_Color_colorDict = colorDict[splitted_firstStim_Color]
        [c1, c2] = outfirstStim_Color_colorDict.split('-')
        # Append first stim to list of 8 stimuli in total for one trial
        stimList.append(firstStim)

        # sample the two other stim types
        for i in range(2):

            stimFound = False
            while stimFound == False:
                otherStim = df_stimList.sample()
                # Split new sampled stim for comparison
                splitted_otherStim_Color = otherStim.iloc[0,0].split('w')[0]

                # compare new sampled stim with firstStim
                if otherStim.iloc[0,0] != firstStim.iloc[0,0]:
                    # Apply function for comparison of otherStim_Color with firstStim_Color's
                    stimFound = assignFunc_color(c1, c2)
                else:
                    stimFound = False

        # Append list with all other stimuli according to the previous drawn ones in a randomly drawn ratio
        ratio_list = [[0, 2]]
        ratio = random.sample(ratio_list, 1)

        for i in range(ratio[0][0]):
            stimList.append(stimList[1])

        for i in range(ratio[0][1]):
            stimList.append(stimList[2])

        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], 5)
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 5)
            fieldList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

        # Check that each stimulus position is at least one field away from each other
        noChange = False
        while noChange == False:
            countNoChange = 0
            for l in range(len(fieldNumberList)):
                if abs(fieldNumberList[0] - fieldNumberList[l]) <= 2 and l != 0 or abs(fieldNumberList[0] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[1] - fieldNumberList[l]) <= 2 and l != 1 or abs(fieldNumberList[1] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[2] - fieldNumberList[l]) <= 2 and l != 2 or abs(fieldNumberList[2] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[3] - fieldNumberList[l]) <= 2 and l != 3 or abs(fieldNumberList[3] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[4] - fieldNumberList[l]) <= 2 and l != 4 or abs(fieldNumberList[4] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 25:
                noChange = True

        # Assign every stim to its field according to the sampled random numbers in fieldNumberList
        for i in range(len(stimList)):
            trials_normal.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0,0]
        # Save correct answer to real df
        trials_normal.loc[i, 36] = stimList[2].iloc[0, 0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_normal.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_normal.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_normal.iloc[i, 34] = 6
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_normal.iloc[i, 35] = 1
        else:
            trials_normal.iloc[i, 35] = 0

# Save df as spreadsheet
trials_normal.to_excel('spreadsheetNormal_RelationalProcessing_Anti.xlsx')


# ======================================================================================================================
# Create 100 trials for hard - Only similiar colors and forms in consecutive trials (40 available Stimuli) - max 4 diff. stim
# ======================================================================================================================
# Create empty trials normal df
trials_hard = pd.DataFrame(index = range(240), columns = range(37))

# Create dictionary for forms with their similar connections
formDict = {
    '0_25': '0_50-0_75',
    '0_50': '0_25-0_75',
    '0_75': '0_50-1_0',
    '1_0': '0_50-0_75'
}

def assignFunc_form(form1, form2):
    if splitted_otherStim_Form == form1 or splitted_otherStim_Form == form2:
        # append
        stimList.append(otherStim)
        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

def assignFunc_color(color1, color2, form1, form2):

    if splitted_otherStim_Color == color1 or splitted_otherStim_Color == color2:

        stimFound = assignFunc_form(form1, form2)
        return stimFound

    else:
        stimFound = False
        return stimFound

for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):
        # Allocate list for the stimuli presented in one trial
        stimList = []
        # first stim is sampled
        firstStim = df_stimList.sample()
        # Split new sampled stim for comparison
        splitted_firstStim_Color = firstStim.iloc[0,0].split('w')[0]
        splitted_firstStim_Form = firstStim.iloc[0,0].split('w')[1].split('.')[0]
        # colors to look for w.r.t. first Stim
        outfirstStim_Color_colorDict = colorDict[splitted_firstStim_Color]
        [c1, c2] = outfirstStim_Color_colorDict.split('-')
        # forms to look for w.r.t. first Stim
        outfirstStim_Form_formDict = formDict[splitted_firstStim_Form]
        [f1, f2] = outfirstStim_Form_formDict.split('-')
        # Append first stim to list of 8 stimuli in total for one trial
        stimList.append(firstStim)

        # sample the possible four other stim types
        for i in range(3):

            stimFound = False
            while stimFound == False:
                otherStim = df_stimList.sample()
                # Split new sampled stim for comparison
                splitted_otherStim_Color = otherStim.iloc[0,0].split('w')[0]
                splitted_otherStim_Form = otherStim.iloc[0, 0].split('w')[1].split('.')[0]

                # compare new sampled stim with firstStim
                if otherStim.iloc[0,0] != firstStim.iloc[0,0]:
                    # Apply function for comparison of otherStim_Color with firstStim_Color's
                    stimFound = assignFunc_color(c1, c2, f1, f2)
                else:
                    stimFound = False

        # Append list with all other stimuli according to the previous drawn ones in a randomly drawn ratio
        ratio_list = [[0, 0, 3]]
        ratio = random.sample(ratio_list, 1)

        for i in range(ratio[0][0]):
            stimList.append(stimList[1])

        for i in range(ratio[0][1]):
            stimList.append(stimList[2])

        for i in range(ratio[0][2]):
            stimList.append(stimList[3])

        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], 7)
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 7)
            fieldList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

        # Check that each stimulus position is at least one field away from each other
        noChange = False
        while noChange == False:
            countNoChange = 0
            for l in range(len(fieldNumberList)):
                if abs(fieldNumberList[0] - fieldNumberList[l]) <= 2 and l != 0 or abs(fieldNumberList[0] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[1] - fieldNumberList[l]) <= 2 and l != 1 or abs(fieldNumberList[1] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[2] - fieldNumberList[l]) <= 2 and l != 2 or abs(fieldNumberList[2] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[3] - fieldNumberList[l]) <= 2 and l != 3 or abs(fieldNumberList[3] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[4] - fieldNumberList[l]) <= 2 and l != 4 or abs(fieldNumberList[4] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[5] - fieldNumberList[l]) <= 2 and l != 5 or abs(fieldNumberList[5] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[6] - fieldNumberList[l]) <= 2 and l != 6 or abs(fieldNumberList[6] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 49:
                noChange = True

        # Assign every stim to its field according to the sampled random numbers in fieldNumberList
        for i in range(len(stimList)):
            trials_hard.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0,0]
        # Save correct answer to real df
        trials_hard.loc[i, 36] = stimList[3].iloc[0, 0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_hard.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_hard.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_hard.iloc[i, 34] = 6
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_hard.iloc[i, 35] = 1
        else:
            trials_hard.iloc[i, 35] = 0

# Save df as spreadsheet
trials_hard.to_excel('spreadsheetHard_RelationalProcessing_Anti.xlsx')

