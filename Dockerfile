FROM python:3.11

RUN mkdir /src


COPY ./new_www /src
RUN apt-get update

WORKDIR /src
# RUN apt-get update && \
#     apt-get install dos2unix && \
#     apt-get clean

# RUN dos2unix new_www/docker-entrypoint.sh

# RUN sed -i 's/\r$//' new_www/docker-entrypoint.sh


ENV PYTHONPATH=${PYTHONPATH}:new_www
RUN echo $PYTHONPATH
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install
RUN chown 777 docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]

