import pandas as pd
import os
import random

# Direct to project file
# os.getcwd()
os.chdir('./Decision Making')

stims = pd.DataFrame(['Uw0_25.png', 'Dw0_25.png', 'Lw0_25.png', 'Rw0_25.png',\
                      'Uw0_5.png', 'Dw0_5.png', 'Lw0_5.png', 'Rw0_5.png',\
                      'Uw0_75.png', 'Dw0_75.png', 'Lw0_75.png', 'Rw0_75.png',\
                      'Uw1_0.png', 'Dw1_0.png', 'Lw1_0.png', 'Rw1_0.png'])


# ======================================================================================================================
# Create 200 trials for easy - random
# ======================================================================================================================
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
        # Randomly choose a stim from general stimulus pool as the right direction stim
        centralStim = stims.sample()
        correct_answerDirection = centralStim.iloc[0, 0].split('w')[0]
        stimList.append(centralStim)
        # Randomly choose another one
        otherStim = stims.sample()
        stimList.append(otherStim)

        # ratio list for the two stims
        ratio_list = [[1,0]]
        ratio = random.sample(ratio_list, 1)

        for i in range(ratio[0][0]):
            stimList.append(stimList[0])

        for i in range(ratio[0][1]):
            stimList.append(stimList[1])

        # Sample a random number for every stimulus per trial for assigning them to their field in experiment space
        if displays == 0:
            fieldNumberList = random.sample([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], 3)
            fieldList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
        else:
            fieldNumberList = random.sample([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 3)
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

            if countNoChange == 9:
                noChange = True

        # Assign every stim to its field according to the sampled random numbers in fieldNumberList
        for i in range(len(stimList)):
            trials_easy.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0, 0]
        # Save correct answer to real df
        trials_easy.loc[iter, 36] = correct_answerDirection

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_easy.iloc[iter, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_easy.iloc[iter, 33] = after_response_time[0]
        # Add Block Randomization
        trials_easy.iloc[iter, 34] = 1
        # Add Block Division
        if iter == 59 or iter == 119 or iter == 179 or iter == 239:
            trials_easy.iloc[iter, 35] = 1
        else:
            trials_easy.iloc[iter, 35] = 0


# Save df as spreadsheet
trials_easy.to_excel('spreadsheetEasy_DecisionMaking.xlsx')


# ======================================================================================================================
# Create 200 trials for normal - similiar strengths
# ======================================================================================================================
trials_normal = pd.DataFrame(index = range(240), columns = range(37))

def assignFunc_strength(strength1, strength2, strength3):

    if splitted_otherStim_strength == strength1 or splitted_otherStim_strength == strength2 or splitted_otherStim_strength == strength3:
        stimFound = True
        stimList.append(otherStim)
        return stimFound
    else:
        stimFound = False
        return stimFound

# Create dictionary for colors with their similar connections
strengthDict = {
    '0_25': '0-0_25-0_5',
    '0_5': '0_25-0_5-0_75',
    '0_75': '0_5-0_75-1_0',
    '1_0': '0-0_75-1_0'
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
        # Randomly choose a stim from general stimulus pool as the right direction stim
        centralStim = stims.sample()
        correct_answerDirection = centralStim.iloc[0, 0].split('w')[0]
        stimList.append(centralStim)
        # Get direction and strength for choosing the other stims
        splitted_centralStim_strength = centralStim.iloc[0, 0].split('w')[1].split('.')[0]
        # colors to look for w.r.t. central Stim
        centralStim_strength_strengthDict = strengthDict[splitted_centralStim_strength]
        [s1, s2, s3] = centralStim_strength_strengthDict.split('-')

        # sample the two other stim types
        for i in range(2):

            stimFound = False
            while stimFound == False:
                otherStim = stims.sample()
                # Split new sampled stim for comparison
                splitted_otherStim_strength = otherStim.iloc[0, 0].split('w')[1].split('.')[0]
                stimFound = assignFunc_strength(s1, s2, s3)

        # ratio list for the two stims
        ratio_list = [[2, 0, 0]]
        ratio = random.sample(ratio_list, 1)

        for i in range(ratio[0][0]):
            stimList.append(stimList[0])

        for i in range(ratio[0][1]):
            stimList.append(stimList[1])

        for i in range(ratio[0][2]):
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
            trials_normal.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0, 0]
        # Save correct answer to real df
        trials_normal.loc[iter, 36] = correct_answerDirection

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_normal.iloc[iter, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_normal.iloc[iter, 33] = after_response_time[0]
        # Add Block Randomization
        trials_normal.iloc[iter, 34] = 1
        # Add Block Division
        if iter == 59 or iter == 119 or iter == 179 or iter == 239:
            trials_normal.iloc[iter, 35] = 1
        else:
            trials_normal.iloc[iter, 35] = 0

# Save df as spreadsheet
trials_normal.to_excel('spreadsheetNormal_DecisionMaking.xlsx')


# ======================================================================================================================
# Create 200 trials for hard - similiar strengths, incongruent direction
# ======================================================================================================================
trials_hard = pd.DataFrame(index = range(240), columns = range(37))

def assignFunc_direction(direction1):
    if splitted_otherStim_direction == direction1:
        stimFound = True
        stimList.append(otherStim)
        return stimFound

    else:
        stimFound = False
        return stimFound

# Create dictionary for forms with their similar connections
directionDict = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'U'
}

def assignFunc_strength(strength1, strength2, strength3, direction1):

    if splitted_otherStim_strength == strength1 or splitted_otherStim_strength == strength2 or splitted_otherStim_strength == strength3:
        stimFound = assignFunc_direction(direction1)
        return stimFound
    else:
        stimFound = False
        return stimFound

# Create dictionary for colors with their similar connections
strengthDict = {
    '0_25': '0-0_25-0_5',
    '0_5': '0_25-0_5-0_75',
    '0_75': '0_5-0_75-1_0',
    '1_0': '0-0_75-1_0'
}

# Fill all rows for the first 100 and second 100 (for distributing reasons on the two circles in gorilla)
for displays in range(2):
    if displays == 0:
        rangeList = [0,120]
    else:
        rangeList = [120,240]

    for iter in range(rangeList[0],rangeList[1]):
        stimList = []
        # Randomly choose a stim from general stimulus pool
        centralStim = stims.sample()
        correct_answerDirection = centralStim.iloc[0, 0].split('w')[0]
        stimList.append(centralStim)
        # Split it
        splitted_centralStim_strength = centralStim.iloc[0, 0].split('w')[1].split('.')[0]
        splitted_centralStim_direction = centralStim.iloc[0, 0].split('w')[0]
        # strengths to look for w.r.t. central Stim
        centralStim_strength_strengthDict = strengthDict[splitted_centralStim_strength]
        [s1, s2, s3] = centralStim_strength_strengthDict.split('-')
        # direction to look for w.r.t. central Stim
        centralStim_direction_directionDict = directionDict[splitted_centralStim_direction]
        [d1] = centralStim_direction_directionDict.split('-')

        # sample the three other stim types
        for i in range(3):

            stimFound = False
            while stimFound == False:
                otherStim = stims.sample()
                # Split new sampled stim for comparison
                splitted_otherStim_strength = otherStim.iloc[0, 0].split('w')[1].split('.')[0]
                splitted_otherStim_direction = otherStim.iloc[0, 0].split('w')[0]
                stimFound = assignFunc_strength(s1, s2, s3, d1)

        # ratio list for the two stims
        ratio_list = [[3, 0, 0, 0]]
        ratio = random.sample(ratio_list, 1)

        for i in range(ratio[0][0]):
            stimList.append(stimList[0])

        for i in range(ratio[0][1]):
            stimList.append(stimList[1])

        for i in range(ratio[0][2]):
            stimList.append(stimList[2])

        for i in range(ratio[0][3]):
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

                if abs(fieldNumberList[5] - fieldNumberList[l]) <= 2 and l != 5 or abs(fieldNumberList[5] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

                if abs(fieldNumberList[6] - fieldNumberList[l]) <= 2 and l != 6 or abs(fieldNumberList[6] - fieldNumberList[l]) >= 30:
                    fieldNumberList[l] = random.sample(fieldList,1)[0]
                else:
                    countNoChange += 1

            if countNoChange == 49:
                noChange = True

        # Assign every stim to its field according to the sampled random numbers in fieldNumberList
        for i in range(len(stimList)):
            trials_hard.iloc[iter, fieldNumberList[i]] = stimList[i].iloc[0, 0]
        # Save correct answer to real df
        trials_normal.loc[iter, 36] = correct_answerDirection

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_hard.iloc[iter, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_hard.iloc[iter, 33] = after_response_time[0]
        # Add Block Randomization
        trials_hard.iloc[iter, 34] = 1
        # Add Block Division
        if iter == 59 or iter == 119 or iter == 179 or iter == 239:
            trials_hard.iloc[iter, 35] = 1
        else:
            trials_hard.iloc[iter, 35] = 0

# Save df as spreadsheet
trials_hard.to_excel('spreadsheetHard_DecisionMaking.xlsx')