# Uppsala universty
# Software Engineering and Project Management autumn 2017
# Group L
# Author: Retreived by Henrik Thorsell from user 'mediocrity' on StackOverflow
#         (https://stackoverflow.com/questions/15528939/python-3-timed-input)
#         on 20/9/2017.

import time
from threading import Thread

answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print('Too slow!')

Thread(target = check).start()

answer = raw_input("Input something: ")
if answer == None:
    print('Nothing given.')
else:
    print('Answer given: ' + str(answer))

# An interesting comment from the same page. Could be useful when we're migrating to python 3
# you could use threading. Timer instead of Thread + time.sleep. There is no raw_input in
# Python 3. – jfs Mar 20 '13 at 20:08
