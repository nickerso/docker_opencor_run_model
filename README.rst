

Docker for OpenCOR with Sanic
=============================

This repository holds the files required to build a Docker image that runs a simulation of a CellML model using OpenCOR with Python.
It achieves this by serving a Sanic service which allows simulations to be executed via a web API.
The Sanic server is installed into the internal OpenCOR Python interpreter and that is the interpreter used to run the server.

Build Command
-------------

You will need to get a copy of the OpenCOR binary from `here <https://opencor.ws/downloads/snapshots/2020-02-14/OpenCOR-2020-02-14-Linux.tar.gz>`_.
Save this in the directory where the 'Dockerfile' file exists.

::
  
  docker build --rm -t opencor-python/sanic .

Run Command
-----------

The Sanic server runs in the container under port 8000.
This needs to be mapped to a port on the host if you would like to access this outside the container.

::

  docker run -p 12345:8000 -d opencor-python/sanic



Using
-----

Using the above run command, you can run a simulation by accessing the URL http://localhost:12345/run_model?stim_mode=1&stim_level=0.5 where the stim_mode is the stimulation mode as an integer number (1:stellate; 2:vagal) and stim_level is the stimulation level (0-1) as a decimal number.

The result is a JSON object (printed in the browser window) with the membrane potential 'v' at each time step and the heart rate in beats per minute, as per the sample shown below.

::

    {
        "heart_rate": 73,
        "membrane": {
            "v": [-47.78, -47.82, -47.85, ...]
        }
    }

Implementation notes
--------------------

We are using the Fabbri et al (2017) sinoatrial cell model: https://models.physiomeproject.org/e/568

The model includes autonomic modulation via inclusion of the effects of ACh on I\ :sub:`f`, I\ :sub:`CaL`, SR calcium uptake, and I\ :sub:`K,ACh`; and the effect of isoprenaline on I\ :sub:`f`, I\ :sub:`CaL`, I\ :sub:`NaK`, maximal Ca uptake, and I\ :sub:`Ks`. We are varying the concentration of ACh according to the stimulation level, while isoprenaline is encoded to be "on" or "off" only (we use the "on" version in this exemplar). The range of ACh we're allowing is beyond what has been presented in the paper.

Example output
++++++++++++++

Plotted example data when using this container to simulate various levels of stellate stimulation:

.. image:: stellate-stimulation.png

Plotted example data when using this container to simulate various levels of vagus stimulation:

.. image:: vagus-stimulation.png


