## To break down a folder by { file ext: count}
## for example, if you point d to a production volume, you will expect to see
## something like this {'.OPT': 1, '.TIF': 6015, '.LFP': 1, '.TXT': 408, '.DII': 1, '.CSV': 1, '.DAT': 2}
## which means in the production there are 6015 tif files, 408 text files, and 1 opt, lfp, dii, csv file and 2 Dat files.
## quite useful for QC purpose on a production volume. using windows right click - > property will get not accurate doc count 
## because thumb.db files are counted by windows too. 

## uncomment to get filesize sum for each file type, size in byte


from os import walk
from os.path import isfile, join, getsize, splitext

d = r"C:\path\to\the\folder"  # use "r" only in windows environment, and both local and UNC path should work
       

report_dict_count = {}
report_dict_size={}


for root, subdirs, files in walk(d):
    for f in files:
        ext = splitext(f)[1]
        if ext in report_dict_count:
            report_dict_count[ext] += 1
            ##report_dict_size[ext] += getsize(join(root,f))
        else:
            report_dict_count[ext] = 1
            ##report_dict_size[ext] = getsize(join(root,f))

print(report_dict_count)
##print(report_dict_size)
            
            
