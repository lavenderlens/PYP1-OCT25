file_read_ref = open("students.dat","r")
results=[]
for line in file_read_ref:
 #strip new line char from name
 line=line.strip()
 print(line)
 grade=str(input(f"Grade for {line} "))
 results.append(line.strip('\n') +"," + grade)
 print(results)#in PY

#  write results to new file