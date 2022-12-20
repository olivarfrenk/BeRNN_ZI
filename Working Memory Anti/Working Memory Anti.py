import pandas as pd
import os
import random

# Direct to project file
os.getcwd()
os.chdir('./Working Memory Anti')


# ======================================================================================================================
# todo Twin memory task
# ======================================================================================================================
# Create general stimulus pool
AllStimuli = pd.read_excel('AllStimuli.xlsx')
# Concatenate all columns from AllStimuli into one united column
stimList = []
for iter in range(len(AllStimuli.columns)):
    currentList = AllStimuli.iloc[:, iter].tolist()
    stimList = stimList + currentList

df_stimList = pd.DataFrame(stimList)


# ======================================================================================================================
# Create 240 trials for easy - all stimuli in consecutive trial allowed (32 available Stimuli)
# ======================================================================================================================
trials_easy = pd.DataFrame(index = range(240), columns = range(37))
trials_easy_preDF = pd.DataFrame(index = range(240), columns = range(2))

# Put in the 180_0w1_0.png beginnings and ends for being able two shuffle the paired trials:
trials_easy_preDF.loc[0,0] = '180_0w1_0.png'
trials_easy_preDF.loc[60,0] = '180_0w1_0.png'
trials_easy_preDF.loc[120,0] = '180_0w1_0.png'
trials_easy_preDF.loc[180,0] = '180_0w1_0.png'
trials_easy_preDF.loc[240,0] = '180_0w1_0.png'

# Fill all rows for the first 120 and second 120 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for i in range(rangeList[0],rangeList[1]):
        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], 2)
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 2)
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

                if abs(fieldNumberList[1] - fieldNumberList[l]) <= 2 and l != 1 or abs(fieldNumberList[0] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 4:
                noChange = True

        # Add first stim to real df
        trials_easy.loc[i, fieldNumberList[0]] = trials_easy_preDF.loc[i,0]

        # randomly choose a stim from general stimulus pool
        stimFound = False
        while stimFound == False:
            currentStim = df_stimList.sample()
            if currentStim.iloc[0,0] != trials_easy_preDF.loc[i,0]:
                # add stim to trial df
                if pd.isna(trials_easy_preDF.loc[i,1]):
                    trials_easy.loc[i,fieldNumberList[1]] = currentStim.iloc[0,0]
                    trials_easy_preDF.loc[i,1] = currentStim.iloc[0,0]
                # check for consecutive trial
                if i != len(trials_easy_preDF)-1:
                    if pd.isna(trials_easy_preDF.loc[i+1,0]):
                        # trials_easy.loc[i+1,fieldNumberList[0]] = currentStim.iloc[0,0]
                        trials_easy_preDF.loc[i+1,0] = currentStim.iloc[0,0]
                    else:
                        trials_easy.loc[i,fieldNumberList[1]] = '180_0w1_0.png'
                        trials_easy_preDF.loc[i,1] = '180_0w1_0.png'
                # Save correct answer to real df
                trials_easy.loc[i, 36] = trials_easy_preDF.loc[i,1]
                stimFound = True
            else:
                stimFound = False

            # Add random fixation cross time
            fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
            trials_easy.iloc[i, 32] = fixation_cross_time[0]
            # Add random after response time
            after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
            trials_easy.iloc[i, 33] = after_response_time[0]
            # Add Block Randomization
            trials_easy.iloc[i, 34] = 10
            # Add Block Division
            if i == 59 or i == 119 or i == 179 or i == 239:
                trials_easy.iloc[i, 35] = 1
            else:
                trials_easy.iloc[i, 35] = 0

# Save df as spreadsheet
trials_easy.to_excel('spreadsheetEasy_WorkingMemory_Anti.xlsx')


# ======================================================================================================================
# Create 240 trials for normal - Only similiar colors in consecutive trials (32 available Stimuli)
# ======================================================================================================================
trials_normal = pd.DataFrame(index = range(240), columns = range(37))
trials_normal_preDF = pd.DataFrame(index = range(240), columns = range(2))

def assignFunc_color(color1, color2, color3):

    if splitted_currentStim_color == color1 or splitted_currentStim_color == color2 and splitted_previousStim_form != splitted_currentStim_form \
            or splitted_currentStim_color == color3:
        # append
        trials_normal.loc[i, fieldNumberList[1]] = currentStim.iloc[0, 0]
        trials_normal_preDF.loc[i, 1] = currentStim.iloc[0, 0]

        if i != len(trials_normal) - 1:
            if pd.isna(trials_normal_preDF.loc[i + 1, 0]):
                trials_normal_preDF.loc[i + 1, 0] = currentStim.iloc[0, 0]
            else:
                trials_normal.loc[i, fieldNumberList[1]] = '180_0w1_0.png'
                trials_normal_preDF.loc[i, 1] = '180_0w1_0.png'

        # Save correct answer to real df
        trials_normal.loc[i, 36] = trials_normal_preDF.loc[i, 1]
        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

# Create dictionary for colors with their similar connections
colorDict = {
    '360_0': '337_5-360_5-22_5',
    '337_5': '292_5-337_5-360_0',
    '292_5': '225_0-292_5-337_5',
    '225_0': '180_0-225_0-292_5',
    '180_0': '135_0-180_0-225_0',
    '135_0': '67_5-135_0-180_0',
    '67_5': '22_5-67_5-135_0',
    '22_5': '360_0-22_5-67_5'
}

# Put in the 180_0w1_0.png beginnings and ends for being able two shuffle the paired trials:
trials_normal_preDF.loc[0,0] = '180_0w1_0.png'
trials_normal_preDF.loc[60,0] = '180_0w1_0.png'
trials_normal_preDF.loc[120,0] = '180_0w1_0.png'
trials_normal_preDF.loc[180,0] = '180_0w1_0.png'
trials_normal_preDF.loc[240,0] = '180_0w1_0.png'

# Allocate first previous stim
previousStim = '180_0w1_0.png'
# split it up for comparison
splitted_previousStim_color = previousStim.split('w')[0]
splitted_previousStim_form = previousStim.split('w')[1].split('.')[0]

# Fill all rows for the first 100 and second 100 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for i in range(rangeList[0],rangeList[1]):
        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], 2)
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 2)
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

                if abs(fieldNumberList[1] - fieldNumberList[l]) <= 2 and l != 1 or abs(fieldNumberList[0] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 4:
                noChange = True

        # Add first stim to real df
        trials_normal.loc[i, fieldNumberList[0]] = trials_normal_preDF.loc[i, 0]

        # colors to look for w.r.t. first Stim
        previousStim_color_colorDict = colorDict[splitted_previousStim_color]
        [c1, c2, c3] = previousStim_color_colorDict.split('-')

        # while loop until the right stimuli w.r.t. to the previous stim was found
        stimFound = False
        while stimFound == False:
            # randomly choose a stim from general stimulus pool
            currentStim = df_stimList.sample()
            # split it up for comparison
            string_currentStim = currentStim.iloc[0, 0]
            splitted_currentStim_color = string_currentStim.split('w')[0]
            splitted_currentStim_form = string_currentStim.split('w')[1].split('.')[0]

            stimFound = assignFunc_color(c1, c2, c3)

        # the current stim is the previous for the next iteration in the for loop
        previousStim = trials_normal_preDF.loc[i, 1]
        # split it up for comparison
        splitted_previousStim_color = previousStim.split('w')[0]
        splitted_previousStim_form = previousStim.split('w')[1].split('.')[0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_normal.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_normal.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_normal.iloc[i, 34] = 10
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_normal.iloc[i, 35] = 1
        else:
            trials_normal.iloc[i, 35] = 0

# Save df as spreadsheet
trials_normal.to_excel('spreadsheetNormal_WorkingMemory_Anti.xlsx')


# ======================================================================================================================
# Create 240 trials for hard
# ======================================================================================================================

def assignFunc_form(form1, form2, form3, iter):
    if splitted_currentStim_form == form1 or splitted_currentStim_form == form2 or splitted_currentStim_form == form3:
        # add sampled stim to trial df
        trials_hard.loc[iter, fieldNumberList[1]] = currentStim.iloc[0, 0]
        trials_hard_preDF.loc[iter, 1] = currentStim.iloc[0, 0]
        # check for consecutive trial
        if iter != len(trials_hard) - 1:
            if pd.isna(trials_hard_preDF.loc[iter + 1, 0]):
                trials_hard_preDF.loc[iter + 1, 0] = currentStim.iloc[0, 0]
            else:
                trials_hard.loc[iter, fieldNumberList[1]] = '180_0w1_0.png'
                trials_hard_preDF.loc[iter, 1] = '180_0w1_0.png'

        # Save correct answer to real df
        trials_hard.loc[iter, 36] = trials_hard_preDF.loc[iter, 1]

        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

def assignFunc_color(color1, color2, color3, form1, form2, form3, iter):
    if splitted_currentStim_color == color2 and splitted_currentStim_form != splitted_previousStim_form or \
        splitted_currentStim_color == color1 or splitted_currentStim_color == color3:

        stimFound = assignFunc_form(form1, form2, form3, iter)
        return stimFound

    else:
        stimFound = False
        return stimFound

formDict = {
    '0_25': '0_25-0_5-0_75',
    '0_50': '0_25-0_5-0_75',
    '0_75': '0_5-0_75-1_0',
    '1_0': '0_5-0_75-1_0'
}

# Create empty trials hard df
trials_hard = pd.DataFrame(index = range(240), columns = range(37))
trials_hard_preDF = pd.DataFrame(index = range(240), columns = range(2))

# Put in the 180_0w1_0.png beginnings and ends for being able two shuffle the paired trials:
trials_hard_preDF.loc[0,0] = '180_0w1_0.png'
trials_hard_preDF.loc[60,0] = '180_0w1_0.png'
trials_hard_preDF.loc[120,0] = '180_0w1_0.png'
trials_hard_preDF.loc[180,0] = '180_0w1_0.png'
trials_hard_preDF.loc[240,0] = '180_0w1_0.png'

# Allocate first previous stim
previousStim = '180_0w1_0.png'
# split it up for comparison
splitted_previousStim_color = previousStim.split('w')[0]
splitted_previousStim_form = previousStim.split('w')[1].split('.')[0]


for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):
        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], 2)
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 2)
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

                if abs(fieldNumberList[1] - fieldNumberList[l]) <= 2 and l != 1 or abs(fieldNumberList[0] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 4:
                noChange = True

        # Add first stim to real df
        trials_hard.loc[iter, fieldNumberList[0]] = trials_hard_preDF.loc[iter, 0]

        # colors to look for w.r.t. previous Stim
        outPrevious_colorDict = colorDict[splitted_previousStim_color]
        [c1, c2, c3] = outPrevious_colorDict.split('-')
        # forms to look for w.r.t. previous Stim
        outPrevious_formDict = formDict[splitted_previousStim_form]
        [f1, f2, f3] = outPrevious_formDict.split('-')

        # .. until right stim according to the previous stim conditions was found
        stimFound = False
        while stimFound == False:
            # randomly choose a stim from general stimulus pool
            currentStim = df_stimList.sample()
            # split it up for comparison
            string_currentStim = currentStim.iloc[0, 0]
            splitted_currentStim_color = string_currentStim.split('w')[0]
            splitted_currentStim_form = string_currentStim.split('w')[1].split('.')[0]

            # Apply function for finding right consecutive stimulus
            stimFound = assignFunc_color(c1, c2, c3, f1, f2, f3, iter)

        # At the end allocate previous stim for next for loop
        previousStim = trials_hard_preDF.iloc[iter, 1]
        # split it up for comparison
        splitted_previousStim_color = previousStim.split('w')[0]
        splitted_previousStim_form = previousStim.split('w')[1].split('.')[0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_hard.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_hard.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_hard.iloc[i, 34] = 10
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_hard.iloc[i, 35] = 1
        else:
            trials_hard.iloc[i, 35] = 0

# Save df as spreadsheet
trials_hard.to_excel('spreadsheetHard_WorkingMemory_Anti.xlsx')


