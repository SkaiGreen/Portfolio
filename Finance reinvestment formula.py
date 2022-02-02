import time
import pandas as pd
import numpy as np
print("Welcome to the finance calculator")
time.sleep(1)
print("This helps you calculate what your monthly revenue will be if you save all that money \nand reinvest with conditions similiar to prior investments")
print("Loading....")
time.sleep(2)
print("What would you like to do?")
print("(a) Find the monthly revenue on the nth month \n(b) Find the future monthly revenue given a certain risk/spend/loss %")
Revenue = input("Enter choice: ")
if Revenue == "a" or "b":
    I = int(input("Enter initial investment amount: "))
    RI = int(input("Enter reinvestment amount: "))
    CS = input("Enter currency symbol: ")
    MP = float(input("Enter monthly percentage pay: "))/100
    R = I * MP
    M = int(input("Enter the number of months you would like to know the new revenue on: "))
    if Revenue == "b":
        risk = float(input("Enter monthly risk/loss percentage: "))
        RI = RI - (RI*risk/100)
        I = I - (I * risk/100)




#This section applies a mathematical funtions what groups the number of months


G1 = (RI - MP*I)/(MP*I)
G2 = G1-((RI - MP * I * 2) / (MP * I * 2))
G3 = G2-((RI - MP * I * 3) / (MP * I * 3))
G4 = G3-((RI - MP * I * 4) / (MP * I * 4))
G5 = G4-((RI - MP * I * 5) / (MP * I * 5))
G6 = G5-((RI - MP * I * 6) / (MP * I * 6))
G7 = G6-((RI - MP * I * 7) / (MP * I * 7))
G8 = G7-((RI - MP * I * 8) / (MP * I * 8))
G9 = G8-((RI - MP * I * 9) / (MP * I * 9))
G10 = G9-((RI - MP * I * 10) / (MP * I * 10))
G11 = G10-((RI - MP * I * 11) / (MP * I * 11))
G12 = G11-((RI - MP * I * 12) / (MP * I * 12))
G13 = G12-((RI - MP * I * 13) / (MP * I * 13))
G14 = G13-((RI - MP * I * 14) / (MP * I * 14))
G15 = G14-((RI - MP * I * 15) / (MP * I * 15))
G16 = G15-((RI - MP * I * 16) / (MP * I * 16))
G17 = G16-((RI - MP * I * 17) / (MP * I * 17))
G18 = G17-((RI - MP * I * 18) / (MP * I * 18))
G19 = G18-((RI - MP * I * 19) / (MP * I * 19))
G20 = G19-((RI - MP * I * 20) / (MP * I * 20))

#print(G1,G2,G3,G4,G5)
#print(G1,G1+G2,G2+G3+G1,G1+G2+G3+G4,G1+G2+G3+G4+G5)
Answer = 0
if M <= G1:
    Answer = (MP*I) + ((1-1)*MP*RI)
elif M <= G1+G2:
    Answer = (MP * I) + ((2 - 1) * MP * RI)
elif M <= G2+G3+G1:
    Answer = (MP * I) + ((3 - 1) * MP * RI)
elif M <= G1+G2+G3+G4:
    Answer = (MP * I) + ((4 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5:
    Answer = (MP * I) + ((5 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6:
    Answer = (MP * I) + ((6 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7:
    Answer = (MP * I) + ((7 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8:
    Answer = (MP * I) + ((8 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9:
    Answer = (MP * I) + ((9 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14+G15:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16+G17:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16+G17+G18:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16+G17+G18+G19:
    Answer = (MP * I) + ((10 - 1) * MP * RI)
elif M <= G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16+G17+G18+G19+G20:
    Answer = (MP * I) + ((10 - 1) * MP * RI)


elif M > G1+G2+G3+G4+G5+G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16+G17+G18+G19+G20:
    Answer = "Currently can not compute that many groups"

print("Monthly Renvenue on month " + str(M)+" will be "+CS+str(Answer))
