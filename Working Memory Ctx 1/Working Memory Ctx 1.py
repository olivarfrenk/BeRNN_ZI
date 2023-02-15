import pandas as pd
import os
import random

# Direct to project file
os.getcwd()
os.chdir('./Working Memory Ctx 1')


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
# Create 240 trials for easy - all stimuli in consecutive trial allowed
# ======================================================================================================================
trials_easy = pd.DataFrame(index = range(248), columns = range(37))

# Sample very first trial
firstStim = df_stimList.sample()
secondStim = df_stimList.sample()
firstStim_memory2 = firstStim
firstStim_memory2_color = firstStim_memory2.iloc[0,0].split('w')[0]
secondStim_memory2 = secondStim
secondStim_memory2_color = secondStim_memory2.iloc[0,0].split('w')[0]
# Create very first trial
trials_easy.iloc[0, 1] = firstStim.iloc[0,0]
trials_easy.iloc[0, 17] = secondStim.iloc[0,0]
trials_easy.iloc[0, 34] = 11
trials_easy.iloc[0, 35] = 0
trials_easy.loc[0, 36] = 'Mismatch'
# Add random fixation cross time
fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
trials_easy.iloc[0, 32] = fixation_cross_time[0]
# Add random after response time
after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
trials_easy.iloc[0, 33] = after_response_time[0]

# Sample second trial
firstStim = df_stimList.sample()
secondStim = df_stimList.sample()
firstStim_memory1 = firstStim
firstStim_memory1_color = firstStim_memory1.iloc[0,0].split('w')[0]
secondStim_memory1 = secondStim
secondStim_memory1_color = secondStim_memory1.iloc[0,0].split('w')[0]
# Create second trial
trials_easy.iloc[1, 7] = firstStim.iloc[0,0]
trials_easy.iloc[1, 23] = secondStim.iloc[0,0]
trials_easy.iloc[1, 34] = 11
trials_easy.iloc[1, 35] = 0
trials_easy.loc[1, 36] = 'Mismatch'
# Add random fixation cross time
fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
trials_easy.iloc[1, 32] = fixation_cross_time[0]
# Add random after response time
after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
trials_easy.iloc[1, 33] = after_response_time[0]


# Fill all rows for the first 120 and second 120 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [2,124]
    else:
        rangeList = [124,248]

    for i in range(rangeList[0], rangeList[1]):
        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
            fieldNumberList = random.sample(fieldList, 2)
        else:
            fieldList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
            fieldNumberList = random.sample(fieldList, 2)

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


        # Create subsequently connected trials
        ratioMatches = random.sample([0,1], 1)
        if ratioMatches[0] == 0:
            diffFound = False
            while diffFound == False:
                # Overtake the stims from the previous trial
                firstStim = df_stimList.sample()
                firstStim_currentTrial_color = firstStim.iloc[0, 0].split('w')[0]
                secondStim = df_stimList.sample()
                secondStim_currentTrial_color = secondStim.iloc[0, 0].split('w')[0]

                correctAnswer = 'Match'

                if firstStim_currentTrial_color == firstStim_memory2_color and secondStim_currentTrial_color == secondStim_memory2_color or \
                        firstStim_currentTrial_color == secondStim_memory2_color and secondStim_currentTrial_color == firstStim_memory2_color:
                    diffFound = True
                else:
                    diffFound = False

        else:
            diffFound = False
            while diffFound == False:
                firstStim = df_stimList.sample()
                firstStim_currentTrial_color = firstStim.iloc[0, 0].split('w')[0]
                secondStim = df_stimList.sample()
                secondStim_currentTrial_color = secondStim.iloc[0, 0].split('w')[0]

                correctAnswer = 'Mismatch'

                if firstStim_currentTrial_color == firstStim_memory2_color and secondStim_currentTrial_color == secondStim_memory2_color or \
                        firstStim_currentTrial_color == secondStim_memory2_color and secondStim_currentTrial_color == firstStim_memory2_color:
                    diffFound = False
                else:
                    diffFound = True

        # Save the two memory1 to memory2
        firstStim_memory2_color = firstStim_memory1_color
        secondStim_memory2_color = secondStim_memory1_color

        # Save the two for the next trial
        firstStim_memory1_color = firstStim.iloc[0, 0].split('w')[0]
        secondStim_memory1_color = secondStim.iloc[0, 0].split('w')[0]

        # Save the stims in the df
        trials_easy.loc[i, fieldNumberList[0]] = firstStim.iloc[0,0]
        trials_easy.loc[i, fieldNumberList[1]] = secondStim.iloc[0,0]
        # Save correct answer
        trials_easy.loc[i, 36] = correctAnswer

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_easy.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_easy.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_easy.iloc[i, 34] = 11
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_easy.iloc[i, 35] = 1
        else:
            trials_easy.iloc[i, 35] = 0

# Save df as spreadsheet
trials_easy.to_excel('spreadsheetEasy_WorkingMemory_Ctx1.xlsx')


# ======================================================================================================================
# Create 240 trials for normal - Only similiar colors in consecutive trials
# ======================================================================================================================
trials_normal = pd.DataFrame(index = range(248), columns = range(37))

# Create dictionary for colors with their similar connections
colorDict = {
    '360': '300_0-360_0-60_0-300_1-360_1-60_1',
    '300': '240_0-300_0-360_0-240_1-300_1-360_1',
    '240': '180_0-240_0-300_0-180_1-240_1-300_1',
    '180': '120_0-180_0-240_0-120_0-180_0-240_0',
    '120': '60_0-120_0-180_0-60_1-120_1-180_1',
    '60': '360_0-60_0-120_0-360_1-60_1-120_1'
}

def assignFunc_color(color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12):
    if firstStim_currentTrial_color == color1 or firstStim_currentTrial_color == color2 or firstStim_currentTrial_color == color3 or\
        firstStim_currentTrial_color == color4 or firstStim_currentTrial_color == color5 or firstStim_currentTrial_color == color6 and\
        secondStim_currentTrial_color == color7 or secondStim_currentTrial_color == color8 or secondStim_currentTrial_color == color9 or\
        secondStim_currentTrial_color == color10 or secondStim_currentTrial_color == color11 or secondStim_currentTrial_color == color12:
        # Save the stims in the df
        trials_normal.loc[i, fieldNumberList[0]] = firstStim.iloc[0,0]
        trials_normal.loc[i, fieldNumberList[1]] = secondStim.iloc[0,0]
        # Save correct answer
        trials_normal.loc[i, 36] = correctAnswer

        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

# Sample very first trial
firstStim = df_stimList.sample()
secondStim = df_stimList.sample()

firstStim_memory2 = firstStim
firstStim_memory2_color = firstStim_memory2.iloc[0,0].split('w')[0]
secondStim_memory2 = secondStim
secondStim_memory2_color = secondStim_memory2.iloc[0,0].split('w')[0]

# Create very first trial
trials_normal.iloc[0, 1] = firstStim.iloc[0,0]
trials_normal.iloc[0, 17] = secondStim.iloc[0,0]
trials_normal.iloc[0, 34] = 11
trials_normal.iloc[0, 35] = 0
trials_normal.loc[0, 36] = 'Mismatch'

# Add random fixation cross time
fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
trials_normal.iloc[0, 32] = fixation_cross_time[0]
# Add random after response time
after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
trials_normal.iloc[0, 33] = after_response_time[0]


# Sample second trial
firstStim = df_stimList.sample()
secondStim = df_stimList.sample()

firstStim_memory1 = firstStim
firstStim_memory1_color = firstStim_memory1.iloc[0,0].split('w')[0]
secondStim_memory1 = secondStim
secondStim_memory1_color = secondStim_memory1.iloc[0,0].split('w')[0]

# Create very first trial
trials_normal.iloc[1, 7] = firstStim.iloc[0,0]
trials_normal.iloc[1, 23] = secondStim.iloc[0,0]
trials_normal.iloc[1, 34] = 11
trials_normal.iloc[1, 35] = 0
trials_normal.loc[1, 36] = 'Mismatch'

# Add random fixation cross time
fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
trials_normal.iloc[1, 32] = fixation_cross_time[0]
# Add random after response time
after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
trials_normal.iloc[1, 33] = after_response_time[0]


# Fill all rows for the first 120 and second 120 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [2,124]
    else:
        rangeList = [124,248]

    for i in range(rangeList[0], rangeList[1]):
        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
            fieldNumberList = random.sample(fieldList,2)
        else:
            fieldList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
            fieldNumberList = random.sample(fieldList,2)

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

        stimFound = False
        while stimFound == False:
            # Create subsequently connected trials
            ratioMatches = random.sample([0,1], 1)
            if ratioMatches[0] == 0:
                diffFound = False
                while diffFound == False:
                    # Overtake the stims from the previous trial
                    firstStim = df_stimList.sample()
                    firstStim_currentTrial_color = firstStim.iloc[0,0].split('w')[0]
                    secondStim = df_stimList.sample()
                    secondStim_currentTrial_color = secondStim.iloc[0,0].split('w')[0]

                    correctAnswer = 'Match'

                    if firstStim_currentTrial_color == firstStim_memory2_color and secondStim_currentTrial_color == secondStim_memory2_color or \
                            firstStim_currentTrial_color == secondStim_memory2_color and secondStim_currentTrial_color == firstStim_memory2_color:
                        diffFound = True
                    else:
                        diffFound = False

            else:
                # Create new stims
                diffFound = False
                while diffFound == False:
                    firstStim = df_stimList.sample()
                    firstStim_currentTrial_color = firstStim.iloc[0,0].split('w')[0]
                    secondStim = df_stimList.sample()
                    secondStim_currentTrial_color = secondStim.iloc[0,0].split('w')[0]

                    correctAnswer = 'Mismatch'

                    if firstStim_currentTrial_color == firstStim_memory2_color and secondStim_currentTrial_color == secondStim_memory2_color or \
                        firstStim_currentTrial_color == secondStim_memory2_color and secondStim_currentTrial_color == firstStim_memory2_color:
                        diffFound = False
                    else:
                        diffFound = True

            # See if the colors match
            firstStim_memory2_color_colorDict = colorDict[firstStim_memory2_color.split('_')[0]]
            [c1, c2, c3, c4, c5, c6] = firstStim_memory2_color_colorDict.split('-')
            secondStim_memory2_color_colorDict = colorDict[secondStim_memory2_color.split('_')[0]]
            [c7, c8, c9, c10, c11, c12] = secondStim_memory2_color_colorDict.split('-')
            stimFound = assignFunc_color(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12)

        # Save the two memory1 to memory2
        firstStim_memory2_color = firstStim_memory1_color
        secondStim_memory2_color = secondStim_memory1_color

        # Save the two for the next trial
        firstStim_memory1_color = firstStim.iloc[0, 0].split('w')[0]
        secondStim_memory1_color = secondStim.iloc[0, 0].split('w')[0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_normal.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_normal.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_normal.iloc[i, 34] = 11
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_normal.iloc[i, 35] = 1
        else:
            trials_normal.iloc[i, 35] = 0

# Save df as spreadsheet
trials_normal.to_excel('spreadsheetNormal_WorkingMemory_Ctx1.xlsx')


# ======================================================================================================================
# Create 240 trials for hard
# ======================================================================================================================
trials_hard = pd.DataFrame(index = range(248), columns = range(37))

formDict = {
    '0_25': '0_25-0_5-0_75',
    '0_50': '0_25-0_5-0_75',
    '0_75': '0_5-0_75-1_0',
    '1_0': '0_5-0_75-1_0'
}

def assignFunc_color(color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12):
    if firstStim_currentTrial_color == color1 or firstStim_currentTrial_color == color2 or firstStim_currentTrial_color == color3 or\
        firstStim_currentTrial_color == color4 or firstStim_currentTrial_color == color5 or firstStim_currentTrial_color == color6 and\
        secondStim_currentTrial_color == color7 or secondStim_currentTrial_color == color8 or secondStim_currentTrial_color == color9 or\
        secondStim_currentTrial_color == color10 or secondStim_currentTrial_color == color11 or secondStim_currentTrial_color == color12:
        # Save the stims in the df
        trials_hard.loc[i, fieldNumberList[0]] = firstStim.iloc[0,0]
        trials_hard.loc[i, fieldNumberList[1]] = secondStim.iloc[0,0]
        # Save correct answer
        trials_hard.loc[i, 36] = correctAnswer

        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

def assignFunc_form(color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, form1, form2, form3, form4, form5, form6):
    if firstStim_currentTrial_form == form1 or firstStim_currentTrial_form == form2 or firstStim_currentTrial_form == form3 and\
        secondStim_currentTrial_form == form4 or secondStim_currentTrial_form == form5 or secondStim_currentTrial_form == form6:

        stimFound = assignFunc_color(color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12)
        return stimFound

    else:
        stimFound = False
        return stimFound


# Sample very first trial
firstStim = df_stimList.sample()
secondStim = df_stimList.sample()

firstStim_memory2 = firstStim
firstStim_memory2_color = firstStim_memory2.iloc[0,0].split('w')[0]
firstStim_memory2_form = firstStim_memory2.iloc[0, 0].split('w')[1].split('.')[0]
secondStim_memory2 = secondStim
secondStim_memory2_color = secondStim_memory2.iloc[0,0].split('w')[0]
secondStim_memory2_form = secondStim_memory2.iloc[0, 0].split('w')[1].split('.')[0]

# Create very first trial
trials_hard.iloc[0, 1] = firstStim.iloc[0,0]
trials_hard.iloc[0, 17] = secondStim.iloc[0,0]
trials_hard.iloc[0, 34] = 11
trials_hard.iloc[0, 35] = 0
trials_hard.loc[0, 36] = 'Mismatch'

# Add random fixation cross time
fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
trials_hard.iloc[0, 32] = fixation_cross_time[0]
# Add random after response time
after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
trials_hard.iloc[0, 33] = after_response_time[0]


# Sample second trial
firstStim = df_stimList.sample()
secondStim = df_stimList.sample()

firstStim_memory1 = firstStim
firstStim_memory1_color = firstStim_memory1.iloc[0,0].split('w')[0]
firstStim_memory1_form = firstStim_memory1.iloc[0, 0].split('w')[1].split('.')[0]
secondStim_memory1 = secondStim
secondStim_memory1_color = secondStim_memory1.iloc[0,0].split('w')[0]
secondStim_memory1_form = secondStim_memory1.iloc[0, 0].split('w')[1].split('.')[0]

# Create very first trial
trials_hard.iloc[1, 7] = firstStim.iloc[0,0]
trials_hard.iloc[1, 23] = secondStim.iloc[0,0]
trials_hard.iloc[1, 34] = 11
trials_hard.iloc[1, 35] = 0
trials_hard.loc[1, 36] = 'Mismatch'

# Add random fixation cross time
fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
trials_hard.iloc[1, 32] = fixation_cross_time[0]
# Add random after response time
after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
trials_hard.iloc[1, 33] = after_response_time[0]


# Fill all rows for the first 120 and second 120 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [2,124]
    else:
        rangeList = [124,248]

    for i in range(rangeList[0], rangeList[1]):
        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
            fieldNumberList = random.sample(fieldList,2)
        else:
            fieldList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
            fieldNumberList = random.sample(fieldList,2)

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

        stimFound = False
        while stimFound == False:
            # Create subsequently connected trials
            ratioMatches = random.sample([0,1], 1)
            if ratioMatches[0] == 0:
                diffFound = False
                while diffFound == False:
                    # Overtake the stims from the previous trial
                    firstStim = df_stimList.sample()
                    firstStim_currentTrial_color = firstStim.iloc[0,0].split('w')[0]
                    firstStim_currentTrial_form = firstStim.iloc[0, 0].split('w')[1].split('.')[0]

                    secondStim = df_stimList.sample()
                    secondStim_currentTrial_color = secondStim.iloc[0,0].split('w')[0]
                    secondStim_currentTrial_form = secondStim.iloc[0, 0].split('w')[1].split('.')[0]

                    correctAnswer = 'Match'

                    if firstStim_currentTrial_color == firstStim_memory2_color and secondStim_currentTrial_color == secondStim_memory2_color or \
                            firstStim_currentTrial_color == secondStim_memory2_color and secondStim_currentTrial_color == firstStim_memory2_color:
                        diffFound = True
                    else:
                        diffFound = False

            else:
                # Create new stims
                diffFound = False
                while diffFound == False:
                    firstStim = df_stimList.sample()
                    firstStim_currentTrial_color = firstStim.iloc[0,0].split('w')[0]
                    firstStim_currentTrial_form = firstStim.iloc[0, 0].split('w')[1].split('.')[0]

                    secondStim = df_stimList.sample()
                    secondStim_currentTrial_color = secondStim.iloc[0,0].split('w')[0]
                    secondStim_currentTrial_form = secondStim.iloc[0, 0].split('w')[1].split('.')[0]

                    firstMemoryStim = firstStim
                    secondMemoryStim = secondStim

                    correctAnswer = 'Mismatch'

                    if firstStim_currentTrial_color == firstStim_memory2_color and secondStim_currentTrial_color == secondStim_memory2_color or \
                        firstStim_currentTrial_color == secondStim_memory2_color and secondStim_currentTrial_color == firstStim_memory2_color:
                        diffFound = False
                    else:
                        diffFound = True

            # See if the colors and forms match
            firstStim_memory2_color_colorDict = colorDict[firstStim_memory2_color.split('_')[0]]
            [c1, c2, c3, c4, c5, c6] = firstStim_memory2_color_colorDict.split('-')
            firstStim_memory2_form_formDict = formDict[firstStim_memory2_form]
            [f1, f2, f3] = firstStim_memory2_form_formDict.split('-')

            secondStim_memory2_color_colorDict = colorDict[secondStim_memory2_color.split('_')[0]]
            [c7, c8, c9, c10, c11, c12] = secondStim_memory2_color_colorDict.split('-')
            secondStim_memory2_form_formDict = formDict[secondStim_memory2_form]
            [f4, f5, f6] = secondStim_memory2_form_formDict.split('-')

            stimFound = assignFunc_form(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, f1, f2, f3, f4, f5, f6)

        firstStim_memory2_color = firstStim_memory1_color
        firstStim_memory2_form = firstStim_memory1_form
        secondStim_memory2_color = secondStim_memory1_color
        secondStim_memory2_form = secondStim_memory1_form

        # Save the two for the next trial
        firstStim_memory1_color = firstStim.iloc[0, 0].split('w')[0]
        firstStim_memory1_form = firstStim.iloc[0, 0].split('w')[1].split('.')[0]
        secondStim_memory1_color = secondStim.iloc[0, 0].split('w')[0]
        secondStim_memory1_form = secondStim.iloc[0, 0].split('w')[1].split('.')[0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_hard.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_hard.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_hard.iloc[i, 34] = 11
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_hard.iloc[i, 35] = 1
        else:
            trials_hard.iloc[i, 35] = 0

# Save df as spreadsheet
trials_hard.to_excel('spreadsheetHard_WorkingMemory_Ctx1.xlsx')




# # Bug Fix tool #########################################################################################################
# stopIt = False
# for i in range(len(trials_normal)):
#     if i+2 == len(trials_normal):
#         break
#     print(i)
#     stimuli = []
#     for j in range(37):
#         if type(trials_normal.iloc[i,j]) == str:
#             stimuli.append(trials_normal.loc[i,j])
#     for k in range(37):
#         if type(trials_normal.loc[i+2,k]) == str:
#             stimuli.append(trials_normal.loc[i+2,k])
#     if stimuli[0].split('w')[0] == stimuli[3].split('w')[0] and stimuli[1].split('w')[0] == stimuli[4].split('w')[0] and stimuli[5] == 'Mismatch'\
#         or stimuli[0].split('w')[0] == stimuli[4].split('w')[0] and stimuli[1].split('w')[0] == stimuli[3].split('w')[0] and stimuli[5] == 'Mismatch'\
#         or stimuli[0].split('w')[0] != stimuli[3].split('w')[0] and stimuli[1].split('w')[0] == stimuli[4].split('w')[0] and stimuli[5] == 'Match'\
#         or stimuli[0].split('w')[0] != stimuli[4].split('w')[0] and stimuli[1].split('w')[0] == stimuli[3].split('w')[0] and stimuli[5] == 'Match'\
#         or stimuli[0].split('w')[0] != stimuli[4].split('w')[0] and stimuli[1].split('w')[0] != stimuli[3].split('w')[0] and stimuli[5] == 'Match'\
#         and stimuli[0].split('w')[0] != stimuli[3].split('w')[0] and stimuli[1].split('w')[0] != stimuli[4].split('w')[0] and stimuli[5] == 'Match':
#         print(i)
#         print(stimuli[0])
#         print(stimuli[1])
#         print(stimuli[3])
#         print(stimuli[4])
#         print(stimuli[5])
#         print('ERROR')
#         break
# # ########################################################################################################################
