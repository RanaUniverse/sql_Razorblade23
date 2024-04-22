

'''
This is the scripts where i will add different class for different tables
This is the database defines table creates

'''


from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base





Base = declarative_base()


class UserDetails(Base):
    __tablename__ = "UserDetails"

    id_ = Column(Integer, primary_key= True)
    user_id_ = Column(Integer)
    username_ = Column(String)
    full_name_ = Column(String)
    type_ = Column(String)
    token_ = Column(Integer)
    start_time_ = Column(DateTime)
    end_time_ = Column(DateTime)


    def __init__(
        self,
        user_id_: int = None,
        username_: str = None,
        full_name_: str = None,
        type_: str = None,
        token_: int = None,
        start_time_: datetime = None,
        end_time_: datetime = None
    ):
        self.user_id_ = user_id_
        self.username_ = username_
        self.full_name_ = full_name_
        self.type_ = type_
        self.token_ = token_
        self.start_time_ = start_time_
        self.end_time_ = end_time_







def main():
    print("This is the main of this module")
    


if __name__ == "__main__":
    main()









