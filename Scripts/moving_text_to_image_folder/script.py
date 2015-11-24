##Move text files into corresponding image folders

source_path = r"path\to\TEXT"
target_path = r"path\to\IMAGES"

import glob
import ntpath
import os
import shutil

source_text_list = glob.glob(source_path+r"\**\*.TXT")
target_image_list = glob.glob(target_path+ r"\**\*")

for file in source_text_list:
    text_file_name_to_look = os.path.splitext(ntpath.basename(file))[0]
    for image in target_image_list:
        image_file_base_name = os.path.splitext(ntpath.basename(image))[0]
        if text_file_name_to_look ==image_file_base_name:
            shutil.copy(file,os.path.dirname(os.path.abspath(image)))
            
            
    

