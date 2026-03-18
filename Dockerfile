FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv
RUN uv sync

EXPOSE 3000

CMD ["uv", "run", "bentoml", "serve", "src.service:RFClassifierService", "--port", "3000"]