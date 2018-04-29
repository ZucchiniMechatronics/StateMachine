
#import the correct files and registers



#generate coordinate system using MAPPING/node_generator.py
#node_generator.py  COMMAND FUNCTION: node_generator(x,y) INPUTS: a1 locations measured by camera
print('Phase 1 MAPPING')
MAP=node_generator

#check the gps coordinates using RFM69/parsedGPS.py
#parsedGPS.py COMMAND FUNCTION: gpsgo()
print(Phase 2 GPS')
[ROB,PSG,DES]=gpsgo()


#find closest node information using node finder



#use pathfinder algorithm for proper driver location Dijkstra
#dijkstra.py COMMAND FUNCTION: pathdata("start","end") INPUTS: ex. pathdata("a1","d2")
print('Phase 3 Path finding')
PATH=pathdata(start,end)

#asses drive instructions per node. Continuous loop to send node case until next node is in range. Then send next node drive instructions. 
#connections.py  COMMAND FUNCTION: connections(directions)
print('Phase 4 connections')
CONNECT=connections(PATH)

print('Phase 5
i=0
  while (i<(len(PATH)-1)):
    PING=gpsgo()
    ROB=PING[1] 
    
    #calculates drive instructions
    drive_instruct=instruction(CONNECT[i])
    #Send drive instructions to arduino using i2c communications
    #PIi2c.py  COMMAND FUNCTION: speakpi("hello"), readarduino() 
    speakpi(drive_instruct)
    
#once final node before passenger is achieved run algorithm for Arduino to drive until passenger is found



#pick up passenger using Lasso commands


#drive to closest node


#dijkstra to find shortest path


#send drive instructions to arudino


#once final node closes to destination is reached. drive and continuous check gps until range value is reached


#drop off passenger using lasso commands


#check RFM for new coordinates.  repeat all





