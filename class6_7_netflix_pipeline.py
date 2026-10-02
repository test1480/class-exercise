import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    clean_text,
    drop_missing_rows,
    remove_duplicates,
    remove_iqr_outliers,
    show_overview,
)

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    # TODO 4:
    datafile = Path(args.input)
    try:
        df = pd.read_csv(datafile)
    except FileNotFoundError:
        logger.error("File Not Found")
        sys.exit(1)
    logger.info(f"Data loaded: {args.input}")

    # TODO 5:
    logger.info("Showing Overview:")
    #show_overview(df)
    
    df_original = df.copy()

    # TODO 6:
    before = len(df)
    df = remove_duplicates(df)
    logger.info("Removed duplicates")
    df = drop_missing_rows(df)
    logger.info("Removed missing rows")


    # TODO 3:
    try:
        df = remove_iqr_outliers(df,"runtime_minutes",1.5)
    except ValueError:
        sys.exit(1)
    logger.info(f"Removed outliers")

    # TODO 4:
    for col in ["title","type","country"]:
        df[col].apply(clean_text)
        logger.info(f"Column {col} Text cleaned")

    # TODO 5:
    report = {"rows_before":len(df_original),"rows_after":len(df),"rows_removed":len(df_original)-len(df),"columns":df.columns.tolist()}
    logger.info(f"Report:{report}")

if __name__ == "__main__":
    main()