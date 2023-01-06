# Create a function for the filling the trials_hard df according to the conditions for hard trials
import pandas as pd
import os
import random

# Direct to project file
os.getcwd()
os.chdir('./Working Memory')

# Create general stimulus pool
AllStimuli = pd.read_excel('AllStimuli.xlsx')
# Concatenate all columns from AllStimuli into one united column
stimList = []
for iter in range(len(AllStimuli.columns)):
    currentList = AllStimuli.iloc[:, iter].tolist()
    stimList = stimList + currentList

df_stimList = pd.DataFrame(stimList)


# ======================================================================================================================
# Create 240 trials for hard - Only similiar colors and forms in consecutive trials (32 available Stimuli)
# ======================================================================================================================
# Define functions
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
        # Interrupt while loop
        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

def assignFunc_color(color1, color2, color3, color4, color5, color6, form1, form2, form3, iter):
    if splitted_currentStim_color == color2 and splitted_currentStim_form != splitted_previousStim_form or \
        splitted_currentStim_color == color1 or splitted_currentStim_color == color3 or splitted_currentStim_color == color4 \
        or splitted_currentStim_color == color5 and splitted_currentStim_form != splitted_previousStim_form or splitted_currentStim_color == color6:

        stimFound = assignFunc_form(form1, form2, form3, iter)
        return stimFound

    else:
        stimFound = False
        return stimFound


# Create dictionary for colors and forms with their similar connections
colorDict = {
    '360': '300_0-360_0-60_0-300_1-360_1-60_1',
    '300': '240_0-300_0-360_0-240_1-300_1-360_1',
    '240': '180_0-240_0-300_0-180_1-240_1-300_1',
    '180': '120_0-180_0-240_0-120_0-180_0-240_0',
    '120': '60_0-120_0-180_0-60_1-120_1-180_1',
    '60': '360_0-60_0-120_0-360_1-60_1-120_1'
}

formDict = {
    '0_25': '0_25-0_5-0_75',
    '0_5': '0_25-0_5-0_75',
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
splitted_previousStim_color = previousStim.split('_')[0]
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
        # Save correct answer to real df
        trials_hard.loc[iter, 36] = trials_hard_preDF.loc[iter, 0]

        # colors to look for w.r.t. previous Stim
        outPrevious_colorDict = colorDict[splitted_previousStim_color]
        [c1, c2, c3, c4, c5, c6] = outPrevious_colorDict.split('-')
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
            stimFound = assignFunc_color(c1, c2, c3, c4, c5, c6, f1, f2, f3, iter)

        # At the end allocate previous stim for next for loop
        previousStim = trials_hard_preDF.iloc[iter, 1]
        # split it up for comparison
        splitted_previousStim_color = previousStim.split('_')[0]
        splitted_previousStim_form = previousStim.split('w')[1].split('.')[0]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_hard.iloc[iter, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_hard.iloc[iter, 33] = after_response_time[0]
        # Add Block Randomization
        trials_hard.iloc[iter, 34] = 9
        # Add Block Division
        if iter == 59 or iter == 119 or iter == 179 or iter == 239:
            trials_hard.iloc[iter, 35] = 1
        else:
            trials_hard.iloc[iter, 35] = 0

# Save df as spreadsheet
trials_hard.to_excel('spreadsheetHard_WorkingMemory.xlsx')