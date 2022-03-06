FROM python:3.6
WORKDIR /code
COPY * ./
RUN pip install -r requirements.txt
RUN "tr -d '\r' wait-for-it.sh > wait-for-it.sh"