FROM python:2.7
ADD . /code
WORKDIR /code/
ENV PROJECT_CONFIG=development
RUN pip install -r requirements.txt

EXPOSE 9000
