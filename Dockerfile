FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv
RUN uv sync

EXPOSE 10000

CMD ["sh", "-c", "uv run python src/models/train_model.py && uv run bentoml serve src.service:RFClassifierService --port ${PORT:-10000}"]