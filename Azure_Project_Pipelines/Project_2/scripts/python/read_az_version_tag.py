import argparse
import json
import logging
import os.path
import requests
import sys

# Main Script
# PARAMETERS
parser = argparse.ArgumentParser()

parser.add_argument('-ll', '--loglevel',
                    default='INFO',
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help=f"Sets the log level to use.{os.linesep}"
                         f"Accepted values: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']")
# Reading args
args = parser.parse_args()

# Logger Configuration
logging_level = logging.INFO
if args.loglevel != 'INFO':
    logging_level = getattr(logging, args.loglevel.upper())

logging.basicConfig(stream=sys.stdout,
                    format='[%(asctime)s][%(name)-12s][%(levelname)-8s]: %(message)s',
                    level=logging_level)
logger = logging.getLogger("TeamsNotify")

try:
    response_dict = ""
    with open('.response', 'r') as file:
        _resp = file.read().replace("\n", " ")
        response_dict = json.loads(_resp)


    with open('taglist.lst', 'w') as file2:
        try:
            logger.info(f"""Actually deployed version: {response_dict["properties"]["tags"]["version"]}""")
            file2.write(f"""{response_dict["properties"]["tags"]["version"]}""")
        except KeyError as e:
            logger.info(f"""Actually deployed version: No version found""")
            file2.write("None")

except Exception as ex:
    message = f"An exception occurred while running:{os.linesep}" \
              f"TYPE:{type(ex)}{os.linesep}" \
              f"ARGS: {ex.args}{os.linesep}" \
              f"ERROR:{ex}"
    logger.info(message)
    exit(666)




