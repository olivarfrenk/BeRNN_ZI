import pandas as pd
import os
import random

# Direct to project file
# os.getcwd()
os.chdir('./Executive Function Anti')

stims = pd.DataFrame(['Uw0_25.png', 'Dw0_25.png', 'Lw0_25.png', 'Rw0_25.png',\
                      'Uw0_5.png', 'Dw0_5.png', 'Lw0_5.png', 'Rw0_5.png',\
                      'Uw0_75.png', 'Dw0_75.png', 'Lw0_75.png', 'Rw0_75.png',\
                      'Uw1_0.png', 'Dw1_0.png', 'Lw1_0.png', 'Rw1_0.png'])


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

for displays in range(8):
    # select rangeList according to display
    if displays == 0: # Display 1
        rangeList = [0, 30]
        [x,y,z] = [30,0,2]
    elif displays == 1: # Display 2
        rangeList = [30, 60]
        [x,y,z] = [31,1,3]
    elif displays == 2: # Display 1
        rangeList = [60, 90]
        [x,y,z] = [6,8,10]
    elif displays == 3: # Display 2
        rangeList = [90, 120]
        [x,y,z] = [7,9,11]
    elif displays == 4: # Display 1
        rangeList = [120, 150]
        [x,y,z] = [14,16,18]
    elif displays == 5: # Display 2
        rangeList = [150, 180]
        [x,y,z] = [15,17,19]
    elif displays == 6: # Display 1
        rangeList = [180, 210]
        [x, y, z] = [22, 24, 26]
    else: # Display 2
        rangeList = [210, 240]
        [x, y, z] = [23, 25, 27]

    for i in range(rangeList[0],rangeList[1]):
        # Randomly choose a stim from general stimulus pool
        centralStim = stims.sample()
        splitted_centralStim_direction = centralStim.iloc[0, 0].split('w')[0]

        ratio_list = [1, 2, 3, 4]
        ratio = random.sample(ratio_list, 1)

        if ratio[0] == 1:
            otherStim = 'XwX.png'
            splitted_centralStim_direction = 'X'
        else:
            otherStim = stims.sample().iloc[0, 0]

        # Fill the cells for correct and wrong answers
        trials_easy.loc[i, x] = otherStim
        trials_easy.loc[i, y] = centralStim.iloc[0, 0]
        trials_easy.loc[i, z] = otherStim
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
trials_easy.to_excel('EF_Anti_easy.xlsx')


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

for displays in range(8):
    # select rangeList according to display
    if displays == 0: # Display 1
        rangeList = [0, 30]
        [w,x,y,z,a] = [28,30,0,2,4]
    elif displays == 1: # Display 2
        rangeList = [30, 60]
        [w,x,y,z,a] = [29,31,1,3,5]
    elif displays == 2: # Display 1
        rangeList = [60, 90]
        [w,x,y,z,a] = [4,6,8,10,12]
    elif displays == 3: # Display 2
        rangeList = [90, 120]
        [w,x,y,z,a] = [5,7,9,11,13]
    elif displays == 4: # Display 1
        rangeList = [120, 150]
        [w,x,y,z,a] = [12,14,16,18,20]
    elif displays == 5: # Display 2
        rangeList = [150, 180]
        [w,x,y,z,a] = [13,15,17,19,21]
    elif displays == 6: # Display 1
        rangeList = [180, 210]
        [w,x,y,z,a] = [20,22,24,26,28]
    else: # Display 2
        rangeList = [210, 240]
        [w,x,y,z,a] = [21,23,25,27,29]

    for i in range(rangeList[0],rangeList[1]):
        # Randomly choose a stim from general stimulus pool
        centralStim = stims.sample()
        splitted_centralStim_direction = centralStim.iloc[0, 0].split('w')[0]

        ratio_list = [1, 2, 3, 4]
        ratio = random.sample(ratio_list, 1)
        stimFound = False
        while stimFound == False:
            if ratio[0] == 1:
                otherStim = 'XwX.png'
                splitted_centralStim_direction = 'X'
                stimFound = True
            else:
                splitted_centralStim_strength = centralStim.iloc[0, 0].split('w')[1].split('.')[0]
                # colors to look for w.r.t. central Stim
                centralStim_strength_strengthDict = strengthDict[splitted_centralStim_strength]
                [s1, s2, s3] = centralStim_strength_strengthDict.split('-')

                otherStim = stims.sample().iloc[0, 0]
                # Split new sampled stim for comparison
                splitted_otherStim_strength = otherStim.split('w')[1].split('.')[0]
                stimFound = assignFunc_strength(s1, s2, s3)

        # Fill the cells for correct and wrong answers
        trials_normal.loc[i, w] = otherStim
        trials_normal.loc[i, x] = otherStim
        trials_normal.loc[i, y] = centralStim.iloc[0, 0]
        trials_normal.loc[i, z] = otherStim
        trials_normal.loc[i, a] = otherStim
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
trials_normal.to_excel('EF_Anti_normal.xlsx')


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

for displays in range(8):
    # select rangeList according to display
    if displays == 0: # Display 1
        rangeList = [0, 30]
        [v,w,x,y,z,a,b] = [26,28,30,0,2,4,6]
    elif displays == 1: # Display 2
        rangeList = [30, 60]
        [v,w,x,y,z,a,b] = [27,29,31,1,3,5,7]
    elif displays == 2: # Display 1
        rangeList = [60, 90]
        [v,w,x,y,z,a,b] = [2,4,6,8,10,12,14]
    elif displays == 3: # Display 2
        rangeList = [90, 120]
        [v,w,x,y,z,a,b] = [3,5,7,9,11,13,15]
    elif displays == 4: # Display 1
        rangeList = [120, 150]
        [v,w,x,y,z,a,b] = [10,12,14,16,18,20,22]
    elif displays == 5: # Display 2
        rangeList = [150, 180]
        [v,w,x,y,z,a,b] = [11,13,15,17,19,21,23]
    elif displays == 6: # Display 1
        rangeList = [180, 210]
        [v,w,x,y,z,a,b] = [18,20,22,24,26,28,30]
    else: # Display 2
        rangeList = [210, 240]
        [v,w,x,y,z,a,b] = [19,21,23,25,27,29,31]

    for i in range(rangeList[0],rangeList[1]):
        # Randomly choose a stim from general stimulus pool
        centralStim = stims.sample()
        splitted_centralStim_direction = centralStim.iloc[0, 0].split('w')[0]

        ratio_list = [1, 2, 3, 4]
        ratio = random.sample(ratio_list, 1)
        stimFound = False
        while stimFound == False:
            if ratio[0] == 1:
                otherStim = 'XwX.png'
                splitted_centralStim_direction = 'X'
                stimFound = True
            else:
                splitted_centralStim_strength = centralStim.iloc[0, 0].split('w')[1].split('.')[0]
                # colors to look for w.r.t. central Stim
                centralStim_strength_strengthDict = strengthDict[splitted_centralStim_strength]
                [s1, s2, s3] = centralStim_strength_strengthDict.split('-')
                # direction to look for w.r.t. central Stim
                centralStim_direction_directionDict = directionDict[splitted_centralStim_direction]
                [d1] = centralStim_direction_directionDict.split('-')

                otherStim = stims.sample().iloc[0, 0]
                # Split new sampled stim for comparison
                splitted_otherStim_strength = otherStim.split('w')[1].split('.')[0]
                splitted_otherStim_direction = otherStim.split('w')[0]
                stimFound = assignFunc_strength(s1, s2, s3, d1)

        # Fill the cells for correct and wrong answers
        trials_hard.loc[i, v] = otherStim
        trials_hard.loc[i, w] = otherStim
        trials_hard.loc[i, x] = otherStim
        trials_hard.loc[i, y] = centralStim.iloc[0, 0]
        trials_hard.loc[i, z] = otherStim
        trials_hard.loc[i, a] = otherStim
        trials_hard.loc[i, b] = otherStim
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
trials_hard.to_excel('EF_Anti_hard.xlsx')

