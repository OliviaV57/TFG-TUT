import numpy as np
import eagleSqlTools as sql
from matplotlib import pyplot as plt
print(1)
con = sql.connect("olivia.vidal@estudiante.uam.es", "TFG-TUT2020")
print(2)
the_query = """SELECT snapnum, MstarSpheroid FROM MDPL2.Galacticus
            WHERE redshift = 0 
            LIMIT 10"""
print(3)
data = con.execute_query(the_query)
print(4)
print (type (data))

print ("Compila")