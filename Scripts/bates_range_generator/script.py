import re

## function that extracts numbers from a bates
## if prefix doesnt include number, the result will return a list with single itme
## if prefix inluces a number, for example like 'ABC-3-ddd-000232',
## the return result will be like ['3','000232']
## please note all returned results are list of strings that only contain numbers

def extract_numbers( bates ):
    return re.findall(r'\d+',str(bates))[-1]

## function that return the prefix of bates
## please note it will return empty string if the bates contain pure numbers
## like '0045334'

def extract_prefix( bates ):
    bates_num = extract_numbers( bates ) # return last item to ensure its the number part not number in prefix
    return bates[0:len(str(bates))-len(bates_num)] 
    
## read a csv file that contains beg and end bates

source = open(r"\\unc\path\to\sourcefile.txt","r") # local path works too like C:\Users\johnli\Downloads\source.txt
output = open(r"\\unc\path\to\output.txt","a+") # this file doesnt need to be created, script will create if file doesnt exist

with source as f:
    temp = '' # temp is used to store endbates, and then be used to compare with next begbates in next loop run
    temp_prefix = 'a' # hold prefix from last line
    for line in f:
        beg = line.strip().split(",")[0] # store begbates in a variable beg for later use
        end = line.strip().split(",")[1] # store endbates in a variable end for later use        
        beg_prefix = extract_prefix( beg )
        end_prefix = extract_prefix( end )        
        beg_number = extract_numbers( beg )
        end_number = extract_numbers( end )
        if beg_prefix != end_prefix:
            print(line+" has different prefixes")
            continue
        if int(end_number) < int(beg_number):
            print(line+" endbates is smaller than begbates")
            continue      
            
        if beg_prefix != temp_prefix: # new prefix found, meaning new bates range found
            temp_prefix = beg_prefix            
            output.write(temp+'\n') # write previous end bates and start a new line since there is a new bates range
            output.write(beg+',')
            temp=end # temp now holds the new end bates number
            continue
        if beg_prefix == temp_prefix and int(beg_number) == int(extract_numbers(temp)) + 1 :
            temp = end
            continue # verify the next beg number is continuous from last end number, do nth
        if beg_prefix == temp_prefix and int(beg_number) != int(extract_numbers(temp)) + 1: # there is a gap
            # handle gap here
            output.write(temp+'\n')
            output.write(beg+',')
            temp = end
            continue
    output.write(temp+'\n') # end of loop    
output.close()
        
            
        
        
