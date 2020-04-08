#!/bin/bash
set -e #Exit immediately if a command exits with a non-zero status.

STIM_MODE=$1
STIM_LEVEL=$2

if [ "x$STIM_MODE" == "x-h" ]; then
  echo "Usage: docker run hsorby/opencor-python <int> <float>"
  echo "  where <int> is the stimulation mode as an integer number (1:stellate; 2:vagal)"
  echo "  and <float> is the stimulation level in the interval [0-1] as a decimal number."
  exit 1
else
  exec ./OpenCOR-2020-02-14-Linux/bin/OpenCOR -c PythonShell::python run_model.py $STIM_MODE $STIM_LEVEL
fi

