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

from psychopy import prefs
from psychopy import sound, gui, visual, core, data, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
from psychopy.hardware import keyboard
from random import shuffle, choice
import os  # handy system and path functions

# Import task specific details (sounds, counts etc)
from config import (sound_set, sound_files, classes, counts, __version__,
                    soa_time, rest_time, code_length, global_volume,
                    no_parallel)

global_volume = 0.5
sounds = [sound.Sound(sound_files[s_idx], name=s, volume=global_volume)
          for s_idx, s in enumerate(sound_set)]


if no_parallel:
    class PPort():
        def setData(self, code):
            print(f'Sent {code: >3} to parallel port')
    port = PPort()
else:
    port = parallel.ParallelPort(address=0x4FB8)
# Play one sound to init sound card, set port to 0 to stop mnissing code
sounds[0].play()
port.setData(0)
print(sounds[0])

def select_stimuli(types, count_tracker):
    """Select a stimulus match the type from the provided array
    :returns: a dict for the stimulus chosen
    """
    type_index = choice(types)
    count_tracker[type_index] -= 1
    if count_tracker[type_index] == 0:
        del(types[types.index(type_index)])
    return type_index


def get_snd_dict(snd_index):
    """Return a dictionary representing the sound
    """
    return {
        'stim_type': classes[snd_index],
        'sound': snd_index,
        'name': sound_set[snd_index].rpartition('.')[0],
        'base_code': 1 if classes[snd_index] == 'std' else 2
    }


def generate_sequence(sequence_type, block_code):
    """
    For a particular condition, generate a sequence of sounds that fulfills
    the requirements of the condition.

    : A list of dictionaries, each element of the list represents a
    trial in the final block.

    """
    # A sequence is 1 std, followed by a random shuffled array of stds and ssd,
    # where ssd represents three trials - std, std, dev.
    length = sum(counts[sequence_type])  # Total length of block
    num_devs = sum(c for i, c in enumerate(counts[sequence_type])
                   if classes[i] == 'dev')
    # total plain standards = total - first std - number of trials in ssd
    num_stds = length - 1 - num_devs * 3

    sequence = ['std'] * num_stds + ['ssd'] * num_devs
    shuffle(sequence)
    tracker = counts[sequence_type].copy()
    stds = [i for i, c in enumerate(classes) if c == 'std']
    devs = [i for i, c in enumerate(classes) if c == 'dev']
    stimuli_list = []

    # First standard
    idx = select_stimuli(stds, tracker)
    stimuli_list.append(get_snd_dict(idx))

    # All std/sdd's in sequence
    for s in sequence:
        if s == 'std':
            idx = select_stimuli(stds, tracker)
            stimuli_list.append(get_snd_dict(idx))
        elif s == 'ssd':
            idx = select_stimuli(stds, tracker)
            stimuli_list.append(get_snd_dict(idx))
            idx = select_stimuli(stds, tracker)
            stimuli_list.append(get_snd_dict(idx))
            idx = select_stimuli(devs, tracker)
            stimuli_list.append(get_snd_dict(idx))
        else:
            raise RuntimeError('Unexpected sequence value')

    # Adjust special codes (InitStd, Std After Dev)
    for idx, snd in enumerate(stimuli_list):
        stimuli_list[idx].update({'code': 1})

    return stimuli_list


def rest_break():
    """Rest for five minutes and return
    """
    rest = visual.TextStim(
        win=win, name='rest', text='5 minutes rest break', font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, color='white',
        colorSpace='rgb', opacity=None, languageStyle='LTR', depth=0.0
    )
    txt = '5 minutes rest break\n{} seconds remaining'

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(rest_time)
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = [rest]
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
    n_secs = 1

    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *rest* updates
        if rest.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            rest.frameNStart = frameN  # exact frame index
            rest.tStart = t  # local t and not account for scr refresh
            rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
            rest.setAutoDraw(True)
        if rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest.tStartRefresh + n_secs - frameTolerance:
                rest.text = txt.format(rest_time - n_secs)
                n_secs += 1
            if tThisFlipGlobal > rest.tStartRefresh + rest_time - frameTolerance:
                # keep track of stop time/frame for later
                rest.tStop = t  # not accounting for scr refresh
                rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest, 'tStopRefresh')  # time at next scr refresh
                rest.setAutoDraw(False)

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
    thisExp.addData('rest.started', rest.tStartRefresh)
    thisExp.addData('rest.stopped', rest.tStopRefresh)


# Setup (taken from Psychopy generated code and adjusted slightly)
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'  # GC: Check this
expName = 'Mattsen_Study3'
expInfo = {'participant': '', 'group': '1'}
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
    name=expName, version=__version__, extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir, savePickle=True, saveWideText=True,
    dataFileName=filename
)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
# GC: Update for lab
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, winType='pyglet',
    allowGUI=False, allowStencil=False, monitor='testMonitor', color=[0, 0, 0],
    colorSpace='rgb', blendMode='avg', useFBO=True, units='height'
)
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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

if expInfo['group'] == '1':
    blocks = ['hvc', 'lvc', 'break', 'lvc', 'hvc']
    code_adder = [0, 2, 0, 12, 10]
else:
    blocks = ['lvc', 'hvc', 'break', 'hvc', 'lvc']
    code_adder = [4, 6, 0, 26, 24]

for block, adder in zip(blocks, code_adder):
    if block == 'break':
        rest_break()
        continue
    # Otherwise we are in a stimulus delivery block
    display = visual.TextStim(
        win=win, name='block_display', text=block, font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, color='white',
        colorSpace='rgb', opacity=None, languageStyle='LTR', depth=0.0
    )
    display.setAutoDraw(True)
    # refresh the screen
    win.flip()
    # set up handler to look after randomisation of conditions etc
    test_block = data.TrialHandler(
        nReps=1, method='sequential', extraInfo=expInfo, originPath=-1,
        trialList=generate_sequence(block, adder), seed=None, name=block + '_block'
    )
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
        t = trialClock.getTime()
        gt = globalClock.getTime()
        # keep track of which components have finished
        sound = sounds[sound]
        trialComponents = [sound]
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
        sendingCode = False
        routineTimer.add(soa_time)

        # -------Run Routine "trial"-------
        while routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            gt = globalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound
            if sound.status == NOT_STARTED and t >= 0.0:
                # keep track of start time/frame for later
                sound.frameNStart = frameN  # exact frame index
                sound.tStart = t  # local t and not account for scr refresh
                sound.tStartRefresh = tThisFlipGlobal  # on global time
                port.setData(code)
                sound.play()  # start the sound (it finishes automatically)
                sendingCode = True
            if sendingCode and  t >= code_length:
                port.setData(0)
                sendingCode = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()


        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound.stop()  # ensure sound has stopped at end of routine
        test_block.addData('sound.started', sound.tStart)
        test_block.addData('trial.started', gt)
        test_block.addData('block.name', block)
        test_block.addData('port.code', code)

        thisExp.nextEntry()
    display.setAutoDraw(False)


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
