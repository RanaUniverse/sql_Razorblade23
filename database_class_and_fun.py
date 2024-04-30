

'''
Here i will defines the class of my main datbase logic 
so that i can use this in other places easily
Here i used pathlib's Path so that the .db file will saved in the folder
all the fun i made here, i will use this in main.py this is my logic
'''

from datetime import datetime
from pathlib import Path


from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Boolean ,DateTime, Integer, String

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db_filename = "user_information_checking.db"
folder_name = Path("RanaUniverse") / "data_store_folder"
folder_name.mkdir(parents= True, exist_ok= True)
file_location = folder_name / db_filename


file_url = f"sqlite+pysqlite:///{file_location}"
engine = create_engine(url= file_url, echo= False)

Session = sessionmaker(bind= engine)
session = Session()


Base = declarative_base()


class UserDetails(Base):
    __tablename__ = "user_details"

    id_ = Column(Integer, primary_key= True)
    user_id_ = Column(Integer)
    user_name_ = Column(String)
    full_name_ = Column(String)
    is_premium_ = Column(Boolean)
    validity_ = Column(DateTime)

    def __init__(
            self,
            user_id_:int = 0,
            user_name_:str = None,
            full_name_:str = None,
            is_premium_:bool = None,
            validity_:datetime = None
    ):
        self.user_id_ = user_id_
        self.user_name_ = user_name_
        self.full_name_ = full_name_
        self.is_premium_ = is_premium_
        self.validity_ = validity_

    def __repr__(self):
        user_obj_details = f"<UserDetails(id={self.id_}, user_id={self.user_id_}, user_name={self.user_name_}, full_name={self.full_name_}, is_premium={self.is_premium_}, validity={self.validity_})>"
        return user_obj_details


    '''Below are fun taking the class instance'''

    def add_user_return_id_(self):
        """This will take the user obj and return the inserted id_"""
        session.add(self)
        session.commit()
        inserted_id_ = self.id_
        print(inserted_id_, self)
        # session.close()
        return inserted_id_


    def delete_user(self):
        session.delete(self)
        session.commit()


    @staticmethod
    def count_total_users():
        '''Count the total number of users'''
        count = session.query(UserDetails).count()
        session.close()
        return count
    

    @staticmethod
    def get_all_users():
        '''Get all users from the database'''
        users = session.query(UserDetails).all()
        session.close()
        return users




    @staticmethod
    def check_user_is_premium_new(user_id_: int = None):
        user_obj = session.query(UserDetails).filter(UserDetails.user_id_ == user_id_).first()
        print("userdetials are", user_obj)
        if user_obj:
            if user_obj.is_premium_ == True:
                return True
            else:
                return False
        else:
            return None


    @staticmethod
    def fun_to_get_premium_value(id_value: int = 0):
        user_obj = session.query(UserDetails).filter(UserDetails.user_id_ == id_value).first()
        value = user_obj.is_premium_
        print(value)


    @staticmethod
    def insert_many_row_one_by_one(number_of_row: int = 1):
        '''This is not good fun, rather i need to make a add_all fun'''
        for i in range(number_of_row):
            user_obj: UserDetails = UserDetails(
                user_id_= fake.random_int(100, 300),
                user_name_= (fake.name()).replace(" ", "_"),
                full_name_= fake.name(),
                is_premium_= fake.boolean(),
                validity_= fake.date_time(end_datetime = datetime(2025, 1, 1)))
            user_obj.add_user_return_id_()


    @staticmethod            
    def insert_many_rows(number_of_rows: int = 1):
        '''Insert multiple rows into the database using add_all method.'''
        users = []
        for i in range(number_of_rows):
            user = UserDetails(
                user_id_=fake.random_int(100, 300),
                user_name_=(fake.name()).replace(" ", "_"),
                full_name_=fake.name(),
                is_premium_=fake.boolean(),
                validity_=fake.date_time(end_datetime=datetime(2025, 1, 1))
            )
            users.append(user)
        
        session.add_all(users)
        session.commit()
        print(users)
        print(users.__len__())


# This below line is the most important as it will do the main things

Base.metadata.create_all(engine)


#Below functions i made for checking purpose
def count_total_users():
    '''Count the total number of users'''
    count = session.query(UserDetails).count()
    session.close()
    return count

def get_all_users():
    '''Get all users from the database'''
    users = session.query(UserDetails).all()
    session.close()
    return users

def fun_to_get_premium_value(id_value: int = 0):
    user_obj = session.query(UserDetails).filter(UserDetails.user_id_ == id_value).first()
    value = user_obj.is_premium_
    print(value)



if __name__ == "__main__":
    '''This is just for the example as if it is the another main.py scripts'''

    from faker import Faker
    fake = Faker()
    print("Starting the Main Function of this Scripts Running")

    UserDetails.insert_many_row_one_by_one(100)
    UserDetails.insert_many_rows(10)


    fun_to_get_premium_value(187)
    fun_to_get_premium_value(189)





