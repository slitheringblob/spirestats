import enum
import json
import os
import pandas as pd
from sqlalchemy.orm import DeclarativeBase

Base = DeclarativeBase()


class Character(str, enum.Enum):
    defect = "DEFECT"
    ironclad = "IRONCLAD"
    silent = "THE_SILENT"
    watcher = "WATCHER"

class Run(base):
    __tablename__ = "runs"
    

def parse_run(run_data: dict) -> dict:
    
    return {}


