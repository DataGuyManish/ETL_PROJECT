from utils.logger_setup import get_logger
from pathlib import Path
import pandas as pd

logger = get_logger(__name__)

def extract():
    FILE_PATH = Path(__file__).parent.parent / "data" / "raw" / "Student_details.csv"
    
    logger.info("Starting extraction from: %s", FILE_PATH)

    try:
        df = pd.read_csv(FILE_PATH)
        logger.info("File loaded successfully")
        return df
    except Exception as e:
        logger.exception(f" file not found : {e}")
        raise 
    finally:
        logger.info("pipeline runs smoothly")   

    # counting number of rows...
    rows = len(df)

    logger.info(f"Number of rows extracted is: {rows}")
    

if __name__ == "__main__":
    df = extract() 




