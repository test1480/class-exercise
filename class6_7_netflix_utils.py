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