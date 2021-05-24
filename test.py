#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by Gavin Cooper for Juanita Todd and Mattsen Yeark
    on May 18, 2021, at 22:35
This experiment was created with the assistance of the PsychoPy3 Experiment
Builder (v2021.1.4),
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import sound, gui, visual, core, data, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
import os  # handy system and path functions

from psychopy.hardware import keyboard

import config

sound_set = [
    'Central_100ms.wav', 'Central_50ms.wav', 'left_22.5deg_100ms.wav',
    'left_22.5deg_50ms.wav', 'left_45deg_100ms.wav', 'left_45deg_50ms.wav',
    'left_67deg_100ms.wav', 'left_67deg_50ms.wav', 'left_90deg_100ms.wav',
    'left_90deg_50ms.wav', 'right_22.5deg_100ms.wav', 'right_22.5deg_50ms.wav',
    'right_45deg_100ms.wav', 'right_45deg_50ms.wav', 'right_67deg_100ms.wav',
    'right_67deg_50ms.wav', 'right_90deg_100ms.wav', 'right_90deg_50ms.wav'
]
sound_files = ['stimuli/' + s for s in sound_set]
sounds = [sound.Sound(sound_files[s_idx], name=s)
          for s_idx, s in enumerate(sound_set)]
classes = ['std' if '50ms' in s else 'dev' for s in sound_set]
hvc_counts = [145 if c == 'std' else 15 for c in classes]
lvc_counts = [263 if c == 'std' else 25 for c in classes]
for idx, snd in enumerate(sound_set):
    if '67deg' in snd or '90deg' in snd:
        lvc_counts[idx] = 0
hvc_list = []
for idx, snd in enumerate(sounds):
    hvc_list += hvc_counts[idx] * [{
        'stim_type': classes[idx],
        'sound': snd,
        'name': sound_set[idx].split('.')[0]
    }]


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'  # GC: Check this
expName = 'Mattsen_Study3'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if not dlg.OK:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(
    name=expName, version=config._version,
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir,  # GC: update
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
# GC: Update for lab
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
SOA = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='SOA')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# set up handler to look after randomisation of conditions etc
test_block = data.TrialHandler(
    nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=hvc_list,
    seed=None, name='test_block')
thisExp.addLoop(test_block)  # add the loop to the experiment
thisTrial = test_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial is not None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in test_block:
    currentLoop = test_block
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial is not None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # keep track of which components have finished
    trialComponents = [sound, SOA]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound
        if sound.status == NOT_STARTED and t >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            sound.frameNStart = frameN  # exact frame index
            sound.tStart = t  # local t and not account for scr refresh
            sound.tStartRefresh = tThisFlipGlobal  # on global time
            sound.play()  # start the sound (it finishes automatically)
        # *SOA* period
        if SOA.status == NOT_STARTED and t >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            SOA.frameNStart = frameN  # exact frame index
            SOA.tStart = t  # local t and not account for scr refresh
            SOA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SOA, 'tStartRefresh')  # time at next scr refresh
            SOA.start(0.5)
        elif SOA.status == STARTED:  # one frame should pass before updating params and completing
            SOA.complete()  # finish the static period
            SOA.tStop = SOA.tStart + 0.5  # record stop time

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound.stop()  # ensure sound has stopped at end of routine
    test_block.addData('sound.started', sound.tStart)
    test_block.addData('sound.stopped', sound.tStop)
    test_block.addData('SOA.started', SOA.tStart)
    test_block.addData('SOA.stopped', SOA.tStop)

    routineTimer.reset()
    thisExp.nextEntry()

# completed 100.0 repeats of 'test_block'


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
