RUN echo 'Creating image'

FROM python:3.4

#RUN apt-get update
#RUN apt-get update &amp;&amp; apt-get -y upgrade
#RUN apt-get install -y \
#   gcc \
#   python-dev python-distribute \
#   python-pip \
#   python-dev \
#   python-distribute python-pip

RUN mkdir -p /opt/basicAppFlask/
WORKDIR /opt/basicAppFlask

ADD requirements.txt /opt/basicAppFlask/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--workers=2", "-b 0.0.0.0:8000","wsgi:app"]

EXPOSE 8000
