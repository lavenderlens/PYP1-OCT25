# execute from CMD line, ensure cursor is in this directory

# open the file for reading
file = open("data.txt")
# other ways to call a relative file path
# relative to where the calling script is
# file = open("../parent_folder/data.txt")
# file = open("./folder_name/data.txt")
print(type(file))#<class '_io.TextIOWrapper'>
print(file)#<_io.TextIOWrapper name='data.txt' mode='r' encoding='UTF-8'>
# about as much use as a chocolate teapot
# we must use methods of the TextIOWrapper object to read/write

# 1. read (whole file)
print(f"\n{"*" * 50}\nread whole file\n{"*" * 50}")
print(file_contents := file.read())
# super-important
file.close()

# 2. read limited characters
print(f"\n{"*" * 50}\nread limited characters\n{"*" * 50}")
file = open("data.txt")
print("79")
print(limited_chars_79 := file.read(79))
print("120")
print(limited_chars_120 := file.read(120))#cursor continues from rest position
file.close()

# 2A. read limited characters and reset cursor
print(f"\n{"*" * 50}\nread limited characters and reset cursor\n{"*" * 50}")
file = open("data.txt")
print("79")
print(limited_chars_79 := file.read(79))
file.close()
file = open("data.txt")
print("120")
print(limited_chars_120 := file.read(120))#cursor continues from rest position
file.close()

# 3. read line
print(f"\n{"*" * 50}\nread line\n{"*" * 50}")
file = open("data.txt")
print(line := file.readline())
file.close()

# 4. read lines
print(f"\n{"*" * 50}\nread multiple lines\n{"*" * 50}")
file = open("data.txt")
print(lines := file.readlines())#list of lines, each with newline char at end
file.close()

for line in lines:
    print(line)#double newline characters, 1 from readlines and 1 from print

