"""
This script is used to check bates gaps. You need to enter the number
of paddings in integer format for the script to run. For example, ABC 000343
has 6 paddings. Please note this script is not capable of checking bates
with different paddings or prefixes. A sample source.txt is provided for demostration
only. path to text file could be relative, UNC or local. 
"""

with open(r"./source.txt","r") as f:
    print("Please enter number of paddings")
    try:
        n = int(input())
    except ValueError:
        print("Please re-run the script and enter an integer!")    
    temp = ''
    i = 0
    for line in f:
        i = i + 1
        if temp == '':
            temp = line.strip(' \t\n\r').split(',')[1]                        
            continue        
        if int(line.strip(' \t\n\r').split(',')[0][-n:]) == int(temp[-n:])+1:
            temp = line.strip(' \t\n\r').split(',')[1]
            continue
        else:
            print("gap found")
            print(line.strip(' \t\n\r'))
            temp = line.strip(' \t\n\r').split(',')[1]
            continue
    print(str(i) + " lines have been scanned. Done!")

