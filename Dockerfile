FROM python:3.9-slim

COPY ./api/requirements.txt .

RUN pip install --upgrade -r ./requirements.txt

COPY ./api/src ./src

COPY ./models ./models

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]