import json
import os
import pandas as pd


class Character(str, Enum.enum):
    defect = "DEFECT"
    ironclad = "IRONCLAD"
    silent = "THE_SILENT"
    watcher = "WATCHER"

defect_base_path = 'D:\Steam\steamapps\common\SlayTheSpire\\runs\DEFECT\\'
ironclad_base_path = 'D:\Steam\steamapps\common\SlayTheSpire\\runs\IRONCLAD\\'
silent_base_path = 'D:\Steam\steamapps\common\SlayTheSpire\\runs\THE_SILENT\\'
watcher_base_path = 'D:\Steam\steamapps\common\SlayTheSpire\\runs\WATCHER\\'


def parse_run(run_file: json) -> dict:
    return {}



def ingest_runs(path: str) -> dict:
    
    for file_name in [file for file in os.listdir(defect_base_path) if file.endswith('.run')]:
        with open(defect_base_path + file_name) as json_file:
            data = json.load(json_file)
            print(data)

def main():
    ingest_runs(defect_base_path)


if __name__ == "__main__":
    main()

