import os

os.chdir ("C:\Users\Utente\Desktop\git_clone\Python4ScientificComputing_Fundamentals\Assignment 4")

import wallCalculations_Martinelli as WC

layers_wall_series = ["gypsiumWallboard_13mm","commonBrick_100mm","woodFiberboard_13mm","WoodBevelLappedSiding"]
layers_wall_par = ["glassFiberInsulation_90mm","woodStud_38x90mm"]
layers_door = ["wood_50mm"]
#layers_roof = ["wood_50mm","urethaneRigidFoam_90mm","AsphaltShingleRoofing"]

U_roof_win = 0.25

results_wall = WC.wallCalc_withParallel(layers_wall_series,layers_wall_par,0.7)
results_door = WC.wallCalc_onlyInSeries(layers_door)
#results_roof = WC.wallCalc_onlyInSeries(layers_roof)  #the value of U is given by the example, this can be used if U is not given and the layers are given in a list

U_wall_sum = results_wall["Utot_sum"]
U_wall_win = results_wall["Utot_win"]
U_door_sum = results_door["Utot_sum"]
U_door_win = results_door["Utot_win"]
#U_roof_sum = results_roof["Utot_sum"]   #the value of U is given by the example, same as before
#U_roof_win = results_roof["Utot_win"]   #the value of U is given by the example, same as before

print "the U value of the wall in summer is " + str(U_wall_sum) +" W/(m2 degC)"
print "the U value of the wall in winter is " + str(U_wall_win) +" W/(m2 degC)"

print "the U value of the door in summer is " + str(U_door_sum) +" W/(m2 degC)"
print "the U value of the door in winter is " + str(U_door_win) +" W/(m2 degC)"

print "The U value of the roof is " + str(U_roof_win) +" W/(m2 degC)"
print " "

Tin = 20
Tout = -4.8
deltaT_heating = Tin - Tout

#from now on heating only

HF_wall = U_wall_win*deltaT_heating
HF_door = U_door_win*deltaT_heating
HF_roof = U_roof_win*deltaT_heating

L1 = 10
L2 = 20
H = 2.4
L_d = 1
H_d = 2.2
A_fin = 3.0*4.0*1.8 + 8.0*1.8

Adoor = L_d*H_d
Awall = (L1+L2)*2.0*H - A_fin - Adoor
Aroof = L1*L2

Qwall = HF_wall*Awall
Qdoor = HF_door*Adoor
Qroof = HF_roof*Aroof

Qtot = Qwall + Qdoor + Qroof

print "The heating load of the walls is " + str(Qwall) + " (W)"
print " "
print "The heating load of the door is " + str(Qdoor) + " (W)"
print " "
print "The heating load of the roof is " + str(Qroof) + " (W)"
print " "
print "The total heating load of the opaque surfaces of the house is " + str(Qtot) + " (W)"
