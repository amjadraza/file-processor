FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV LISTEN_PORT 8080

EXPOSE 8080

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./file_processor /app/file_processor

CMD ["uvicorn", "file_processor.API.main:app", "--host", "0.0.0.0", "--port", "8000"]
