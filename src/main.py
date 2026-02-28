from utils.logger_setup import get_logger
from pathlib import Path
from extract import extract           
from transform import transformation
from load import load                 

logger = get_logger(__name__)


def run_pipeline():
    logger.info("------ PIPELINE STARTED ------")

    try:
        # Extract
        df = extract()                       

        # Transform
        cleaned_df = transformation(df)

        # Load
        load(cleaned_df)

        logger.info("------ PIPELINE COMPLETED ------")

    except Exception as e:
        logger.exception("PIPELINE FAILED: %s", e)
        raise


if __name__ == "__main__":
    run_pipeline()