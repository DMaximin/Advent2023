import sys;
with open("keys") as f :
    lines = f.read().split('\n')

sum = 0
for line in lines:
    first= None
    last = None
    for char in line:
        try:
           int(char)
           last = char
           if(first == None):
               first = last

        except ValueError:
            None
    if first != None:
        sum += int(first+last)
        print(f" Adding {int(first+last)} to sum : Current sum {sum}")
print(f"Result sum {sum}")