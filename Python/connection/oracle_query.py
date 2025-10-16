import pandas as pd
from typing import Dict, Optional
from database import DatabaseConnection

class OracleQuery:
    def __init__(self):
        self.db = DatabaseConnection()

