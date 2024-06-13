import psutil
import json
import os
import sys
import time
import re

def get_processes_info():
    regexp_filter = os.getenv('PROCESS_NAME_FILTER', '.*')  # Default to '.*' if not set
    processes_info = []

    for process in psutil.process_iter(['pid', 'name']):
        process_name = process.info['name']

        # Apply the regexp filter
        if re.search(regexp_filter, process_name):
            prime_state = None
            pid = process.info['pid']

            if pid > 1:
                for i in range(2, int(pid / 2) + 1):
                    if pid % i == 0:
                        prime_state = False
                        break
                else:
                    prime_state = True
            else:
                prime_state = True

            processes_info.append({
                'Process Name': process_name,
                'Process ID': pid,
                'Is Prime': f'{prime_state}'
            })

    return processes_info

def generate_json(output_dir, json_data, json_name):
    if not output_dir:
        output_dir = "."  # Default to the current directory if output_dir is empty
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"{json_name}.json")
    with open(output_file, "w") as f:
        json.dump(json_data, f, indent=4)

def main():
    pids_json_path = os.getenv('PIDS_JSON_PATH', 'prime_pids.json')
    if not pids_json_path:
        print("Environment variable PIDS_JSON_PATH not set.")
        sys.exit(1)

    output_dir, name_of_json = os.path.split(pids_json_path)
    name_of_json = os.path.splitext(name_of_json)[0]

    processes_info = get_processes_info()
    generate_json(output_dir, processes_info, name_of_json)
