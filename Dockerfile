FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    gcc \
    make

WORKDIR /app
#copying only required files for first layers
COPY requirements.txt .
COPY pyvenv.cfg .

# Create a virtual environment in /opt
RUN python3 -m venv /opt/venv

# Install requirments to new virtual environment
RUN /opt/venv/bin/pip install --upgrade pip

RUN /opt/venv/bin/pip install -r requirements.txt

# purge unused
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# copying source files here to speedup docker rebuild
COPY . .
# make entrypoint.sh executable
RUN chmod +x entrypoint.sh

WORKDIR /app




CMD [ "./entrypoint.sh" ]