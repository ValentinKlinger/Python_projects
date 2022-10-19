# This program can be used to brute force a zipped file.  
# This program works for passwords of the form "a + b + c" where a, b and c are strings.
# It will try all combinations of the form pwd_lvl_1 + pwd_lvl_2 + pwd_lvl_3 + ...
from zipfile import ZipFile 


file = "test_brute_force.zip" # the location of the zipped file example "/home/valentin/password"

pwd_lvl_1 = ['bob', 'Bob', 'robert', 'Robert', 'azerty'] # first level
pwd_lvl_2 = ['polson', 'Polson', '2812', '1504', '2020', '2022'] # second level
pwd_lvl_3 = ['', '2000', '2020', '2022', '22'] # third level
# you can add lvl here


with ZipFile(file, 'r') as zp: # open the zip file in reading mode.

    zp.printdir() # show all the contenu of the file.
  
    print('\nextraction...')

    for lvl_1 in pwd_lvl_1:
        '''try all combinations''' 
        for lvl_2 in pwd_lvl_2:
            for lvl_3 in pwd_lvl_3: 
                # if you have added lvl, you have to add for loops.
                try:
                    zp.extractall(path='extraction_zip', pwd=str.encode(lvl_1 + lvl_2 + lvl_3))
                        
                    print(f'the password is {lvl_1 + lvl_2 + lvl_3}!\nCompleted!')
                    exit()
                except RuntimeError:
                    pass
    print("We don't found the password sorry")
