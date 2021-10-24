#Pyhton 3.x
# -*- coding: UTF-8 -*-

import wand
from wand.image import Image as WImage
import traceback
import re
import shutil
import os

class Convert2JPG():
    def __init__(self) -> None:
        pass
    
    def Heic2JPG(self, curDir, file):
        fname = ""
        try:
            with WImage(filename= curDir + '/' + file) as img:
                #print(img.width, img.height)
                im = img.convert('jpeg')
                im.save(filename= curDir + '/' + file + '.JPG')
            
            if os.path.exists(curDir + '/' + file + '.JPG'):
                fname = file + '.JPG'                
                if not os.path.exists(curDir + '/Heic_+_Livp'):  
                    os.makedirs(curDir + '/Heic_+_Livp')
                shutil.move(curDir + '/' + file, curDir + '/Heic_+_Livp/' + file)          
        except:
            print(traceback.format_exc())   
            
        return fname
     
    def Livp2JPG(self, curDir, file):
        fname = ""
        try:
            fsize = os.path.getsize(curDir + '/' + file)            
            buf = bytearray(fsize)
            with open(curDir + '/' + file, "rb") as FH:
                FH.readinto(buf)
                
            new_file_name = file + ".JPG"
            if re.match(r'.*heic', str(buf[0:100]), re.I):
                new_file_name = file + ".HEIC"
            print("\tsave image to", new_file_name)
        
            newImg = open(curDir + '/' + new_file_name, "wb")
            newImg.write(buf)
            newImg.close()

            if re.match(r'.*\.heic$', new_file_name, re.I):
                with WImage(filename= curDir + '/' + new_file_name) as img:               
                    im = img.convert('jpeg')
                    im.save(filename= curDir + '/' + file + '.JPG')
                
                os.unlink(curDir + '/' + new_file_name)             
                       
            if os.path.exists(curDir + '/' + file + '.JPG'):
                fname = file + '.JPG'
                if not os.path.exists(curDir + '/Heic_+_Livp'):  
                    os.makedirs(curDir + '/Heic_+_Livp')
                shutil.move(curDir + '/' + file, curDir + '/Heic_+_Livp/' + file)          
        except:
            print(traceback.format_exc())   
            
        return fname   