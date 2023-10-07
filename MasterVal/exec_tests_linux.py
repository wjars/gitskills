#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

import copy
import os
import random
import sys
import re
import time
import datetime

sys.path.append(os.path.abspath(f'lib{os.sep}Generic{os.sep}wcwidth'))

g_ReportOn = False


SOF = False
REPORT_DIR = '/data/testLog'

python_pathList = [
    os.path.dirname(__file__)
]

sep = ";"
python_path = sep.join(python_pathList)
os.environ["PYTHONPATH"] = python_path


def main():
    err = 0
    global cliList
    cliList = []
    count = 0

    argvCopy = copy.copy(sys.argv)
    for arg in argvCopy:
        if arg.find("=") >= 0:
            cliList.append(arg)
            sys.argv.pop(count)
            continue
        count += 1

    for arg in sys.argv:
        err += Build_TestList(arg)

    if err:
        print("ERROR: Unable to build TestList")
        return 1

    run_test()
    return 0


def run_test():
    failCount = 0
    passCount = 0
    totalExecTime = 0

    fname_TTtime = setup_report()
    if fname_TTtime is not None:
        print("\nLog File Name: ", fname_TTtime)

    arg = ""
    for inArg in cliList:
        if inArg.split('=')[0] in arg:
            arg = re.sub(r'{0}.*?\s' .format(inArg.split('=')[0]), inArg + " ", arg)
        else:
            arg = arg + " " + inArg

    startTime = datetime.datetime.now()
    for tst in g_TestList:
        if SOF:
            mode = 'SOF'
        else:
            mode = 'TTE'

        if tst.split()[0].endswith('py'):
            print("Running test: ", tst)

            testResult = 'PASS'
            if ' '.join(cliList).find('logFileName') == -1:
                timeStr = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
                logFileName = os.path.split(tst.split('.py')[0])[1] + "_" + timeStr + '.log'
                driverLogName = logFileName.split('.')[0] + '_Driver.log'
                argList = arg.split(' ')
                for a in argList:
                    if 'logFileName' in a:
                        argList.remove(a)
                        break

                argList.append(f'--logFileName={logFileName}')
                arg = ' '.join(argList)

            cmd = 'python -u   '
            cmd += tst
            cmd += arg
            print("_________________NEW TEST________________", tst)

            timeStart = time.perf_counter()
            sys.stdout.flush()

            retValue = os.system(cmd)

            sys.stdout.flush()
            timeStop = time.perf_counter()
            executeTime = round((timeStop - timeStart), 3)
            totalExecTime += executeTime

            if retValue != 0:
                testResult = "FAIL"
                failCount += 1
            else:
                if os.path.exists(os.path.join(REPORT_DIR, logFileName)):
                    os.remove(os.path.join(REPORT_DIR, logFileName))
                if os.path.exists(os.path.join(REPORT_DIR, driverLogName)):
                    os.remove(os.path.join(REPORT_DIR, driverLogName))

                passCount += 1

            if fname_TTtime is not None:
                endTime = datetime.datetime.now()
                elapsedTime = (endTime - startTime).days * 1440 + (endTime - startTime).seconds // 68
                info = ['None', 'None', 'MTK', str(startTime), str(endTime), str(elapsedTime) + 'Min']

            if mode == "SOF" and retValue != 0:
                break
        else:
            print("ERROR: non python test request test - ", tst)

    if fname_TTtime != None:
        msgTTtime = "\nTest Summary:\nTotal {0} cases, Passed {1}, Failed {2}, Total Test Time {3}s\n" .format(
            len(g_TestList), passCount, failCount, round(totalExecTime, 3))
        print(msgTTtime)
        with open(fname_TTtime, 'ab', 0) as logtimefp:
            logtimefp.write(msgTTtime.encode())

"""
    @Descriptor:
        Bulid test List XXX.ini Test path
"""
def Build_TestList(arg):

    global g_TestList
    g_TestList = []

    try:
        if os.path.isdir(arg):
            for root, dirs, files in os.walk(os.path.abspath(arg)):
                for name in files:
                    if name.endswith('py') and name != "__init__.py":
                        g_TestList.append(os.path.join(root, name))
    except:
        pass

    if g_TestList:
        random.shuffle(g_TestList)
        print(f'total {len(g_TestList)} in {arg}')
        if arg[-1] != os.sep:
            g_TestList = random.sample(g_TestList, random.randint(len(g_TestList) // 5, len(g_TestList)))
        with open('simutestlist.ini', 'w+') as f:
            for t in g_TestList:
                f.write(t+'\n')
                print(t)
        print(f'select {len(g_TestList)} in {arg}')
        return 0

    if arg.endswith('py'):
        g_TestList.append(arg)
        return 0

    with open(arg, 'r') as disk:
        for line in disk:
            validItem = []

            line = line.rsplit('\r\n')
            if len(line) < 1 or line[0] == '#':
                continue
            chunk = line[0].split()
            for item in chunk:
                if item.startswith('#'):
                    break
                item = item.replace('\\', '/')
                validItem.append(item)
            validCase = ' '.join(validItem)
            g_TestList.append(validCase)
    return 0


def setup_report():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    fname_TTtime = REPORT_DIR + "/3720_" + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + "_Test_Report.txt"

    return fname_TTtime


if __name__ == "__main__":
    exit(main())
