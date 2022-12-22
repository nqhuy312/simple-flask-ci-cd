FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT=80
