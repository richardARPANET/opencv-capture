FROM jjanzic/docker-python3-opencv:latest

# RUN apk add --update \
#     redis make gcc git ghostscript file libmagic imagemagick imagemagick-dev pulseaudio-dev \
#     swig \
#     python-dev poppler-utils postgresql-libs postgresql-dev musl-dev linux-headers jpeg-dev libxslt-dev
RUN apt-get update
RUN apt-get install -y libdvdnav4 libdvdread4 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
RUN apt-get update && apt-get install -y vlc
COPY requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt
ADD . /opt/app
WORKDIR /opt/app
ENV PYTHONPATH="${PYTHONPATH}:./src/"
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
