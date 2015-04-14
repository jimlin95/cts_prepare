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
from com.dtmilano.android.viewclient import ViewClient, View, UiDevice 
from cts_chanagelanguage import changeLanguage
from cts_develop import ChangeDeveloper_settings
from cts_setsecurity import setSecurity
from cts_settimezone import setTimezone
from cts_wifisetting import SetWifiConnect,ModifyNetwork
from cts_skipwizzard import skip_setupwizzard


os.system("adb devices")
device, serialno = ViewClient.connectToDeviceOrExit()
# Connect to device with the IP received as a parameter
device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device=device, serialno=serialno)
ud = UiDevice(vc=vc)
skip_setupwizzard(vc)
# Press the HOME button to start the test from the home screen
device.press('KEYCODE_HOME','DOWN_AND_UP')

#Change language to English (United States)
changeLanguage(ud,'en')
ChangeDeveloper_settings(device,vc)
setSecurity(device,vc)
setTimezone(device,vc)
SetWifiConnect(device,vc)
ModifyNetwork(device,vc)
# Press the HOME button to start the test from the home screen
device.press('KEYCODE_HOME','DOWN_AND_UP')
