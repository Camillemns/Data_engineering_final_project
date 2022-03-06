FROM python:3.6
WORKDIR /code
COPY * ./
RUN pip install -r requirements.txt
RUN sed 's/\r$//' wait-for-it.sh > wait-for-it.sh
RUN chmod +x wait-for-it.sh
CMD ["./wait-for-it.sh", "back:8000", "--timeout=0", "--", "python", "app_test.py"]