# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:44:26 2023

@author: lab
"""
import os
import shutil
print("Exercise 7 solution.")
print("Clear the clutter")

def copyFolder():
    # Source and destination
    src = 'C:\\Users\\lab\\Desktop\\wallpaper'
    dst = 'C:\\Users\\lab\\Desktop\\new dst'
        # Copy File
    # cmd = f'copy "{src}" "dst"'
    # os.system(cmd)
    
    # understand join as 'If dst is C:\Users\lab\Desktop\new dst, this line creates dst_file as C:\Users\lab\Desktop\new dst\image.jpg.'
    for filename in os.listdir(src):
        src_file = os.path.join(src, filename)
        dst_file = os.path.join(dst, filename)
        shutil.copy2(src_file, dst_file)
        
def changeFilesName():
    i = 1
    src = "C:\\Users\\lab\\Desktop\\new dst"
    for file_name in os.listdir(src):
        if file_name.endswith(".png"):
            src_file = os.path.join(src, file_name)
            new_file = os.path.join(src, f"Image{i}.jpg")
            os.rename(src_file, new_file)
            i+=1
        # print(file_name)
    print("misson accomplished? yes!")
            
changeFilesName()

            


