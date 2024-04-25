

'''
This is my module so that i dont need to change the datagase_main_class module 
for call any function
Here i will defines some functions here so that i can use this in other main program
1st: ** add_user_and_return_id_ ** ✅

Last: i will add a fun which will take the id_ and then it will search
    in my database about the row and return the objec fully

-Rana Universe 🍌🍌🍌
'''

# Adding a comment to make a change


import sys
sys.dont_write_bytecode = True




from datetime import datetime
from pathlib import Path


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_main_class import Base, UserDetails







db_filename = "users_information.db"
folder_name = Path("RanaUniverse") / "database_store_folder"
folder_name.mkdir(parents= True, exist_ok= True)
file_location = folder_name / db_filename
file_url = f"sqlite+pysqlite:///{file_location}"

engine = create_engine(url= file_url, echo= False)

Session = sessionmaker(bind= engine)
session = Session()

Base.metadata.create_all(engine)






def add_user_and_return_id_(
        user_id_: int = None,
        username_: str = None,
        full_name_: str = None,
        type_: str = None,
        token_: int = None,
        start_time_: datetime = None,
        end_time_: datetime = None
    ):
    '''
    This will take the UserDetails Class information
    and it will insert the user into the database and then
    it will return the *id_
    '''
    user_obj = UserDetails(user_id_= user_id_, username_= username_, full_name_= full_name_, type_= type_, token_= token_, start_time_= start_time_, end_time_= end_time_)

    session.add(user_obj)
    session.commit()
    inserted_id_ = user_obj.id_
    session.close()
    print("User added successfully. ID:", inserted_id_)
    return inserted_id_




def find_user_from_id_(id_:int = None):
    '''
    id_ is the primary column value
    this will take unique id_ and then it will search the row
    '''
    if id_ is None:
        print("Please provide valid id_ other than 'None'")
        return None

    try:
        user_obj = session.query(UserDetails).filter_by(id_=id_).first()
        print(user_obj)
        return user_obj
    except Exception as e:
        print("A error has came:", e)
        return None




def update_user_by_id(id_, **kwargs):
    '''
    Here the columns names are,
    id_         INTEGER  NOT NULL,
    user_id_    INTEGER,
    username_   VARCHAR,
    full_name_  VARCHAR,
    type_       VARCHAR,
    token_      INTEGER,
    start_time_ DATETIME,
    end_time_   DATETIME,
    PRIMARY KEY (
        id_
    )
    so i need to kwargs inside this so that i can chagne approgpriag
    '''
    try:
        print("before update", find_user_from_id_(id_))
        update_query = (
            session.query(UserDetails)
            .filter(UserDetails.id_ == id_)
            .update(kwargs)
        )

        session.commit()

        if update_query:
            print(f"User with id_ {id_} updated successfully.")
            return True
        else:
            print(f"No user found with id_ {id_}.")
            return False

    except Exception as e:
        session.rollback()
        print("Error updating user:", e)
        return False
    finally:
        session.close()
        print("AFter update", find_user_from_id_(id_))







def total_row_count():
    '''
    Need to impliment later ⚠⚠⚠🍌🍌🍌
    This will count how many users are there in the table
    it will count how many row is there and return this int
    '''
    def long_time_taken():
        user_obj = session.query(UserDetails).all()
        print(len(user_obj))
        return len(user_obj)

    user_obj = session.query(UserDetails).count()
    print(user_obj)
    return user_obj











if __name__ == "__main__":
    add_user_and_return_id_("manik")









