
"""Flanker task

At each trial, a set of arrows is presented at the center of the
screen and the participant must look at the middle arrow, then press the left arrow key if the middle arrow points the left, and the right arrow key if the middle arrow points the right.


"""

import random
from expyriment import design, control, stimuli
import expyriment
import os

#change your working directory to the place the picture are:
os.chdir('c:\\users\\utilisateur\\desktop\\lilas')

MAX_RESPONSE_DELAY = 2000
LEFT_RESPONSE = 'Left arrow'
RIGHT_RESPONSE = 'Right arrow'
REPETITIONS=8
TRIALS = REPETITIONS*4

exp = design.Experiment(name="Flanker Task", text_size=40)
expyriment.io.defaults.outputfile_time_stamp = False

control.initialize(exp)

pictures = {"lcong": expyriment.stimuli.Picture("left_congruent.png"),"rcong": expyriment.stimuli.Picture("right_congruent.png"),"lincong": expyriment.stimuli.Picture("left_incongruent.png"),"rincong": expyriment.stimuli.Picture("right_incongruent.png")}


cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a set of arrows, your task to decide, as quickly as possible, whether the middle arrow points the left or the right.

    if it points the left, press '{LEFT_RESPONSE}'

    if it points the right, press '{RIGHT_RESPONSE}'

    There will be '{TRIALS}' trials in total.

    Press the space bar to start.""")


exp.add_data_variable_names(['stimulus', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for i in range (0,REPETITIONS):
    #randomize order of stimulus presentation
    #within each repetition of the 4 pictures
    random_pictures={}
    items = list(pictures.items())  # List of tuples of (key,values)
    random.shuffle(items)
    for key, value in items:
        random_pictures[key]=value

    pictures = random_pictures

    for picture in pictures:
        pictures[picture].preload()
        blankscreen.present()
        exp.clock.wait(1000)
        cue.present()
        exp.clock.wait(500)
        pictures[picture].present()
        key, rt = exp.keyboard.wait( duration=MAX_RESPONSE_DELAY)

        exp.data.add([picture,  key, rt])

control.end()
