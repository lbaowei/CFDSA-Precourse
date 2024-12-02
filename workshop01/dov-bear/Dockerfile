FROM python:3.8

# Setup
ADD python python
WORKDIR python
RUN pip install -r ./requirements.txt

# environment variable
ENV APP_PORT=3000

# Add health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=5s \
    CMD curl -s -f http://localhost:${APP_PORT}/healthz > /dev/null || exit 1

# entrypoint command
ENTRYPOINT ./run.sh