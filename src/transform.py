from utils.logger_setup import get_logger
import pandas as pd
from pathlib import Path

logger = get_logger(__name__)

# Now Trandsformation begins 

def transformation(df):
    logger.info("transformation of data begins")

    # 1. Drop rows where name is missing
    before = len(df)
    df = df.dropna(subset=["name"])
    dropped = before - len(df)

    if dropped > 0:
        logger.warning("Dropped %d rows with misisng name: " , dropped)
    else:
        logger.debug("No rows dropped for missing name")   

    # 2. Drop rows where age is not a number

    before = len(df)

    # this will first try to convert to string in to number of valid otherwise
    #convert them to a nan value and the notna() will keep the valid number and remove the nan.
    
    df = df[pd.to_numeric(df["age"] , errors = "coerce").notna()]

    dropped = before - len(df)

    if dropped > 0:
        logger.warning("dropped %d rows where age is not number:" , dropped)
    else:
        logger.debug("no rows dropper for invalid  age")   

     # 3. Drop rows where grade is empty

    before = len(df)

    df = df.dropna(subset =["grade"])
    dropped = before - len(df)

    if dropped > 0:
        logger.warning("Dropped %d rows with empty grade : " , dropped)
    else:
        logger.debug("No rows dropped for empty grade ")   

    logger.info("transformation complete . rows remaining : %d " , len(df))

    return df   

if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent.parent/"data"/"raw"/"Student_details.csv"  # ✅ pathlib

    df = pd.read_csv(FILE_PATH)

    logger.info("Loaded %d rows", len(df))

    cleaned_df = transformation(df) 

    

    













