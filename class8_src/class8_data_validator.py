import logging

logger = logging.getLogger(__name__)

def require_columns(df, required_cols):
    """Check that all required columns exist."""
    missing_columns = [col for col in required_cols if col not in df.columns]
    if missing_columns: 
        #logger.error(f"{len(missing_columns)} Columns Missing")
        logger.error(f"Missing Columns: {",".join(missing_columns)}")
        raise ValueError("one or more required columns are missing")
    logger.info("Columns Validated")
    return df   