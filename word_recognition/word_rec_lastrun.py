#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on Tue Mar  9 16:50:14 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'word_rec'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/christinadelta/Desktop/word_recognition/word_rec_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome_screen"
welcome_screenClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome!\nThe experiment will start shortly. \n\nRelax and wait to read the instructions.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instructions_screen"
Instructions_screenClock = core.Clock()
instructions_screen = visual.TextStim(win=win, name='instructions_screen',
    text='Hello and thank you for participating!\nThis is phase 1.\nDuring this phase, at every trial you will be presented with words (nouns) at the center of the screen. Your task is to read the words and maintain them in memory.\nIf you have understood the instructions please press SPACE. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_response = keyboard.Keyboard()

# Initialize components for Routine "blank500ms"
blank500msClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learning_routine"
learning_routineClock = core.Clock()
studyWord = visual.TextStim(win=win, name='studyWord',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank_500 = visual.TextStim(win=win, name='blank_500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learning_phase_end"
learning_phase_endClock = core.Clock()
end_learning_phase = visual.TextStim(win=win, name='end_learning_phase',
    text='This was the learning phase. \n\nThe instrunctions for the test phase will appear shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_screen"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
welcome_screenComponents = [welcome_text]
for thisComponent in welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = welcome_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    if welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_text, 'tStopRefresh')  # time at next scr refresh
            welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_screen"-------
for thisComponent in welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)

# ------Prepare to start Routine "Instructions_screen"-------
continueRoutine = True
# update component parameters for each repeat
instructions_response.keys = []
instructions_response.rt = []
_instructions_response_allKeys = []
# keep track of which components have finished
Instructions_screenComponents = [instructions_screen, instructions_response]
for thisComponent in Instructions_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions_screen"-------
while continueRoutine:
    # get current time
    t = Instructions_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_screen* updates
    if instructions_screen.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_screen.frameNStart = frameN  # exact frame index
        instructions_screen.tStart = t  # local t and not account for scr refresh
        instructions_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_screen, 'tStartRefresh')  # time at next scr refresh
        instructions_screen.setAutoDraw(True)
    
    # *instructions_response* updates
    waitOnFlip = False
    if instructions_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_response.frameNStart = frameN  # exact frame index
        instructions_response.tStart = t  # local t and not account for scr refresh
        instructions_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_response, 'tStartRefresh')  # time at next scr refresh
        instructions_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_response.status == STARTED and not waitOnFlip:
        theseKeys = instructions_response.getKeys(keyList=['space'], waitRelease=False)
        _instructions_response_allKeys.extend(theseKeys)
        if len(_instructions_response_allKeys):
            instructions_response.keys = _instructions_response_allKeys[-1].name  # just the last key pressed
            instructions_response.rt = _instructions_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_screen"-------
for thisComponent in Instructions_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_screen.started', instructions_screen.tStartRefresh)
thisExp.addData('instructions_screen.stopped', instructions_screen.tStopRefresh)
# check responses
if instructions_response.keys in ['', [], None]:  # No response was made
    instructions_response.keys = None
thisExp.addData('instructions_response.keys',instructions_response.keys)
if instructions_response.keys != None:  # we had a response
    thisExp.addData('instructions_response.rt', instructions_response.rt)
thisExp.addData('instructions_response.started', instructions_response.tStartRefresh)
thisExp.addData('instructions_response.stopped', instructions_response.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank500ms"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blank500msComponents = [text]
for thisComponent in blank500msComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank500msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank500ms"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank500msClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank500msClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500msComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank500ms"-------
for thisComponent in blank500msComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
learning_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/word_stimuli.xlsx'),
    seed=None, name='learning_trials')
thisExp.addLoop(learning_trials)  # add the loop to the experiment
thisLearning_trial = learning_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearning_trial.rgb)
if thisLearning_trial != None:
    for paramName in thisLearning_trial:
        exec('{} = thisLearning_trial[paramName]'.format(paramName))

for thisLearning_trial in learning_trials:
    currentLoop = learning_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLearning_trial.rgb)
    if thisLearning_trial != None:
        for paramName in thisLearning_trial:
            exec('{} = thisLearning_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learning_routine"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    studyWord.setText(stimuli)
    # keep track of which components have finished
    learning_routineComponents = [studyWord]
    for thisComponent in learning_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learning_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learning_routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learning_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learning_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *studyWord* updates
        if studyWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            studyWord.frameNStart = frameN  # exact frame index
            studyWord.tStart = t  # local t and not account for scr refresh
            studyWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(studyWord, 'tStartRefresh')  # time at next scr refresh
            studyWord.setAutoDraw(True)
        if studyWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > studyWord.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                studyWord.tStop = t  # not accounting for scr refresh
                studyWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(studyWord, 'tStopRefresh')  # time at next scr refresh
                studyWord.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learning_routine"-------
    for thisComponent in learning_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learning_trials.addData('studyWord.started', studyWord.tStartRefresh)
    learning_trials.addData('studyWord.stopped', studyWord.tStopRefresh)
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank_500]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_500* updates
        if blank_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_500.frameNStart = frameN  # exact frame index
            blank_500.tStart = t  # local t and not account for scr refresh
            blank_500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_500, 'tStartRefresh')  # time at next scr refresh
            blank_500.setAutoDraw(True)
        if blank_500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_500.tStop = t  # not accounting for scr refresh
                blank_500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_500, 'tStopRefresh')  # time at next scr refresh
                blank_500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learning_trials.addData('blank_500.started', blank_500.tStartRefresh)
    learning_trials.addData('blank_500.stopped', blank_500.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'learning_trials'


# ------Prepare to start Routine "learning_phase_end"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
learning_phase_endComponents = [end_learning_phase]
for thisComponent in learning_phase_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learning_phase_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_phase_end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learning_phase_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_phase_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_learning_phase* updates
    if end_learning_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_learning_phase.frameNStart = frameN  # exact frame index
        end_learning_phase.tStart = t  # local t and not account for scr refresh
        end_learning_phase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_learning_phase, 'tStartRefresh')  # time at next scr refresh
        end_learning_phase.setAutoDraw(True)
    if end_learning_phase.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_learning_phase.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            end_learning_phase.tStop = t  # not accounting for scr refresh
            end_learning_phase.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_learning_phase, 'tStopRefresh')  # time at next scr refresh
            end_learning_phase.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_phase_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_phase_end"-------
for thisComponent in learning_phase_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_learning_phase.started', end_learning_phase.tStartRefresh)
thisExp.addData('end_learning_phase.stopped', end_learning_phase.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
