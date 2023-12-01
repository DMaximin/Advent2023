import sys;
units = {
        "zero" : "0", "one" :"1", "two" :"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8",
        "nine":"9",
}


def is_Number(char):
    try :
        int(char)
        return True
    except:
        return False

def is_Letter_Number(chars):

    if(chars.lower() in units.keys()):
        return units[chars]
    return None

with open("keys") as f :
    lines = f.read().split('\n')

sum = 0
for line in lines:
    first= None
    last = None
    values=[]
    for idx,char in enumerate(line):
        if is_Number(char):
            last = char
            if(first == None):
                first = last
        else:
            toParse = ""
            for conc in line[idx:]:
                toParse += conc
                # print(f"parsing {toParse}")
                parsed = is_Letter_Number(toParse)
                if(parsed != None):

                    last = parsed
                    if(first == None):
                        first = last
                    
    if first != None:
        sum += int(first+last)
        print(f" Adding {int(first+last)} to sum : Current sum {sum}")
print(f"Result sum {sum}")


