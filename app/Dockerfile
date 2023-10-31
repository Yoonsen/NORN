# Import python 3.11 slim image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

ENV PORT=8080
ENV BASE_URL="norn"

# Install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run Norn.py when the container launches

CMD streamlit run --server.port $PORT --server.baseUrlPath $BASE_URL Norn.py