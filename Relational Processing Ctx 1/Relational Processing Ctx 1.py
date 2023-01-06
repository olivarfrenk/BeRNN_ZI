import pandas as pd
import numpy as np
import os
import random
from collections import Counter

# Direct to project file
os.getcwd()
os.chdir('./Relational Processing Ctx 1')

# Create general stimulus pool
AllStimuli = pd.read_excel('AllStimuli.xlsx')
# Concatenate all columns from AllStimuli into one united column
stimList = []
for iter in range(len(AllStimuli.columns)):
    currentList = AllStimuli.iloc[:, iter].tolist()
    stimList = stimList + currentList

df_stimList = pd.DataFrame(stimList)


# ======================================================================================================================
# Create 200 trials for easy - all stimuli in consecutive trial allowed
# ======================================================================================================================
# Create empty trials easy df
trials_easy = pd.DataFrame(index = range(240), columns = range(40))

correctAnswer_dict = {
    '360_0': '360_0w1_0.png-360_0w0_50.png-360_0w0_75.png-360_0w0_25.png',
    '360_1': '360_1w1_0.png-360_1w0_50.png-360_1w0_75.png-360_1w0_25.png',
    '300_0': '300_0w1_0.png-300_0w0_50.png-300_0w0_75.png-300_0w0_25.png',
    '300_1': '300_1w1_0.png-300_1w0_50.png-300_1w0_75.png-300_1w0_25.png',
    '240_0': '240_0w1_0.png-240_0w0_50.png-240_0w0_75.png-240_0w0_25.png',
    '240_1': '240_1w1_0.png-240_1w0_50.png-240_1w0_75.png-240_1w0_25.png',
    '180_0': '180_0w1_0.png-180_0w0_50.png-180_0w0_75.png-180_0w0_25.png',
    '180_1': '180_1w1_0.png-180_1w0_50.png-180_1w0_75.png-180_1w0_25.png',
    '120_0': '120_0w1_0.png-120_0w0_50.png-120_0w0_75.png-120_0w0_25.png',
    '120_1': '120_1w1_0.png-120_1w0_50.png-120_1w0_75.png-120_1w0_25.png',
    '60_0': '60_0w1_0.png-60_0w0_50.png-60_0w0_75.png-60_0w0_25.png',
    '60_1': '60_1w1_0.png-60_1w0_50.png-60_1w0_75.png-60_1w0_25.png'
}

# Fill all rows for the first 100 and second 100 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):

        valueColorsIndex = 0
        while valueColorsIndex == 0:
            # Allocate lists for the stimuli presented in one trial
            stimList = []
            colorList = []
            for i in range(3):
                currentStim = df_stimList.sample()
                splitted_currentStim_Color = currentStim.iloc[0, 0].split('w')[0]
                # Append first stim to list of 3 stimuli in total for one trial
                stimList.append(currentStim)
                colorList.append(splitted_currentStim_Color)
            # Get the most common color
            keyColors = Counter(colorList).keys()
            valueColors = list(Counter(colorList).values())
            # Check if found
            valueColorsIndex = valueColors.index(max(valueColors))

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
        # Add correct answers to every trial row
        trials_easy.iloc[iter, 36] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0,0].split('w')[0]].split('-')[0]
        trials_easy.iloc[iter, 37] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0,0].split('w')[0]].split('-')[1]
        trials_easy.iloc[iter, 38] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0,0].split('w')[0]].split('-')[2]
        trials_easy.iloc[iter, 39] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0,0].split('w')[0]].split('-')[3]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_easy.iloc[iter, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_easy.iloc[iter, 33] = after_response_time[0]
        # Add Block Randomization
        trials_easy.iloc[iter, 34] = 7
        # Add Block Division
        if iter == 59 or iter == 119 or iter == 179 or iter == 239:
            trials_easy.iloc[iter, 35] = 1
        else:
            trials_easy.iloc[iter, 35] = 0

# Save df as spreadsheet
trials_easy.to_excel('spreadsheetEasy_RelationalProcessing_Ctx1.xlsx')


# ======================================================================================================================
# Create 200 trials for normal - Only similiar colors in consecutive trials
# ======================================================================================================================
# Create empty trials normal df
trials_normal = pd.DataFrame(index = range(240), columns = range(40))

# Create dictionary for colors with their similar connections
colorDict = {
    '360': '300_0-360_0-60_0-300_1-360_1-60_1',
    '300': '240_0-300_0-360_0-240_1-300_1-360_1',
    '240': '180_0-240_0-300_0-180_1-240_1-300_1',
    '180': '120_0-180_0-240_0-120_0-180_0-240_0',
    '120': '60_0-120_0-180_0-60_1-120_1-180_1',
    '60': '360_0-60_0-120_0-360_1-60_1-120_1'
}

def assignFunc_color(color1, color2, color3, color4, color5, color6):
    if splitted_currentStim_Color == color1 or splitted_currentStim_Color == color2 or splitted_currentStim_Color == color3 or\
        splitted_currentStim_Color == color4 or splitted_currentStim_Color == color5 or splitted_currentStim_Color == color6:
        # append
        stimList.append(currentStim)
        colorList.append(splitted_currentStim_Color)
        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

# Fill all rows for the first 100 and second 100 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):

        valueColorsIndex = 0
        while valueColorsIndex == 0:
            # Allocate lists for the stimuli presented in one trial
            stimList = []
            colorList = []
            firstStim = df_stimList.sample()
            splitted_firstStim_Color = firstStim.iloc[0, 0].split('_')[0]
            # colors to look for w.r.t. first Stim
            outfirstStim_Color_colorDict = colorDict[splitted_firstStim_Color]
            [c1, c2, c3, c4, c5, c6] = outfirstStim_Color_colorDict.split('-')
            for i in range(4):
                stimFound = False
                while stimFound == False:
                    currentStim = df_stimList.sample()
                    splitted_currentStim_Color = currentStim.iloc[0, 0].split('w')[0]
                    stimFound = assignFunc_color(c1, c2, c3, c4, c5, c6)

            # Get the most common color
            keyColors = Counter(colorList).keys()
            valueColors = list(Counter(colorList).values())
            # Check if found
            valueColorsIndex = valueColors.index(max(valueColors))

        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],5)
            fieldList = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 5)
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

                if abs(fieldNumberList[3]-fieldNumberList[l]) <= 2 and l != 3 or abs(fieldNumberList[1] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[4] - fieldNumberList[l]) <= 2 and l != 4 or abs(fieldNumberList[2] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 25:
                noChange = True

        # Assign every stim to its field according to the sampled random numbers in fieldNumberList
        for i in range(len(stimList)):
            trials_normal.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0,0]
        # Add correct answers to every trial row
        trials_normal.iloc[iter, 36] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[0]
        trials_normal.iloc[iter, 37] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[1]
        trials_normal.iloc[iter, 38] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[2]
        trials_normal.iloc[iter, 39] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[3]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_normal.iloc[iter, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_normal.iloc[iter, 33] = after_response_time[0]
        # Add Block Randomization
        trials_normal.iloc[iter, 34] = 7
        # Add Block Division
        if iter == 59 or iter == 119 or iter == 179 or iter == 239:
            trials_normal.iloc[iter, 35] = 1
        else:
            trials_normal.iloc[iter, 35] = 0

# Save df as spreadsheet
trials_normal.to_excel('spreadsheetNormal_RelationalProcessing_Ctx1.xlsx')


# ======================================================================================================================
# Create 200 trials for hard - Only similiar colors and forms in consecutive trials
# ======================================================================================================================
# Create empty trials hard df
trials_hard = pd.DataFrame(index = range(240), columns = range(40))

# Create dictionary for forms with their similar connections
formDict = {
    '0_25': '0_25-0_50-0_75',
    '0_50': '0_25-0_50-0_75',
    '0_75': '0_50-0_75-1_0',
    '1_0': '0_25-0_50-0_75'
}

def assignFunc_form(form1, form2, form3):
    if splitted_currentStim_Form == form1 or splitted_currentStim_Form == form2 or splitted_currentStim_Form == form3:
        # append
        stimList.append(currentStim)
        colorList.append(splitted_currentStim_Color)
        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

def assignFunc_color(color1, color2, color3, color4, color5, color6, form1, form2, form3):
    if splitted_currentStim_Color == color1 or splitted_currentStim_Color == color2 or splitted_currentStim_Color == color3 or\
            splitted_currentStim_Color == color4 or splitted_currentStim_Color == color5 or splitted_currentStim_Color == color6:
        stimFound = assignFunc_form(form1, form2, form3)
        return stimFound

    else:
        stimFound = False
        return stimFound

# Fill all rows for the first 100 and second 100 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):

        valueColorsIndex = 0
        while valueColorsIndex == 0:
            # Allocate lists for the stimuli presented in one trial
            stimList = []
            colorList = []
            # colors to look for w.r.t. first Stim
            firstStim = df_stimList.sample()
            splitted_firstStim_Color = firstStim.iloc[0, 0].split('_')[0]
            outfirstStim_Color_colorDict = colorDict[splitted_firstStim_Color]
            [c1, c2, c3, c4, c5, c6] = outfirstStim_Color_colorDict.split('-')
            # forms to look for w.r.t. first Stim
            splitted_firstStim_Form = firstStim.iloc[0, 0].split('w')[1].split('.')[0]
            outfirstStim_Form_formDict = formDict[splitted_firstStim_Form]
            [f1, f2, f3] = outfirstStim_Form_formDict.split('-')
            for i in range(4):
                stimFound = False
                while stimFound == False:
                    currentStim = df_stimList.sample()
                    splitted_currentStim_Color = currentStim.iloc[0, 0].split('w')[0]
                    splitted_currentStim_Form = currentStim.iloc[0, 0].split('w')[1].split('.')[0]
                    stimFound = assignFunc_color(c1, c2, c3, c4, c5, c6, f1, f2, f3)

            # Get the most common color
            keyColors = Counter(colorList).keys()
            valueColors = list(Counter(colorList).values())
            # Check if found
            valueColorsIndex = valueColors.index(max(valueColors))

        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],7)
            fieldList = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 7)
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

                if abs(fieldNumberList[3]-fieldNumberList[l]) <= 2 and l != 3 or abs(fieldNumberList[1] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[4] - fieldNumberList[l]) <= 2 and l != 4 or abs(fieldNumberList[2] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[5] - fieldNumberList[l]) <= 2 and l != 5 or abs(
                        fieldNumberList[5] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[6] - fieldNumberList[l]) <= 2 and l != 6 or abs(
                        fieldNumberList[6] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList, 1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 49:
                noChange = True

        # Assign every stim to its field according to the sampled random numbers in fieldNumberList
        for i in range(len(stimList)):
            trials_hard.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0,0]
        # Add correct answers to every trial row
        trials_hard.iloc[iter, 36] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[0]
        trials_hard.iloc[iter, 37] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[1]
        trials_hard.iloc[iter, 38] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[2]
        trials_hard.iloc[iter, 39] = correctAnswer_dict[stimList[valueColorsIndex].iloc[0, 0].split('w')[0]].split('-')[3]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_hard.iloc[iter, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_hard.iloc[iter, 33] = after_response_time[0]
        # Add Block Randomization
        trials_hard.iloc[iter, 34] = 7
        # Add Block Division
        if iter == 59 or iter == 119 or iter == 179 or iter == 239:
            trials_hard.iloc[iter, 35] = 1
        else:
            trials_hard.iloc[iter, 35] = 0

# Save df as spreadsheet
trials_hard.to_excel('spreadsheetHard_RelationalProcessing_Ctx1.xlsx')



