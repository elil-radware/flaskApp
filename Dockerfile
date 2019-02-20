FROM alpine:3.9

ENV PATH /usr/local/bin:$PATH

ENV PYTHON_VERSION 3.6.7


RUN apk add --update \
    python3 \
    python3-dev \
    py3-pip \
    build-base \
  && pip3 install virtualenv \
  && rm -rf /var/cache/apk/*


RUN mkdir -p /$HOME/app/

COPY .. /$HOME/app/

COPY requirements.txt /$HOME/app/

WORKDIR /$HOME/app/


# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
	&& ln -s python3 python

ONBUILD RUN virtualenv /env && /env/bin/pip3 install -r /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt
#CMD ["gunicorn", "-c gconfig.py", "wsgi:app"]
CMD ["gunicorn", "-b 0.0.0.0:5000", "-w 2","wsgi:app"]
#CMD ["python --version"]
#CMD ["ll"]
#CMD ["python3", "basicServer.py"]

EXPOSE 5000
