#!/usr/bin/python
import pyupm_grove as grove
import paho.mqtt.client as paho
import psutil
import signal
import sys
import time

from threading import Thread

def functionDataActuator():
    print "Data Actuator"

//info del dato de red 
def functionDataSensor():
    #netdata = psutil.net_io_counters()
    #data = netdata.packets_sent + netdata.packets_recv
    # Create the light sensor object using AIO pin 0
light = grove.GroveLight(0)

# Read the input and print both the raw value and a rough lux value,
# waiting one second between readings
while 1:
    print light.name() + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux";
    time.sleep(1)

# Delete the light sensor object
del light
    return data

def functionDataSensorMqttOnPublish(mosq, obj, msg):
    print "Data Sensor Mqtt Published!"

def functionDataSensorMqttPublish():
    mqttclient = paho.Client()
    mqttclient.on_publish = functionDataSensorMqttOnPublish
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    while True:
        data = functionDataSensor()
        topic = "IoT101/DataSensor"
        mqttclient.publish(topic, data)
        time.sleep(1)

def functionSignalHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, functionSignalHandler)

    threadmqttpublish = Thread(target=functionDataSensorMqttPublish)
    threadmqttpublish.start()

    while True:
        print "Hello Internet of Things 101"
        print "Data Sensor: %s " % functionDataSensor()
        time.sleep(5)

# End of File
