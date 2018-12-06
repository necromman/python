import os, sys
from win32com.client import GetObject

# pip install pywin32 / pip install pypiwin32
def getProcessesList():
    PROCESSES_LIST_ = []
    getobj_ = GetObject('winmgmts:')
    processed_ = getobj_.InstancesOf('Win32_Process')
    for ps_ in processed_:
        PROCESSES_LIST_.append(ps_.Properties_('Name').Value)
    for i in PROCESSES_LIST_:
        print(i)
    return PROCESSES_LIST_

getProcessesList()