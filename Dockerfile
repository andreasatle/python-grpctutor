FROM python:3.11.4-slim-buster

ENV HELLO_SERVICE_HOST="[::]"
ENV HELLO_SERVICE_PORT=50051

WORKDIR /usr/app

# Install socketio and related packages
RUN pip install -U pip
RUN pip install grpcio-tools==1.57.0
RUN pip install asyncio==3.4.3
#RUN pip install logging

COPY grpctutor grpctutor

CMD ["python", "-m", "grpctutor.server"]
