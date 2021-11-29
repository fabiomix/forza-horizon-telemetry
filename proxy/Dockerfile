FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
EXPOSE 9999/udp

# import "proxy" script
COPY app/* /app/

# then run, with the default options
ENTRYPOINT ["python3", "/app/ForzaUdpProxy.py"]
CMD []
