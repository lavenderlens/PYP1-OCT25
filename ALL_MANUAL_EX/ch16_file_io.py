# ensure terminal is in this directory before running

file_read_ref = open('students.dat')
results = []
for name in file_read_ref:
    grade = input(f"Enter a grade for {name}")
    results.append(name.strip('\n') + ", " + grade.strip('\n'))
file_read_ref.close()
print(results)

# x CREATE IF NOT EXIST ELSE THROW ERROR
# a APPEND
# file_write_ref = open('studentgrades.txt', mode='a')
file_write_ref = open('studentgrades.txt', mode='w')

for entry in results:
    file_write_ref.write(f"{entry}\n")

file_write_ref.close()