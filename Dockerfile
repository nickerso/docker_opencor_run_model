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
 dos2unix \
 sqlite3


WORKDIR /home/opencor

# Taking the OpenCOR binary from the web, this binary is Python enabled.  This method fails to complete for me so enabling the alternative method.
#ADD https://github.com/dbrnz/opencor/releases/download/snapshot-2019-06-11/OpenCOR-2019-06-11-Linux.tar.gz /home/opencor/
#RUN tar -xvzf OpenCOR-2019-06-11-Linux.tar.gz && \
#    rm OpenCOR-2019-06-11-Linux.tar.gz

# The alternate option is to add the pre-downloaded binary from the local disk (assuming you have it locally available).
ADD ./OpenCOR-2020-02-14-Linux.tar.gz /home/opencor/

COPY ./entrypoint.sh /usr/local/bin
RUN dos2unix /usr/local/bin/entrypoint.sh
COPY ./HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.cellml /home/opencor/models/
COPY ./HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml /home/opencor/models/
COPY ./run_model.py /home/opencor/

ADD VERSION .

ENTRYPOINT ["entrypoint.sh"]
CMD ["-h"]

