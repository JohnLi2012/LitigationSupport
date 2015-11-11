##Instruction of use
##
##Senario: you get a reference of a list of bates numbers with some information which happen to be page bates.
##You need to overlay the information into database being Relativity, Concordance or whatever. Since most system is document level,
##you will have to find out the corresponding begbates for those page bates, so you could perform the overlay
##
##Purpose: This script loops through a list of page bates, and find its corresponding begbates from another source list file
##



#  UNC path or local path both work:
#  C:\source.csv
#  \\myshare\data\list.csv

list_of_page_bates = open(r"\\UNC\path\to\the\file1","r") 
list_of_begbates_and_endbates = open(r"\\local\path\to\the\file2","r") 

fullbatesrange = []
mylist =[]
outputlist=[]

with list_of_begbates_and_endbates as f:
    for line in f:
        fullbatesrange.append(line.strip())

with list_of_page_bates as f:
    for line in f:
        found = False
        b = line.strip().split(",")[1] # bates in the list to be identified
        for elem in fullbatesrange:
            if b == elem.strip().split(",")[0]: # if bates happen to be a begdoc; add to outputlist move to next iteration
                outputlist.append(str(line.strip())+","+elem.strip().split(",")[0])
                found = True
                break
            elif b>elem.strip().split(",")[0]and b<=elem.strip().split(",")[1]: # if bates fall between fullbatesrange, do the same as above
                outputlist.append(str(line.strip())+","+elem.strip().split(",")[0])
                found = True
                break
            else:
                continue
        if(not found):
            outputlist.append(str(line.strip())+",NOFOUND")
      
print("\n".join(outputlist))
    
