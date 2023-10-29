from tkinter import *
from tkinter import messagebox
import time
import bme280


(chip_id, chip_version) = bme280.readBME280ID()
print("Chip ID :", chip_id)
print("Version :", chip_version)
def druckmessen():
 pressure=0
 a=2.5
 t=[]
 for i in range(0,11):
    pressure = bme280.readBME280All()
    p=pressure*0.001
    if p<=0.5:
     s="Platte reife"
     messagebox.showwarning(s,s)
     break
    else:
      t.append(p)
      p=0
      
      
 if sum(t)/len(t)>0.0:
  d=sum(t)/len(t)
  d=round(d,3)
 if d<a:
  a=a-d
  b=str(a)
  s="es muessen noch an die Reife "
  s1="bar aufgepumpet werden"
  s2=s+b+s1
  messagebox.showinfo(s2,s2)     