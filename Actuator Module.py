#!/usr/bin/env python
# coding: utf-8

# In[17]:


# this imports required packages
import serial
import serial.tools.list_ports

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


# In[18]:


# runs our function and defines a variable as the port named 'prolific'
port=port_authority()
# baud rate is 9600, timeout is 1 second
ser = serial.Serial(port,9600,timeout=1)


# In[19]:


while True:
    t = input("Command: ")+'\n'
    # escapes the loop if the word "break" is found anywhere
    if "break" in t:
        break
    # writes encoded string
    ser.write(t.encode('utf-8'))
        # reads output, then prints and decodes it. Replaces carrage return character with new line character
    out = ser.readline()
    print(out.decode('utf-8').replace('\r','\n'))


# In[21]:


ser.close()


# In[ ]:




