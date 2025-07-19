"""
Configuration settings for Hurricane Florence geospatial analysis.
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"

# Data files
FLORENCE_JSON = DATA_DIR / "florence_2018.json" 