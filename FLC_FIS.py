# Import Library
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define Variables
x_DError = np.arange(0, 100, 1) #Delta Error (RPM)
x_Error = np.arange(0, 1000, 1) #Error (RPM)
x_Speed = np.arange(0, 5000, 1) #Speed of motor (RPM)
x_Incremental = np.arange(0, 100, 1) #Incremental Error (RPM)

# Determining Range
DError_SM = fuzz.trimf(x_DError, [0, 15, 30]) #Small
DError_IM = fuzz.trimf(x_DError, [20, 35, 50]) #Intermediate
DError_LG = fuzz.trimf(x_DError, [40, 55, 70]) #Large
DError_VG = fuzz.trimf(x_DError, [60, 75, 90]) #Very Large

Error_LE = fuzz.trapmf(x_Error, [0, 100, 200, 300]) #Little
Error_ME = fuzz.trapmf(x_Error, [200, 300, 400, 500]) #Middle
Error_BE = fuzz.trapmf(x_Error, [400, 500, 600, 700]) #Big
Error_VE = fuzz.trapmf(x_Error, [600, 700, 800, 900]) #Very Error

Speed_LW  = fuzz.trimf(x_Speed, [1000,1000,1000]) #Low
Speed_MD  = fuzz.trimf(x_Speed, [2000,2000,2000]) #Medium
Speed_HG  = fuzz.trimf(x_Speed, [3000,3000,3000]) #High
Speed_VH  = fuzz.trimf(x_Speed, [4000,4000,4000]) #Very High

Incremental_SM = fuzz.trimf(x_Incremental, [0, 15, 30])  # Small
Incremental_IM = fuzz.trimf(x_Incremental, [20, 35, 50])  # Intermediate
Incremental_LG = fuzz.trimf(x_Incremental, [40, 55, 70])  # Large
Incremental_VL = fuzz.trimf(x_Incremental, [60, 75, 90])  # Very Large

# Create Fuzzy Set Graphs
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(6,9))

ax0.plot(x_DError, DError_SM, 'g', linewidth=1.5, label='Small')
ax0.plot(x_DError, DError_IM, 'b', linewidth=1.5, label='Intermediate')
ax0.plot(x_DError, DError_LG, 'r', linewidth=1.5, label='Large')
ax0.plot(x_DError, DError_VG, 'y', linewidth=1.5, label='Very Large')

ax0.set_title('Delta Error')
ax0.legend()

ax1.plot(x_Error, Error_LE, 'g', linewidth=1.5, label='Little')
ax1.plot(x_Error, Error_ME, 'b', linewidth=1.5, label='Middle')
ax1.plot(x_Error, Error_BE, 'r', linewidth=1.5, label='Big')
ax1.plot(x_Error, Error_VE, 'y', linewidth=1.5, label='Very Big')

ax1.set_title('Error')
ax1.legend()

ax2.plot(x_Speed, Speed_LW, 'g', linewidth=1.5, label='Low')
ax2.plot(x_Speed, Speed_MD, 'b', linewidth=1.5, label='Medium')
ax2.plot(x_Speed, Speed_HG, 'r', linewidth=1.5, label='High')
ax2.plot(x_Speed, Speed_VH, 'y', linewidth=1.5, label='Very High')

ax2.set_title('Speed')
ax2.legend()

ax3.plot(x_Incremental, Incremental_SM, 'g', linewidth=1.5, label='Small')
ax3.plot(x_Incremental, Incremental_IM, 'b', linewidth=1.5, label='Intermediate')
ax3.plot(x_Incremental, Incremental_LG, 'r', linewidth=1.5, label='Large')
ax3.plot(x_Incremental, Incremental_VL, 'y', linewidth=1.5, label='Very Large')

ax3.set_title('Incremental Error')
ax3.legend()

for ax in (ax0, ax1, ax2, ax3):
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

# Input Value
DError = input("Masukan Nilai DError : ")
Error = input("Masukan Niali Error : ")
Incremental = input("Masukkan Nilai Incremental Error: ")

# Determining the Rule Base
"""
•R1,  IF DError SMALL        && Error LITTLE       && Incremental SMALL        THEN Speed = LOW (1000 rpm)
•R2,  IF DError SMALL        && Error LITTLE       && Incremental INTERMEDIATE THEN Speed = LOW (1500 rpm)
•R3,  IF DError SMALL        && Error LITTLE       && Incremental LARGE        THEN Speed = MEDIUM (2000 rpm)
•R4,  IF DError SMALL        && Error LITTLE       && Incremental VERY LARGE   THEN Speed = MEDIUM (2500 rpm)
•R5,  IF DError SMALL        && Error MIDDLE       && Incremental SMALL        THEN Speed = MEDIUM (2000 rpm)
•R6,  IF DError SMALL        && Error MIDDLE       && Incremental INTERMEDIATE THEN Speed = MEDIUM (2500 rpm)
•R7,  IF DError SMALL        && Error MIDDLE       && Incremental LARGE        THEN Speed = HIGH (3000 rpm)
•R8,  IF DError SMALL        && Error MIDDLE       && Incremental VERY LARGE   THEN Speed = HIGH (3500 rpm)
•R9,  IF DError SMALL        && Error BIG          && Incremental SMALL        THEN Speed = HIGH (3000 rpm)
•R10, IF DError SMALL        && Error BIG          && Incremental INTERMEDIATE THEN Speed = HIGH (3500 rpm)
•R11, IF DError SMALL        && Error BIG          && Incremental LARGE        THEN Speed = VERY HIGH (4000 rpm)
•R12, IF DError SMALL        && Error BIG          && Incremental VERY LARGE   THEN Speed = VERY HIGH (4500 rpm)
•R13, IF DError SMALL        && Error VERY BIG     && Incremental SMALL        THEN Speed = VERY HIGH (4000 rpm)
•R14, IF DError SMALL        && Error VERY BIG     && Incremental INTERMEDIATE THEN Speed = VERY HIGH (4500 rpm)
•R15, IF DError SMALL        && Error VERY BIG     && Incremental LARGE        THEN Speed = VERY HIGH (4750 rpm)
•R16, IF DError SMALL        && Error VERY BIG     && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)

•R17, IF DError INTERMEDIATE && Error LITTLE       && Incremental SMALL        THEN Speed = LOW (1500 rpm)
•R18, IF DError INTERMEDIATE && Error LITTLE       && Incremental INTERMEDIATE THEN Speed = MEDIUM (2000 rpm)
•R19, IF DError INTERMEDIATE && Error LITTLE       && Incremental LARGE        THEN Speed = MEDIUM (2500 rpm)
•R20, IF DError INTERMEDIATE && Error LITTLE       && Incremental VERY LARGE   THEN Speed = HIGH (3000 rpm)
•R21, IF DError INTERMEDIATE && Error MIDDLE       && Incremental SMALL        THEN Speed = MEDIUM (2500 rpm)
•R22, IF DError INTERMEDIATE && Error MIDDLE       && Incremental INTERMEDIATE THEN Speed = HIGH (3000 rpm)
•R23, IF DError INTERMEDIATE && Error MIDDLE       && Incremental LARGE        THEN Speed = HIGH (3500 rpm)
•R24, IF DError INTERMEDIATE && Error MIDDLE       && Incremental VERY LARGE   THEN Speed = VERY HIGH (4000 rpm)
•R25, IF DError INTERMEDIATE && Error BIG          && Incremental SMALL        THEN Speed = HIGH (3500 rpm)
•R26, IF DError INTERMEDIATE && Error BIG          && Incremental INTERMEDIATE THEN Speed = VERY HIGH (4000 rpm)
•R27, IF DError INTERMEDIATE && Error BIG          && Incremental LARGE        THEN Speed = VERY HIGH (4500 rpm)
•R28, IF DError INTERMEDIATE && Error BIG          && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)
•R29, IF DError INTERMEDIATE && Error VERY BIG     && Incremental SMALL        THEN Speed = VERY HIGH (4500 rpm)
•R30, IF DError INTERMEDIATE && Error VERY BIG     && Incremental INTERMEDIATE THEN Speed = VERY HIGH (4750 rpm)
•R31, IF DError INTERMEDIATE && Error VERY BIG     && Incremental LARGE        THEN Speed = VERY HIGH (5000 rpm)
•R32, IF DError INTERMEDIATE && Error VERY BIG     && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)

•R33, IF DError LARGE        && Error LITTLE       && Incremental SMALL        THEN Speed = MEDIUM (2000 rpm)
•R34, IF DError LARGE        && Error LITTLE       && Incremental INTERMEDIATE THEN Speed = MEDIUM (2500 rpm)
•R35, IF DError LARGE        && Error LITTLE       && Incremental LARGE        THEN Speed = HIGH (3000 rpm)
•R36, IF DError LARGE        && Error LITTLE       && Incremental VERY LARGE   THEN Speed = HIGH (3500 rpm)
•R37, IF DError LARGE        && Error MIDDLE       && Incremental SMALL        THEN Speed = HIGH (3000 rpm)
•R38, IF DError LARGE        && Error MIDDLE       && Incremental INTERMEDIATE THEN Speed = HIGH (3500 rpm)
•R39, IF DError LARGE        && Error MIDDLE       && Incremental LARGE        THEN Speed = VERY HIGH (4000 rpm)
•R40, IF DError LARGE        && Error MIDDLE       && Incremental VERY LARGE   THEN Speed = VERY HIGH (4500 rpm)
•R41, IF DError LARGE        && Error BIG          && Incremental SMALL        THEN Speed = VERY HIGH (4000 rpm)
•R42, IF DError LARGE        && Error BIG          && Incremental INTERMEDIATE THEN Speed = VERY HIGH (4500 rpm)
•R43, IF DError LARGE        && Error BIG          && Incremental LARGE        THEN Speed = VERY HIGH (4750 rpm)
•R44, IF DError LARGE        && Error BIG          && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)
•R45, IF DError LARGE        && Error VERY BIG     && Incremental SMALL        THEN Speed = VERY HIGH (4500 rpm)
•R46, IF DError LARGE        && Error VERY BIG     && Incremental INTERMEDIATE THEN Speed = VERY HIGH (4750 rpm)
•R47, IF DError LARGE        && Error VERY BIG     && Incremental LARGE        THEN Speed = VERY HIGH (5000 rpm)
•R48, IF DError LARGE        && Error VERY BIG     && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)

•R49, IF DError VERY LARGE   && Error LITTLE       && Incremental SMALL        THEN Speed = HIGH (3000 rpm)
•R50, IF DError VERY LARGE   && Error LITTLE       && Incremental INTERMEDIATE THEN Speed = HIGH (3500 rpm)
•R51, IF DError VERY LARGE   && Error LITTLE       && Incremental LARGE        THEN Speed = VERY HIGH (4000 rpm)
•R52, IF DError VERY LARGE   && Error LITTLE       && Incremental VERY LARGE   THEN Speed = VERY HIGH (4500 rpm)
•R53, IF DError VERY LARGE   && Error MIDDLE       && Incremental SMALL        THEN Speed = VERY HIGH (4000 rpm)
•R54, IF DError VERY LARGE   && Error MIDDLE       && Incremental INTERMEDIATE THEN Speed = VERY HIGH (4500 rpm)
•R55, IF DError VERY LARGE   && Error MIDDLE       && Incremental LARGE        THEN Speed = VERY HIGH (4750 rpm)
•R56, IF DError VERY LARGE   && Error MIDDLE       && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)
•R57, IF DError VERY LARGE   && Error BIG          && Incremental SMALL        THEN Speed = VERY HIGH (4500 rpm)
•R58, IF DError VERY LARGE   && Error BIG          && Incremental INTERMEDIATE THEN Speed = VERY HIGH (4750 rpm)
•R59, IF DError VERY LARGE   && Error BIG          && Incremental LARGE        THEN Speed = VERY HIGH (5000 rpm)
•R60, IF DError VERY LARGE   && Error BIG          && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)
•R61, IF DError VERY LARGE   && Error VERY BIG     && Incremental SMALL        THEN Speed = VERY HIGH (4750 rpm)
•R62, IF DError VERY LARGE   && Error VERY BIG     && Incremental INTERMEDIATE THEN Speed = VERY HIGH (5000 rpm)
•R63, IF DError VERY LARGE   && Error VERY BIG     && Incremental LARGE        THEN Speed = VERY HIGH (5000 rpm)
•R64, IF DError VERY LARGE   && Error VERY BIG     && Incremental VERY LARGE   THEN Speed = VERY HIGH (5000 rpm)
"""

#Determining Degree of Membership
d = [] #Delta Error
d.append(fuzz.interp_membership(x_DError, DError_SM, DError))
d.append(fuzz.interp_membership(x_DError, DError_IM, DError))
d.append(fuzz.interp_membership(x_DError, DError_LG, DError))
d.append(fuzz.interp_membership(x_DError, DError_VG, DError))

e = [] #Error
e.append(fuzz.interp_membership(x_Error, Error_LE, Error))
e.append(fuzz.interp_membership(x_Error, Error_ME, Error))
e.append(fuzz.interp_membership(x_Error, Error_BE, Error))
e.append(fuzz.interp_membership(x_Error, Error_VE, Error))

inc = [] #Incremental Error
inc.append(fuzz.interp_membership(x_Incremental, Incremental_SM, Incremental))
inc.append(fuzz.interp_membership(x_Incremental, Incremental_IM, Incremental))
inc.append(fuzz.interp_membership(x_Incremental, Incremental_LG, Incremental))
inc.append(fuzz.interp_membership(x_Incremental, Incremental_VL, Incremental))

print("DError Membership Degree ")
if d[0] > 0 :
    print("Small : "+str(d[0]))
if d[1] > 0 :
    print("Intermediate : "+str(d[1]))
if d[2] > 0 :
    print("Large  : "+ str(d[2]))
if d[3] > 0 :
    print("Very Large  :"+ str(d[3]))

print("---------")
print("Error Membership Degree")
if e[0]>0 :
    print("Little : "+str(e[0]))
if e[1]>0 :
    print("Middle  : "+ str(e[1]))
if e[2]>0 :
    print("Big  : "+ str(e[2]))
if e[3]>0 :
    print("Very Big  : "+ str(e[3]))

print("---------")
print("Incremental Error Membership Degree")
if inc[0]>0 :
    print("Little : " + str(inc[0]))
if inc[1]>0 :
    print("Middle  : " + str(inc[1]))
if inc[2]>0 :
    print("Large  : " + str(inc[2]))
if inc[3]>0 :
    print("Very Large  : " + str(inc[3]))

# Modeling Rule Base and Sugeno Inference/Implifikasi
rule_strengths = []
rule_outputs = []

for i, d_val in enumerate(d):
    for j, e_val in enumerate(e):
        for k, inc_val in enumerate(inc):
            strength = np.fmin(d_val, np.fmin(e_val, inc_val))
            if i == 0 and j == 0 and k == 0:
                z = 1000  # Small, Little, Small
            elif i == 0 and j == 0 and k == 1:
                z = 1500  # Small, Little, Intermediate
            elif i == 0 and j == 0 and k == 2:
                z = 2000  # Small, Little, Large
            elif i == 0 and j == 0 and k == 3:
                z = 2500  # Small, Little, Very Large
            elif i == 0 and j == 1 and k == 0:
                z = 2000  # Small, Middle, Small
            elif i == 0 and j == 1 and k == 1:
                z = 2500  # Small, Middle, Intermediate
            elif i == 0 and j == 1 and k == 2:
                z = 3000  # Small, Middle, Large
            elif i == 0 and j == 1 and k == 3:
                z = 3500  # Small, Middle, Very Large
            elif i == 0 and j == 2 and k == 0:
                z = 3000  # Small, Big, Small
            elif i == 0 and j == 2 and k == 1:
                z = 3500  # Small, Big, Intermediate
            elif i == 0 and j == 2 and k == 2:
                z = 4000  # Small, Big, Large
            elif i == 0 and j == 2 and k == 3:
                z = 4500  # Small, Big, Very Large
            elif i == 0 and j == 3 and k == 0:
                z = 4000  # Small, Very Large, Small
            elif i == 0 and j == 3 and k == 1:
                z = 4500  # Small, Very Large, Intermediate
            elif i == 0 and j == 3 and k == 2:
                z = 4750  # Small, Very Large, Large
            elif i == 0 and j == 3 and k == 3:
                z = 5000  # Small, Very Large, Very Large
            elif i == 1 and j == 0 and k == 0:
                z = 1500  # Intermediate, Little, Small
            elif i == 1 and j == 0 and k == 1:
                z = 2000  # Intermediate, Little, Intermediate
            elif i == 1 and j == 0 and k == 2:
                z = 2500  # Intermediate, Little, Large
            elif i == 1 and j == 0 and k == 3:
                z = 3000  # Intermediate, Little, Very Large
            elif i == 1 and j == 1 and k == 0:
                z = 2500  # Intermediate, Middle, Small
            elif i == 1 and j == 1 and k == 1:
                z = 3000  # Intermediate, Middle, Intermediate
            elif i == 1 and j == 1 and k == 2:
                z = 3500  # Intermediate, Middle, Large
            elif i == 1 and j == 1 and k == 3:
                z = 4000  # Intermediate, Middle, Very Large
            elif i == 1 and j == 2 and k == 0:
                z = 3500  # Intermediate, Big, Small
            elif i == 1 and j == 2 and k == 1:
                z = 4000  # Intermediate, Big, Intermediate
            elif i == 1 and j == 2 and k == 2:
                z = 4500  # Intermediate, Big, Large
            elif i == 1 and j == 2 and k == 3:
                z = 5000  # Intermediate, Big, Very Large
            elif i == 1 and j == 3 and k == 0:
                z = 4500  # Intermediate, Very Large, Small
            elif i == 1 and j == 3 and k == 1:
                z = 4750  # Intermediate, Very Large, Intermediate
            elif i == 1 and j == 3 and k == 2:
                z = 5000  # Intermediate, Very Large, Large
            elif i == 1 and j == 3 and k == 3:
                z = 5000  # Intermediate, Very Large, Very Large
            elif i == 2 and j == 0 and k == 0:
                z = 2000  # Large, Little, Small
            elif i == 2 and j == 0 and k == 1:
                z = 2500  # Large, Little, Intermediate
            elif i == 2 and j == 0 and k == 2:
                z = 3000  # Large, Little, Large
            elif i == 2 and j == 0 and k == 3:
                z = 3500  # Large, Little, Very Large
            elif i == 2 and j == 1 and k == 0:
                z = 3000  # Large, Middle, Small
            elif i == 2 and j == 1 and k == 1:
                z = 3500  # Large, Middle, Intermediate
            elif i == 2 and j == 1 and k == 2:
                z = 4000  # Large, Middle, Large
            elif i == 2 and j == 1 and k == 3:
                z = 4500  # Large, Middle, Very Large
            elif i == 2 and j == 2 and k == 0:
                z = 4000  # Large, Big, Small
            elif i == 2 and j == 2 and k == 1:
                z = 4500  # Large, Big, Intermediate
            elif i == 2 and j == 2 and k == 2:
                z = 4750  # Large, Big, Large
            elif i == 2 and j == 2 and k == 3:
                z = 5000  # Large, Big, Very Large
            elif i == 2 and j == 3 and k == 0:
                z = 4500  # Large, Very Large, Small
            elif i == 2 and j == 3 and k == 1:
                z = 4750  # Large, Very Large, Intermediate
            elif i == 2 and j == 3 and k == 2:
                z = 5000  # Large, Very Large, Large
            elif i == 2 and j == 3 and k == 3:
                z = 5000  # Large, Very Large, Very Large
            elif i == 3 and j == 0 and k == 0:
                z = 3000  # Very Large, Little, Small
            elif i == 3 and j == 0 and k == 1:
                z = 3500  # Very Large, Little, Intermediate
            elif i == 3 and j == 0 and k == 2:
                z = 4000  # Very Large, Little, Large
            elif i == 3 and j == 0 and k == 3:
                z = 4500  # Very Large, Little, Very Large
            elif i == 3 and j == 1 and k == 0:
                z = 4000  # Very Large, Middle, Small
            elif i == 3 and j == 1 and k == 1:
                z = 4500  # Very Large, Middle, Intermediate
            elif i == 3 and j == 1 and k == 2:
                z = 4750  # Very Large, Middle, Large
            elif i == 3 and j == 1 and k == 3:
                z = 5000  # Very Large, Middle, Very Large
            elif i == 3 and j == 2 and k == 0:
                z = 4500  # Very Large, Big, Small
            elif i == 3 and j == 2 and k == 1:
                z = 4750  # Very Large, Big, Intermediate
            elif i == 3 and j == 2 and k == 2:
                z = 5000  # Very Large, Big, Large
            elif i == 3 and j == 2 and k == 3:
                z = 5000  # Very Large, Big, Very Large
            elif i == 3 and j == 3 and k == 0:
                z = 4750  # Very Large, Very Large, Small
            elif i == 3 and j == 3 and k == 1:
                z = 5000  # Very Large, Very Large, Intermediate
            elif i == 3 and j == 3 and k == 2:
                z = 5000  # Very Large, Very Large, Large
            elif i == 3 and j == 3 and k == 3:
                z = 5000  # Very Large, Very Large, Very Large
            rule_strengths.append(strength)
            rule_outputs.append(z)
    
# Defuzzyfication sugeno
num = sum([strength * output for strength, output in zip(rule_strengths, rule_outputs)])
denum = sum(rule_strengths)

result = num/denum

#print the result
print("Output Speed: = ", round(result,2), "rpm")
