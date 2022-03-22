from datetime import date
from extract import *

data_df = songs_extract()

#PERFORMING VALIDATIONS
def data_validation(df = data_df) -> bool:
    #CHECKING IF DATAFRAME IS EMPTY
    if(df.empty):
        print("No Songs Played")
        return(False)

    #CHECKING FOR ALL UNIQUE VALUES
    if(pd.Series(df['played at']).is_unique):
        pass
    else:
        raise Exception("Primary Key Constraint Error")

    #CHECKING FOR ANY NULL VALUES
    if(df.isnull().values.any()):
        raise Exception("Null Value Found")

    #CHECKING IF ALL SONGS ARE FROM YESTERDAY
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    yesterday = yesterday.replace(hour=0,minute=0,second=0,microsecond=0)

    timestamps = df['timestamp'].tolist()
    for timestamp in timestamps:
        if(datetime.datetime.strptime(timestamp,"%Y-%m-%d") != yesterday):
            raise Exception("Atleast one song not from yesterday")


def send_to_load():
    if(data_validation(data_df)):
        return(data_df)

if(data_validation()):
    print("Data Correct. Proceed to load")
