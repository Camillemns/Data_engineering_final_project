FROM python:3.6
WORKDIR /code
COPY * ./
RUN pip install -r requirements.txt
EXPOSE 8000
RUN python pred_test.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]