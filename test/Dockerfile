FROM python:3.6
WORKDIR /code
COPY * ./
RUN pip install -r requirements.txt
RUN ["sh", "wait-for-it.sh", "back:8000", "--timeout=0", "--", "python", "app_test.py"]