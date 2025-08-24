import sys
file1 = ""
file2 = ""
if len(sys.argv) != 3 :
    print("run formater filename1 outputfilename")
    sys.exit()
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

print(f"file1: {file1}")
print(f"file2: {file2}")
string = ""
reader = open(file1, "r")
writer = open(file2, "w") 

eof = False
while eof == False :
    character = reader.read(1)
    if not character :
        eof = True
    string = string + character
    if character == ";" or character == "{" or character == "}" :
        writer.write(string + "\n")
        string = ""

reader.close()
writer.close()
sys.exit()