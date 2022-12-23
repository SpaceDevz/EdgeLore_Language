"""
Credits: 

Class Parsing made by ben!#2990 on discord
Still pretty slow, but more efficient + can handle infinite amount of classes.

Roughly creates the class in: 0.0002 (Sped up)
Implementation for parsing multiple classes :D
"""

import time

indices = []

fin = open("class.edge", "r+") 
lines = fin.readlines()
fout = open('tempRunner.py', "w+")
fout.write("from dataclasses import dataclass\n\n")
fout.close()

e = time.time()
for idx, line in enumerate(lines):
  if "CREATE,NEW,CLASS" in line:
    indices.append(idx)
  elif "END,CLASS" in line:
    indices.append(idx)
    
unpackable = [(i,j) for i,j in zip(indices[::2], indices[1::2])]
for i,j in unpackable:
  name = lines[i+1].strip().split('"')[1].replace(".", "_")
  variables = [n.strip().split('"') for n in lines[i+3:j]]
  print(name, variables, sep="\n")

  with open("tempRunner.py", "a+") as fout:
    for n in range(len(variables)):
      fout.write("class ")
      fout.write(f"{(variables[n][-1] + variables[n][-2]).replace(',', '')}:\n  pass\n")
    fout.write("\n\n@dataclass\nclass ")
    fout.write(f"{name}:\n")
    fout.write(f'''  """Class definition created by EdgeLore\n     Creation Time: {time.time() - e:.6f}"""\n\n''')
      
