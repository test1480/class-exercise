import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def inspect_file(filepath_str):
    """Return basic information about an existing file."""
    filepath = Path(filepath_str)

    if not filepath.is_file():
        logger.error(f"File not found {filepath_str}")
        raise FileNotFoundError("File not found")

    return {"name":filepath.name, "extension":filepath.suffix}


def inspect_extension(file_info):
    """Confirm that the file uses a supported text extension."""
    supported_extension = ".txt"

    if file_info['extension'] != ".txt":
        logger.error(f"Unsupported file: {file_info['extension']}")
        raise ValueError("Unsupported file")

    return file_info