import enum
import json
import os
import pandas as pd


class Character(str, enum.Enum):
    defect = "DEFECT"
    ironclad = "IRONCLAD"
    silent = "THE_SILENT"
    watcher = "WATCHER"


def parse_run(run_file: json) -> dict:
    return {}


