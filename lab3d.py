#!/usr/bin/env python3
# Author ID: ykudo

import os
import subprocess


#dfcmd = "df -h | grep '/$' | awk '{print $4}'"

#p = subprocess.Popen(dfcmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

#fs = p.communicate()

#stdout = fs[0].decode('utf-8').strip()

#print(stdout)

def free_space():
    dfcmd = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(dfcmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    fs = p.communicate()
    stdout = fs[0].decode('utf-8').strip()
    return stdout

print(free_space())


