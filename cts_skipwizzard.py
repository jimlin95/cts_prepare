#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os

# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if not p in sys.path:
            sys.path.append(p)
except:
   pass

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

# This must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails.
from com.dtmilano.android.viewclient import ViewClient, View

def skip_setupwizzard(vc):
    # page 1
    vc.findViewById('com.google.android.setupwizard:id/start').touch()
    vc.dump(-1)
    # page 2 (wifi)
    vc.findViewById('com.android.settings:id/custom_button').touch()
    vc.dump(-1)
    # page 2 sub page (wifi)
    vc.findViewById('android:id/button2').touch()
    vc.dump(-1)
    # page 3
    vc.findViewById('com.google.android.setupwizard:id/next_button').touch()
    vc.dump(-1)
    vc.findViewById('com.google.android.setupwizard:id/next_button').touch()
    # page 4
    vc.dump(-1)
    # page 5
    vc.findViewById('com.google.android.setupwizard:id/next_button').touch()
    vc.dump(-1)
    vc.findViewWithText('OK').touch()
    vc.dump(-1)
    vc.findViewWithText('OK').touch()

if __name__ == '__main__':
    os.system("adb devices")
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device=device, serialno=serialno)
    skip_setupwizzard(vc) 
