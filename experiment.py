import os
import sys
import time
import subprocess

file_list = os.listdir("C:\\Users\\Henriette\\Documents\\GitHub\\Foursum\\documentation\\datasmall")

for file in file_list:
    filepath = "C:\\Users\\Henriette\\Documents\\GitHub\\Foursum\\documentation\\datasmall\\"+file
    print(filepath)
    subprocess.call(["python",  "simple.py", "<", filepath], shell=True)
