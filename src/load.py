from utils.logger_setup import get_logger
import pandas as pd
from pathlib import Path
from transform import transformation

logger = get_logger(__name__)

def load(df):

    logger.info("saving Cleaned data Begins")

    output_path = Path(__file__).parent.parent/"data"/"cleaned_data"/"cleaned_students.csv"

    try:
        df.to_csv(output_path , index=False)
        logger.info("Load successful! Saved %d rows to %s", len(df), output_path)
    except Exception as e:
        logger.exception("Load failed: %s", e)
        raise

if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent.parent/"data"/"raw"/"Student_details.csv"
    df = pd.read_csv(FILE_PATH)
    cleaned_df = transformation(df)   
    load(cleaned_df)   

        
