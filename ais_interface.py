#!/usr/bin/env python3

import io
import serial
import datetime

def readAISdata():
  try:
    s = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=2, parity=serial.PARITY_EVEN, rtscts=1)
    AISdata = s.read_until('\\r')
    decodedAISdata = AISdata.decode('utf-8')
    if len(decodedAISdata) > 0:
      nowtime = datetime.datetime.now()
      print(nowtime.strftime('%H:%M:%S.%f')[:-3] + ' , ' + decodedAISdata)
      f = open('AISlogging.csv','a')
      f.write(nowtime.strftime('%H:%M:%S.%f')[:-3] + ',' + decodedAISdata)
      s.flush()
      s.close()
      decodedAISdata = ''
    else:
      s.flush()
      s.close()
  except serial.SerialException:
    s.flush()
    s.close()
    logging.error("Could not open serial port")
    print("Could not open serial port")

while 1:
  readAISdata()
