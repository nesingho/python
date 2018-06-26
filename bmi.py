#!/usr/bin/env python3.6

_weight = float(input("Gewicht in kg eingeben: "))
_height = float(input("Größe in m eingeben: "))

_bmi = round((_weight/(_height*_height)),1)
print ("BMI: ",_bmi)

if (_bmi < 18.5):
    print("Untergewicht!")
elif (_bmi > 25):
    print("Übergewicht!")
else:
    print("Normalgewicht")

