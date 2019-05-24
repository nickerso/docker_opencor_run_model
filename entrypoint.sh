#!/bin/bash

PERIOD=$1

if [ "x$PERIOD" == "x-h" ]; then
  echo "Usage: docker run hsorby/opencor-python <float>"
  echo "  where <float> is the stimulation period as a decimal number."
  exit 1
else
  exec ./OpenCOR-2019-05-23-Linux/bin/OpenCOR -c PythonRunScript::script run_model.py $PERIOD
fi

