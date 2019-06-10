FROM ubuntu:18.04

# Acquire libraries required for running OpenCOR from the command line.
RUN apt-get -qq update && apt-get install -y \
 libpulse-mainloop-glib0 \
 libfontconfig1 \
 libfreetype6 \
 libx11-6 \
 libx11-xcb1 \
 libxext6 \
 libxslt1.1 \
 sqlite3


WORKDIR /home/opencor

# Taking the OpenCOR binary from the web, this binary is Python enabled.  This method fails to complete for me so enabling the alternative method.
ADD https://github.com/dbrnz/opencor/releases/download/snapshot-2019-05-23/OpenCOR-2019-05-23-Linux.tar.gz /home/opencor/

# The alternate option is to add the pre-downloaded binary from the local disk (assuming you have it locally available).
# ADD ./OpenCOR-2019-05-23-Linux.tar.gz /home/opencor/

RUN tar -xvzf OpenCOR-2019-05-23-Linux.tar.gz &&\
    rm OpenCOR-2019-05-23-Linux.tar.gz

COPY ./entrypoint.sh /usr/local/bin
COPY ./Ohara_Rudy_2011.cellml /home/opencor/models/
COPY ./action-potential.xml /home/opencor/models/
COPY ./run_model.py /home/opencor/


ADD VERSION .

ENTRYPOINT ["entrypoint.sh"]
CMD ["-h"]

