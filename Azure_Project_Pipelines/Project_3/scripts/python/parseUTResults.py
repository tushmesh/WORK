import xml.etree.ElementTree as ET
import os
import sys
import argparse
import logging
from colorama import Fore, Style

# Main Script
# PARAMETERS
parser = argparse.ArgumentParser()
# sender's email address
parser.add_argument('-fp', '--filepath',
                    required=True,
                    help=f"Unit Test results file path{os.linesep}")
parser.add_argument('-ll', '--loglevel',
                    default='INFO',
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help=f"Sets the log level to use.{os.linesep}"
                         f"Accepted values: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']")
# Reading args
args = parser.parse_args()
filepath = str(args.filepath)
# Logger Configuration
logging_level = logging.INFO
if args.loglevel != 'INFO':
    logging_level = getattr(logging, args.loglevel.upper())

logging.basicConfig(stream=sys.stdout,
                    format='[%(asctime)s][%(name)-12s][%(levelname)-8s]: %(message)s',
                    level=logging_level)
logger = logging.getLogger("UnitTestResultsParser ")

try:
    tree = ET.parse(filepath)
    root = tree.getroot()
    tests = 0
    errors = 0
    failures = 0
    skipped = 0
    testsuites = 0
    for testsuite in root.iter('testsuite'):
        tests += int(testsuite.attrib['tests'])
        errors += int(testsuite.attrib['errors'])
        failures += int(testsuite.attrib['failures'])
        skipped += int(testsuite.attrib['skipped'])
        testsuites += 1

    success = tests - errors - failures - skipped
    print(Fore.BLUE + "***  Global Unit Tests Results:")
    print(Fore.GREEN + f"***  Testsuites: {testsuites}")
    print(Fore.GREEN + f"***  Successful tests in all testsuites: {success}/{tests}")
    print(Fore.RED + f"***  Tests errors in all testsuites: {errors}")
    print(Fore.RED + f"***  Tests failures in all testsuites: {failures}")
    print(Fore.YELLOW + f"***  Tests skipped in all testsuites: {skipped}")

except Exception as ex:
    message = f"An exception occurred while running:{os.linesep}" \
              f"TYPE:{type(ex)}{os.linesep}" \
              f"ARGS: {ex.args}{os.linesep}" \
              f"ERROR:{ex}"
    logger.info(message)
    exit(666)
