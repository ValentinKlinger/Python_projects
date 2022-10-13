# This program can be used to brute force a zipped file.
# This program works for passwords of the form "a + b + c" where a, b and c are strings.
# It will try all combinations of the form pwd_lvl_1 + pwd_lvl_2 + pwd_lvl_3 + ...
from zipfile import ZipFile 


file = "" # the location of the zipped file example "/home/valentin/password"

pwd_lvl_1 = ['Valentin'] # first level, example : ['bob', 'Bob', 'robert', 'Robert', 'azerty']
pwd_lvl_2 = ['2712'] # second level, example : ['polson', 'Polson', '2812', '1504', '2020', '2022']
pwd_lvl_3 = [''] # third level, example : ['', '2812', '1504', '2020', '2022']
# you can add lvl here


with ZipFile(file, 'r') as zip: # open the zip file in reading mode.

    zip.printdir() # show all the contenu of the file.
  
    print('\nextraction...')

    for lvl_1 in pwd_lvl_1:
        '''try all combinations''' 
        for lvl_2 in pwd_lvl_2:
            for lvl_3 in pwd_lvl_3: 
                # if you have added lvl, you have to add for loops.
                try:
                    zip.extractall(path='extraction_zip', pwd=str.encode(lvl_1 + lvl_2 + lvl_3))
                        
                    print(f'the password is {lvl_1 + lvl_2 + lvl_3}!\nCompleted!')
                    exit()
                except RuntimeError:
                    pass 