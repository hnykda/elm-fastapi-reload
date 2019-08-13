FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

RUN pip install aiofiles
COPY ./main.py /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/static/"]
