# the python module initialising security mechansim EN_LICE_ULOCK (ENCRYPTED_LICENCE_UNLOCK)
#-------------------------------------------------------------------------------------------
# COPYRIGHT 2020- 17lwinn

import os
import sys
import logging
from datetime import datetime
from time import *

logging.basicConfig(filename="pyos.log", level=logging.INFO)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def antipiracy():
  logging.warn("[" + current_time + "]" + ": this software utilises the EN_LICE_ULOCK mechanism, which is in all its glory useless")
  sleep(2)
  f = open("LICENSE.txt", "r")
  sleep(2)
  logging.info("[" + current_time + "]" + ": anti-piracy test complete, execution starting...")
  sleep(2)
  logging.error("[" + current_time + "]" + ": if script has not run, then we have detected a bad apple")
  logging.critical("[" + current_time + "]" + ": required file has not been found, please get a copy for the script to run")