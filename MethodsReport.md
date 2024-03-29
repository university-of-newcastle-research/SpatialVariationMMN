---
title: Report on SpatialVariation MMN
authors:
  - name: Gavin Cooper
exports:
  - format: pdf
    template: arxiv_nips
---


# Report on SpatialVariation MMN

This is a report on the work performed for Mattsen Yeark and Juanita Todd for the Spatial Variation MMN task  in 2021.

Covered in this document are aspects of the stimulus generation and task programming.

## Stimulus Generation

The sound stimuli were generated using MATLAB, specifically with a tool I wrote for generating sounds with a particular frequency, combining them into complex sounds and adjusting the phase/timing for ears individually to create the apparent location shift of the sound source.

Some (slightly) more details on the MATLAB package I created and used can be found here: https://github.com/gjcooper/psysound

In terms of the setting for these particular sounds the following lays out how they were created:

#### All Sounds

* The sample frequency was set to 48000, which matches the settings required by the psychtoolbox driver in PsychoPy (previous sounds were at 44100Hz and this seemed to cause the static in the sounds).
* All sounds included a linear ramp on and off to avoid "clicking" due to sudden changes in volume to the sound card. The length of this ramp was set to 0.0005 seconds (half a millisecond)
* All sounds had a bitrate of 16 (16 bits per sample)
* All sounds were scaled to have a maximum amplitude of 90%
* All sounds were created by combining a 300Hz, 600Hz and 1000Hz sound (adding them together and normalising back to 90% amplitude)

#### Variation between sounds

* There were 18 sounds created in total.
* Each sound had two durations created, 50ms and 100ms, the standards in the paradigm corresponding to any 50ms sound and the deviants to the 100ms sounds.
* There were 9 "locations" generated for the rest of the sounds
    * One location was the central position - with no delay to any ear
    * The other 8 locations were delayed by 0.2ms, 0.37ms, 0.5ms and 0.55ms to either the right ear (to create the apparent location shift to the left of the listener) or to the left ear (to shift the location to the right).
    * These delays correspond to an apparent location of $22.5^{\circ}$, $45^{\circ}$, $67^{\circ}$, $90^{\circ}$
    
```{note}
The sound generation script can be found in the main project directory under the filename: soundgen.m
```

## Stimulus Calibration

The stimuli were calibrated using a BRÜEL & KJÆR audiometer by adjusting the volume of the sounds within the task (using a volume parameter for the sound stimulus creation code) and recording the audio level using the audiometer. The main volume control for the PC was set to 75% and should be checked before running the task as the output volume to the participant depends on this setting being stable.

The volume for the stimuli was calibrated to be 75dB

## Task Design

The task consists of two conditions, a High Variance Condition (HVC) and a Low Variance Condition (LVC). Both conditions contain 1440 sounds. As outlined above the sounds were a combination of 3 frequencies (300, 600 and 1000 Hz) and the standards were 50ms duration and deviants 100ms duration. In each block there were 9.375% of the sounds that were deviant, with the rest being standards.

The Stimulus Onset Asynchrony (SOA, the time from the onset of one stimulus to the onset of the next) was set to 0.5 seconds.

The two conditions differed on the apparent locations of the sound stimuli

#### LVC 

The LVC was comprised of sounds played centrally (no time difference between channels) and those with an apparent location of $22.5^{\circ}$ Left and $22.5^{\circ}$ Right. For each of the three locations there were 435 standards (50ms) and 45 deviants (100ms)

#### HVC

The HVC was comprised of sounds played centrally and all other generated sounds, that is for each angle of apparent location ($22.5^{\circ}$, $45^{\circ}$, $67^{\circ}$, $90^{\circ}$) there was a left and a right version with both standards and deviants presented. For reach of the 9 locations there were 145 if standards (50ms) and 15 deviants (100ms).

#### Block Design

Each participant was presented two lots of the previously described conditions, in two distinct orders, with a 5 minute break in the middle of the task.

Participants are allocated into one of two groups with the following condition orders:

* Group 1: HVC, LVC, 5 min break, LVC, HVC
* Group 2: LVC, HVC, 5 min break, HVC, LVC

## Task programming

The task was programmed using the PsychoPy API for stimulus presentation. The PsychoPy version at the time of task development was 2021.1.4. The task is comprised of two python script files, the main task script `SpatialVariationMMN.py` and a script containing configurable elements (`config.py`) such as trial numbers, script version SOA and more. The current version of the script is `0.1.1`

The audio driver used by the study is the [psychtoolbox](http://psychtoolbox.org) driver subset for Python as recommended for audio by PsychoPy.

### Structure of main task

The main task file (`SpatialVariationMMN.py`) follows the following main structure, which borrows heavily from a Builder generated script which was then edited by Gavin Cooper.

* library imports, setting audio driver
* Creation of sounds used in the study from the sound files listed in `config.py`
* Creation of a parallel port for sending codes
* A set of four functions to perform certain tasks:
    * `select_stimuli` Given a list of stimulus types and a dictionary containing counts of that trial type, randomly choose a trial type from the list
    * `get_snd_dict` For a given trial type, return a dictionary containing information about the trial (std/dev status, name of type etc)
    * `generate_sequence` Given either 'hvc' or 'lvc' will generate a sequence of trials matching the condition requirements, plus enforcing a minimum of 2 standards between deviants and a minimum of 3 standards at the start of the block, as well as initial standard and standard after deviant codes.
    * `rest_break` Presents a rest break with a count down of the seconds remaining.
* Gather information about the participant and the environment
* Create a handler for storing and saving data, and a logger for logging problems
* Create a display window for presenting visual information, clocks for timing and a keyboard for quitting the task.
* Create the block structure for each group.
* Loop through each block and:
    * If a rest block, run the rest_break function
    * Otherwise display what block we are in on the screen and then loop through each trial and:
        * Setup each trial
        * Present the sound
        * Send the port code
* Finally save the data to the output file

## Final notes

If you wish to reference PsychoPy in publications you will probably want to use the following article:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y
