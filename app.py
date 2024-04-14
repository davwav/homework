import psutil
import json
import os
import sys
import time

def get_processes_info():
    processes_info = []
    for process in psutil.process_iter(['pid', 'name']):
        prime_state = None
        for i in range(2, (int(process.info['pid']/2))):
            if ( process.info['pid'] % i == 0 ):
                prime_state = False
                break
            else:
                prime_state = True
        if process.info['pid'] == 1:
                prime_state = True
        processes_info.append({
            'Process Name': process.info['name'],
            'Process ID': process.info['pid'],
            'Is Prime': f'{prime_state}'
        })
    return processes_info

def generate_json(output_dir, json_data, json_name):

    data = json_data


    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"{json_name}.json")
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    if len(sys.argv) != 3:
        print("Usage: python main.py OUTPUT_DIR OUTPUT_NAME ")
        sys.exit(1)

name_of_json = sys.argv[2]
processes_info = get_processes_info()
output_dir = sys.argv[1]
generate_json(output_dir, processes_info, name_of_json)
time.sleep(300)
