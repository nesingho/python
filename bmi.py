#!/usr/bin/env python3.6

_weight = float(input("Gewicht in kg eingeben: "))
_heightcm = float(input("Größe in cm eingeben: "))

_heightm = float(_heightcm/100)
_bmi = round((_weight/(_heightm*_heightm)),1)

print ("Gewicht in kg: ",_weight)
print ("Größe im m: ",_heightm)
print ("BMI: ",_bmi)

if (_bmi < 18.5):
    print("Untergewicht!")
elif (_bmi > 25):
    print("Übergewicht!")
else:
    print("Normalgewicht")

