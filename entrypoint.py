import os
from main import main
import time

# Run the first application to create the JSON file
main()
print(f"ENABLE_TESTING: {os.getenv('ENABLE_TESTING', 'false').lower()}")

# Conditionally run the second application if ENABLE_TESTING is true
if os.getenv('ENABLE_TESTING', 'false').lower() == 'true':
    import app2
    app2.check_file_for_errors(os.getenv('INPUT_PATH', 'prime_pids.json'))

    from main import main
    main()

time.sleep(180)
