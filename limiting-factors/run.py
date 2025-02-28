"""Demonstration of OpenAirClim simulation run"""

import os
import shutil
import sys
sys.path.append(".../oac")  # change to OpenAirClim directory
import openairclim as oac

# change directory to match current file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TOML_FILE = "hist_mg.toml"
OUTPUT_DIR = "results/megill/hist_g0p50/"
oac.run(TOML_FILE)

# copy config file to output directory
shutil.copyfile(
    TOML_FILE,
    f"{os.path.dirname(os.path.abspath(__file__))}/{OUTPUT_DIR}{TOML_FILE}"
)
shutil.copyfile(
    "debug.log",
    f"{os.path.dirname(os.path.abspath(__file__))}/{OUTPUT_DIR}debug.log"
)
