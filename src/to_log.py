"""
isolated log-func for usage in edge cases
"""

import os
import time


def log_message(message: str, log_name: str = "default.log", log_dir: str = "./logs/", is_silent: bool = False) -> bool:
    """
    function for loggin msg into specialised log
    :param message: - body of mesasge
    :param log_name: - name of log-file
    :param is_silent: - flag of print in console
    :return: - flag of success
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"[{timestamp}] {message}"

    if not os.access(log_dir, os.F_OK):
        os.mkdir(log_dir, mode=0o777)

    try:
        with open(log_dir + log_name, "a", encoding="utf8") as f:
            f.write(log_line)
        if not is_silent:
            print(message)
        return True

    except Exception as e:
        print("logger crashed", str(e), sep=" ")
        return False
