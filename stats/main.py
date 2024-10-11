#make this file the thing that calls the parser
import configparser
import os
import json
from xml.dom.minidom import CharacterData
import yaml
from stats.parser import parse_run

#this will read config and look for the paths that you set
#update your config with your paths to the runs folder of STS

def discover_runs() -> None:
    paths_to_ingest = []
    with open('stats/config-data.yml', 'r') as f:
        config_generator_object = yaml.safe_load_all(f)
        config = list(config_generator_object)[0]
        for character,path in config['run_path'].items():
            ingest_runs(character, path)


#this will be responsible for going into the path and read each run file
def ingest_runs(character, path) -> None:
    bad_file_count = 0
    for file_name in [file for file in os.listdir(path) if file.endswith('.run')]:
        with open(path + file_name) as json_file:
            data = json.load(json_file)
            try:
                parse_run(data)
            except Exception as e:
                bad_file_count+=1
                print(f"Issue reading File:{file_name}.run")
                print(f"Caused by {e}")
                continue

def main():
    #discover->ingest->parse
    discover_runs()


if __name__ == "__main__":
    main()