
#import the correct files and registers


#MAP___________________________________________________________________________________________________________________

#generate coordinate system using MAPPING/node_generator.py
#node_generator.py  COMMAND FUNCTION: node_generator(x,y) INPUTS: a1 locations measured by camera
print('Phase 1 MAPPING')
MAP=node_generator

while True
#GPS_______________________________________________________________________________________________________________________________________________________

#check the gps coordinates using RFM69/parsedGPS.py
#parsedGPS.py COMMAND FUNCTION: gpsgo()
print('Phase 2 GPS')
[ROB,PSG,DES]=gpsgo()
print('Passenger Found!')

#CLOSEST NODE___________________________________________________________________________________________________________________
#find closest node information using node finder
END=closest_node(PSG).item(2)
START_DIST=closest_node(ROB).item(0)
#set TOLERANCE greater than motor step
TOL=5
#for start location move robot forward some increment and check GPS and use closest node until we get a start position
while (START_DIST>TOL):
  speakit('straight')
  print readarduino()
  ROB=gpsgo().item(0)
  START_DIST=closest_node(ROB).item(0)
START=closest_node(ROB).item(1)
  

#PATH AND DRIVE INSTRUCTIONS___________________________________________________________________________________________________________________

#use pathfinder algorithm ART_DIST=closest_node(ROB).item(0)for proper driver location Dijkstra
#dijkstra.py COMMAND FUNCTION: pathdata("start","end") INPUTS: ex. pathdata("a1","d2")
print('Phase 3 Path finding')
PATH=pathdata(START,END)

#asses drive instructions per node. Continuous loop to send node case until next node is in range. Then send next node drive instructions. 
#connections.py  COMMAND FUNCTION: connections(directions)
print('Phase 4 connections')
CONNECT=connections(PATH)
INSTRUCT=instruction(CONNECT)
print('Phase 5 node connection drive instructions')
    #Send drive instructions to arduino using i2c communications
    #PIi2c.py  COMMAND FUNCTION: speakpi("hello"), readarduino() 
i=0
while (i<(len(PATH)-1)):
    TARGET = node2cord(CONNECT[1,i])
    if (INSTRUCT[i]=='straight'):
      go_straight(TARGET)
      i+=1
    elif (INSTRUCT[i]=='right'):
      go_right(TARGET)
      i+=1         
    elif (INSTRUCT[i]=='left'):
      go_left(TARGET)
      i+=1
    elif (INSTRUCT[i]=='left_tight'):
      go_left_tight(TARGET)
      i+=1
    else:
      print('final node before passenger reached')
      i+=1

#GET TO PASSENGER_____________________________________________________________________________________________________              
      
#once final node before passenger is achieved run algorithm for Arduino to drive until passenger is found
PSG_LOC=PSG[:-1]
go_straight(PSG_LOC)
#pick up passenger using Lasso commands
speakit('p')
listen()

#DRIVE TO NEXT NODE_____________________________________________________________________________________________________
[ROB,PSG,DES]=gpsgo()
END=closest_node(DES).item(0)
START_DIST=closest_node(ROB).item(0)

#dijkstra to find shortest path
PATH=pathdata(START,END)
CONNECT=connections(PATH)
INSTRUCT=instruction(CONNECT)
#send drive instructions to arudino
i=0
while (i<(len(PATH)-1)):
    TARGET = node2cord(CONNECT[1,i])
    if (INSTRUCT[i]=='straight'):
      go_straight(TARGET)
      i+=1
    elif (INSTRUCT[i]=='right'):
      go_right(TARGET)
      i+=1         
    elif (INSTRUCT[i]=='left'):
      go_left(TARGET)
      i+=1
    elif (INSTRUCT[i]=='left_tight'):
      go_left_tight(TARGET)
      i+=1
    else:
      print('final node before passenger reached')
      i+=1
      
#DRIVE SLOW THROUGH DROP OFF__________________________________________________________________________________________________
#once final node closest to destination is reached. drive and continuous check gps until range value is reached

go_straight(FINAL_DEST)
#drop off passenger using lasso commands
speakit('d')
listen()
print ('passenger eliminated')
NEWPSG=PSG
while (NEWPSG==PSG):
  print('waiting for new passenger location')
  [ROB,PSG2,DES]=gpsgo()
  NEWPSG=PSG2
  
#go back to top of while loop and start next passenger pick up!__________________________________________________________________________________________________




