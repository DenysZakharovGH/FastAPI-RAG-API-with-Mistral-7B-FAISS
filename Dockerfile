FROM python:3.10-slim

# System deps for llama.cpp
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt .

# Install Python deps
RUN pip install torch torchvision torchaudio   --index-url https://download.pytorch.org/whl/cu118
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app /app
COPY frontend /frontend

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]