import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "crao1m"
deviceType = "raspberrypi"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"

a=1
jar=1000
cy_w=14.0
gas_s=['No leak','No leak','No leak','Leak','No leak','No leak']

def func1():
        listOfGlobals = globals()
        listOfGlobals['a'] = 1

def func2():
        listOfGlobals = globals()
        listOfGlobals['a'] = 0

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        print(type(cmd.data))
        i=cmd.data['command']
        if i=='fill':
                func2()
                print("Filling the jar")
        elif i=='stop':
                func1()
                print("Stopped filling the jar")
                                
        
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()


deviceCli.connect()

while True:

        
        
        if a==0 :
               
                if jar=='1000':
                    jar='1000'
                else:
                    jar=int(jar)
                    jar =str(jar+100)
                    jar=(jar.zfill(4))

                if cy_w=='00.0':
                    cy_w='00.0'
                    gas='Empty'
                else:
                    cy_w=float(cy_w)
                    cy_w=str(cy_w-0.5)
                    cy_w=(cy_w.zfill(4))
                    gas=random.choice(gas_s)

                
                #Send Jar capacity,Cylinder weight and Gas status to IBM Watson
                data = { 'Jar_status' : jar, 'Cylinder_weight': cy_w, 'Gas_status': gas }
                #print (data)
                def myOnPublishCallback():
                        print ("Published Jar_status = %s ml" % jar, "Cylinder_weight = %s kg" % cy_w, "Gas_status = %s " % gas, "to IBM Watson")

                success = deviceCli.publishEvent("Weather", "json", data, qos=0, on_publish=myOnPublishCallback)
                if not success:
                        print("Not connected to IoTF")
                time.sleep(10)

                deviceCli.commandCallback = myCommandCallback
        

        elif a==1 :
            
                if jar=='0000':
                    jar='0000'
                else:
                    jar=int(jar)
                    jar =str(jar-100)
                    jar=(jar.zfill(4))

                if cy_w=='00.0':
                    cy_w='00.0'
                    gas='Empty'
                else:
                    cy_w=float(cy_w)
                    cy_w=str(cy_w-0.5)
                    cy_w=(cy_w.zfill(4))
                    gas=random.choice(gas_s)
                    
               
                #Send Jar capacity,Cylinder weight and Gas status to IBM Watson
                data = { 'Jar_status' : jar, 'Cylinder_weight': cy_w, 'Gas_status': gas }
                #print (data)
                def myOnPublishCallback():
                        print ("Published Jar_status = %s ml" % jar, "Cylinder_weight = %s kg" % cy_w, "Gas_status = %s " % gas, "to IBM Watson")
                success = deviceCli.publishEvent("Weather", "json", data, qos=0, on_publish=myOnPublishCallback)
                if not success:
                        print("Not connected to IoTF")
                time.sleep(10)

                deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()

