#!/usr/bin/env python3

import subprocess
import time
import logging
import sys

# -------------------
# CONFIGURATION
# -------------------
IP_CHECK = "192.168.0.1"  # IP to check power state
TIME_TO_CHECK = 120 # Time taken to do second check
LOG_FILE = "/root/crl_ups/logs/ups_logs.log"
DEBUG_MODE = False  #Disable script for testing purposes
# Logging conf
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def do_ping(ip):
    try:
        subprocess.run(
            ["ping", "-c", "1", "-W", "2", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def activate_shutdown_ups():
    logging.warning("Blackout detected, executing  'upsmon -c fsd'")
    try:
        subprocess.run(["/usr/sbin/upsmon", "-c", "fsd"], check=True)
    except Exception as e:
        logging.error(f"Error while executing 'upsmon -c fsd': {e}")
        sys.exit(1)

def main():
    if not DEBUG_MODE:
        logging.info("Starting check...")
        if not do_ping(IP_CHECK):
            logging.warning(f"First ping failed to {IP_CHECK}. Waiting {TIME_TO_CHECK} seconds...")
            time.sleep(TIME_TO_CHECK)
            if not do_ping(IP_CHECK):
                activate_shutdown_ups()
            else:
                logging.info("Second ping successful, everything OK.")
        else:
            logging.info("Ping succesful, everything OK.")
    else:
        logging.info(f"Debug mode activated, state: {do_ping(IP_CHECK)}")

if __name__ == "__main__":
    main()

