FROM python:3.6
WORKDIR /code
COPY * ./
RUN pip install -r requirements.txt
RUN sed 's/\r$//' wait-for-it.sh > wait-for-it.sh
RUN ls