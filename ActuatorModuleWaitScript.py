#!/usr/bin/env python
# coding: utf-8

# In[105]:


# required packages
import serial
import serial.tools.list_ports
import time

# defines a function that gets devices plugged into serial ports
# if one's name is 'port authority', we set that port 
def port_authority():
    ports = list(serial.tools.list_ports.comports())
    # this list is 2D
    for p in ports:
        # basically, if it says 'prolific' in the right side
        # give us the name of the port (on the left side)
       if "Prolific" in p[1]:
          return p[0]


# In[106]:


# runs our function and defines a variable as the port named 'prolific'
port=port_authority()
# baud rate is 9600, timeout is 1 second
ser = serial.Serial(port,9600,timeout=0.5)


# In[107]:


# defines all useful functions

def wait(i):
    t = int(i)
    time.sleep(t)

def start():
    ser.write(b'*GOA\n')
    start_time = time.perf_counter()
    print("Starting Run")
    return start_time


def Rinse30(st):
    ser.write(b'2GOB\n')
    print("Rinsing...")
    wait(30)
    current_time = time.perf_counter()
    output_time = current_time - st
    print("Rinsed! Current time: " + str(output_time))



def Rinse45(st):
    ser.write(b'1GOA\n')
    print("Rinsing...")
    wait(45)
    current_time = time.perf_counter()
    output_time = current_time - st
    print("Rinsed! Current time: " + str(output_time))



def Load(st,i):
    t = int(i)
    ser.write(b'*GOB\n')
    print("Loading...")
    wait(t)
    current_time = time.perf_counter()
    output_time = current_time - st
    print("Loaded! Current time: " + str(output_time))


def Elute(st):
    ser.write(b'*GOA\n')
    print("Eluting...")
    wait(240)
    current_time = time.perf_counter()
    output_time = current_time - st
    print("Eluted! Time elapsed: " + str(output_time))
    print("Ready for next run.")


# In[108]:


print("Make sure both valves are at A.")
# gets the load time from user input
i = input("Desired Load Time? (seconds): ")
r = int(i)
start_time = 0


# makes sure all valves are at position A
start_time = start()

# rinse for 30 seconds
Rinse30(start_time)

# load for t seconds (t is user defined time)
Load(start_time,r)

# rinse for 45 seconds
Rinse45(start_time)

# elute for 4 mintues
Elute(start_time)


# In[109]:


# we have to close the connection so it doesn't throw an error when we rerun the script
ser.close()


# In[ ]:




