import pandas as pd
import os
import random

# Direct to project file
# os.getcwd()
os.chdir('./Executive Function Anti')

stims = pd.DataFrame(['Uw0_25.png', 'Dw0_25.png', 'Lw0_25.png', 'Rw0_25.png',\
                      'Uw0_5.png', 'Dw0_5.png', 'Lw0_5.png', 'Rw0_5.png',\
                      'Uw0_75.png', 'Dw0_75.png', 'Lw0_75.png', 'Rw0_75.png',\
                      'Uw1_0.png', 'Dw1_0.png', 'Lw1_0.png', 'Rw1_0.png',\
                      'XwX.png', 'XwX.png', 'XwX.png', 'XwX.png'])


# ======================================================================================================================
# Create 200 trials for easy - random
# ======================================================================================================================
trials_easy = pd.DataFrame(index = range(240), columns = range(37))

# Create dictionary for forms with their opposite direction
directionDict = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L',
    'X': 'X'
}

for displays in range (4):
    # select rangeList according to display
    if displays == 0:
        rangeList = [0, 60]
        [x,y,z] = [30,0,2]
    elif displays == 1:
        rangeList = [60, 120]
        [x,y,z] = [6,8,10]
    elif displays == 2:
        rangeList = [120, 180]
        [x,y,z] = [14,16,18]
    else:
        rangeList = [180, 240]
        [x,y,z] = [22,24,26]

    for i in range(rangeList[0],rangeList[1]):
        # Randomly choose a stim from general stimulus pool
        centralStim = stims.sample()
        splitted_centralStim_direction = centralStim.iloc[0, 0].split('w')[0]

        if splitted_centralStim_direction == 'X':
            otherStim = centralStim
        else:
            otherStim = stims.sample()

        # Fill the cells for correct and wrong answers
        trials_easy.loc[i, x] = otherStim.iloc[0, 0]
        trials_easy.loc[i, y] = centralStim.iloc[0, 0]
        trials_easy.loc[i, z] = otherStim.iloc[0, 0]
        # Save correct answer to real df
        trials_easy.loc[i, 36] = directionDict[splitted_centralStim_direction]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_easy.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_easy.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_easy.iloc[i, 34] = 4
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_easy.iloc[i, 35] = 1
        else:
            trials_easy.iloc[i, 35] = 0

# Save df as spreadsheet
trials_easy.to_excel('spreadsheetEasy_ExecutiveFunction_Anti.xlsx')


# ======================================================================================================================
# Create 200 trials for normal - similiar strengths
# ======================================================================================================================
trials_normal = pd.DataFrame(index = range(240), columns = range(37))

def assignFunc_strength(strength1, strength2, strength3):

    if splitted_otherStim_strength == strength1 or splitted_otherStim_strength == strength2 or \
            splitted_otherStim_strength == strength3:
        stimFound = True
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

for displays in range (4):
    # select rangeList according to display
    if displays == 0:
        rangeList = [0, 60]
        [w,x,y,z,a] = [28,30,0,2,4]
    elif displays == 1:
        rangeList = [50, 100]
        [w,x,y,z,a] = [4,6,8,10,12]
    elif displays == 2:
        rangeList = [100, 150]
        [w,x,y,z,a] = [12,14,16,18,20]
    else:
        rangeList = [150, 200]
        [w,x,y,z,a] = [20,22,24,26,28]

    for i in range(rangeList[0],rangeList[1]):
        # Randomly choose a stim from general stimulus pool
        centralStim = stims.sample()
        splitted_centralStim_direction = centralStim.iloc[0, 0].split('w')[0]
        if splitted_centralStim_direction != 'X':
            splitted_centralStim_strength = centralStim.iloc[0, 0].split('w')[1].split('.')[0]
            # colors to look for w.r.t. central Stim
            centralStim_strength_strengthDict = strengthDict[splitted_centralStim_strength]
            [s1, s2, s3] = centralStim_strength_strengthDict.split('-')

        stimFound = False
        while stimFound == False:
            if splitted_centralStim_direction == 'X':
                otherStim = centralStim
                stimFound = True
            else:
                otherStim = stims.sample()
                # Split new sampled stim for comparison
                splitted_otherStim_strength = otherStim.iloc[0, 0].split('w')[1].split('.')[0]
                stimFound = assignFunc_strength(s1, s2, s3)

        # Fill the cells for correct and wrong answers
        trials_normal.loc[i, w] = otherStim.iloc[0, 0]
        trials_normal.loc[i, x] = otherStim.iloc[0, 0]
        trials_normal.loc[i, y] = centralStim.iloc[0, 0]
        trials_normal.loc[i, z] = otherStim.iloc[0, 0]
        trials_normal.loc[i, a] = otherStim.iloc[0, 0]
        # Save correct answer to real df
        trials_normal.loc[i, 36] = directionDict[splitted_centralStim_direction]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_normal.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_normal.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_normal.iloc[i, 34] = 4
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_normal.iloc[i, 35] = 1
        else:
            trials_normal.iloc[i, 35] = 0

# Save df as spreadsheet
trials_normal.to_excel('spreadsheetNormal_ExecutiveFunction_Anti.xlsx')


# ======================================================================================================================
# Create 200 trials for hard - similiar strengths, incongruent direction
# ======================================================================================================================
trials_hard = pd.DataFrame(index = range(240), columns = range(37))

def assignFunc_direction(direction1):
    if splitted_otherStim_direction == direction1:
        stimFound = True
        return stimFound

    else:
        stimFound = False
        return stimFound

def assignFunc_strength(strength1, strength2, strength3, direction1):

    if splitted_otherStim_strength == strength1 or splitted_otherStim_strength == strength2 \
            or splitted_otherStim_strength == strength3:
        stimFound = assignFunc_direction(direction1)
        return stimFound
    else:
        stimFound = False
        return stimFound

for displays in range (4):
    # select rangeList according to display
    if displays == 0:
        rangeList = [0, 60]
        [v,w,x,y,z,a,b] = [26,28,30,0,2,4,6]
    elif displays == 1:
        rangeList = [60, 120]
        [v,w,x,y,z,a,b] = [2,4,6,8,10,12,14]
    elif displays == 2:
        rangeList = [120, 180]
        [v,w,x,y,z,a,b] = [10,12,14,16,18,20,22]
    else:
        rangeList = [180, 240]
        [v,w,x,y,z,a,b] = [18,20,22,24,26,28,30]

    for i in range(rangeList[0],rangeList[1]):
        # Randomly choose a stim from general stimulus pool
        centralStim = stims.sample()
        splitted_centralStim_direction = centralStim.iloc[0, 0].split('w')[0]
        if splitted_centralStim_direction != 'X':
            splitted_centralStim_strength = centralStim.iloc[0, 0].split('w')[1].split('.')[0]
            # strengths to look for w.r.t. central Stim
            centralStim_strength_strengthDict = strengthDict[splitted_centralStim_strength]
            [s1, s2, s3] = centralStim_strength_strengthDict.split('-')
            # direction to look for w.r.t. central Stim
            centralStim_direction_directionDict = directionDict[splitted_centralStim_direction]
            [d1] = centralStim_direction_directionDict.split('-')

        stimFound = False
        while stimFound == False:
            if splitted_centralStim_direction == 'X':
                otherStim = centralStim
                stimFound = True
            else:
                otherStim = stims.sample()
                # Split new sampled stim for comparison
                splitted_otherStim_strength = otherStim.iloc[0, 0].split('w')[1].split('.')[0]
                splitted_otherStim_direction = otherStim.iloc[0, 0].split('w')[0]
                stimFound = assignFunc_strength(s1, s2, s3, d1)

        # Fill the cells for correct and wrong answers
        trials_hard.loc[i, v] = otherStim.iloc[0, 0]
        trials_hard.loc[i, w] = otherStim.iloc[0, 0]
        trials_hard.loc[i, x] = otherStim.iloc[0, 0]
        trials_hard.loc[i, y] = centralStim.iloc[0, 0]
        trials_hard.loc[i, z] = otherStim.iloc[0, 0]
        trials_hard.loc[i, a] = otherStim.iloc[0, 0]
        trials_hard.loc[i, b] = otherStim.iloc[0, 0]
        # Save correct answer to real df
        trials_hard.loc[i, 36] = directionDict[splitted_centralStim_direction]

        # Add random fixation cross time
        fixation_cross_time = random.sample([100, 200, 300, 400, 500], 1)
        trials_hard.iloc[i, 32] = fixation_cross_time[0]
        # Add random after response time
        after_response_time = random.sample([600, 700, 800, 900, 1000], 1)
        trials_hard.iloc[i, 33] = after_response_time[0]
        # Add Block Randomization
        trials_hard.iloc[i, 34] = 4
        # Add Block Division
        if i == 59 or i == 119 or i == 179 or i == 239:
            trials_hard.iloc[i, 35] = 1
        else:
            trials_hard.iloc[i, 35] = 0

# Save df as spreadsheet
trials_hard.to_excel('spreadsheetHard_ExecutiveFunction_Anti.xlsx')

