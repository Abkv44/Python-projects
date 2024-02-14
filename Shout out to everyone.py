# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:52:36 2024

@author: Abk
"""

import win32com.client
import itertools

print("Shout out to every one!")

names = ["Abhishek", "Verma", "Shek", "AK is ok"]
shoutout = ["Shout out to "]

ns = list(itertools.product(shoutout, names))
speaker = win32com.client.Dispatch("SAPI.SpVoice")
print(ns)

for name in ns:
    string = "Shout out to"
    speaker.Speak(name) 


  