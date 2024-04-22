
'''
i have added this first line from the mobile app

This is the main part of example where i will call the fun to be executed
for example here i will call a fun which will add user info in a database
or a i will call a fun by importing from the database_fun.py module which 
will search the information and match and return something for use
'''


import sys
sys.dont_write_bytecode = True


from database_fun import add_user_and_return_id_

from datetime import datetime






if __name__ == "__main__":
    add_user_and_return_id_("rana", "@hello")




