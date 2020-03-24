import sys
#Basic file I/O code

if len(sys.argv) != 2:
    print("usage: file.py filename")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename) as f:
        for line in f:
            print(line)

            #Ignore comments
            comment_split = line.split("#")

            #Strip out whitespace
            num = comment_split[0].strip()

            #Ignore blank lines
            if num == '': 
                continue
            
            value = int(num)
            

except FileNotFoundError:
    print("File not found")
    sys.exit(2)