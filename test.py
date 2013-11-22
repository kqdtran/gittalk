#!/usr/bin/env python

import sys
import subprocess
import pyttsx as px

engine = px.init()

def say(text='This is so cool', rate_adjust=-30, volume_adjust=0):
    '''
    Says an English text, with any adjust rate and/or volume
    '''
    # Adjusts the property
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+rate_adjust)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume-volume_adjust)

    # Says the text and voila!
    engine.say(text)
    engine.runAndWait()

def say_last_commit():
    line = subprocess.check_output(["git", "log", "-1",
                                    "HEAD", "--pretty=format:%s"])
    say(line)

if __name__ == '__main__':
    say_last_commit()
    