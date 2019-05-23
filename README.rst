

Docker for OpenCOR
==================

This repository holds the files required to build a Docker image that runs a simulation of a CellML model using OpenCOR with Python.

Build Command
-------------

You will need to get a copy of the OpenCOR binary from `here <https://github.com/dbrnz/opencor/releases/download/snapshot-2019-05-17/OpenCOR-2019-05-18-Linux.tar.gz>`_.  Save this in the directory where the 'Dockerfile' file exists.

::
  
  docker build --rm -t hsorby/opencor_python .

Run Command
-----------

::

  docker run hsorby/opencor_python 3.0

Where the number '3.0' passed in as an argument which controls the stimulation period for the model.  Any number suitable for a stimulation period can be used to generate different outputs.

Output
------

The model outputs the membrane potential 'V' at each time step.  The output is in json format.

