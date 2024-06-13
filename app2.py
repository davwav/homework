import json
import os

def is_prime(n):
    if n < 0:
        return False
    if n <= 1:
        return True
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def string_to_bool(text):
    if text == "False":
        return False
    if text == "True":
        return True
    else:
        return None

def check_file_for_errors(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)

    errors = []
    for process in data:
        process_name = process["Process Name"]
        process_id = process["Process ID"]
        is_prime_flag = string_to_bool(process["Is Prime"])

        if is_prime(process_id) != is_prime_flag and (process_id != 0 or 1):
            error_message = f"Для {process_name} процесса найдена ошибка. \n" \
                            f"Число(PID) {process_id} на самом деле " \
                            f"{'простое' if is_prime(process_id) else 'составное'}, а в файле написано {'простое' if is_prime_flag else 'составное'}."
            errors.append(error_message)

    with open("errors.txt", "w") as error_file:
        if errors:
            for error in errors:
                error_file.write(error + "\n")
            error_file.write(f"\nВ файле найдены ошибки: {len(errors)} штуки")
        else:
            error_file.write("Ошибок не найдено")

    print("Error check completed and written to errors.txt")

if __name__ == "__main__":
    filepath = os.getenv('PIDS_JSON_PATH', 'prime_pids.json')
    check_file_for_errors(filepath)
