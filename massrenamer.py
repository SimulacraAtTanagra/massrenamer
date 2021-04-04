# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:18:54 2020

@author: shane
"""

from src.pdftsrename import tsrename as ts
import os

def rename_all(directory_in_str):
    directory = os.fsencode(directory_in_str)           #defines directory as indicated string
    os.chdir(directory)                                 #navigate to directory specified
    for itera,file in enumerate(os.listdir(directory)):                  #iterates over all the files here
        filename = os.fsdecode(file)                    #specifies filename from file
        if filename.endswith(".pdf") and filename.contains('Crystal'):                  #isolates epub for further action
            x=ts(directory_in_str,filename)
            if "2020" not in x or "2019" not in x:
                pass
            else:
                source=f'{directory_in_str}\\{filename}'
                dest=f'{directory_in_str}\\{x}'
                os.rename(source,dest)