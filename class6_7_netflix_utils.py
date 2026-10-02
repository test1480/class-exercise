import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    logger.debug(f"Showing overview -- {df.shape}")
    print(f"Shape: {df.shape}")
    print(f"First Five:")
    print(df.head())
    print(f"Column names: {df.columns}")
    print(f"Data types:")
    print(df.dtypes)


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    before = len(df)
    df = df.drop_duplicates()
    logger.debug(f"Duplicates: {before - len(df)} rows removed")
    return df


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    before = len(df)
    df = df.dropna()
    logger.debug(f"Missing Values: {before - len(df)} rows removed")
    return df

import re

def clean_text(value):
    """Normalize one text value."""
    value = value.strip()
    value = value.lower()
    value = re.sub(r"\s+", " ", value)
    return value


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    # TODO 2:
    if column not in df.columns.tolist():
        logger.error(f"Column {column} not found")
        raise ValueError(f"Column {column} not found")
    before = len(df)
    q3 = df[column].quantile(0.75)
    q1 = df[column].quantile(0.25)
    iqr = q3 - q1
    lower = q1 - threshold * iqr
    upper = q3 + threshold * iqr
    df = df[(df[column] >= lower) & (df[column] <= upper)]
    logger.debug(f"Threshold:{threshold}; {before-len(df)} rows removed")
    return df