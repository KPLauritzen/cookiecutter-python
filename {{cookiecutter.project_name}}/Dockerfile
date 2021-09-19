FROM python:3.9-slim-bullseye as base

## Need to install some packages? Uncomment this
#RUN apt-get update && \
#    DEBIAN_FRONTEND=noninteractive \
#    apt-get install -y --no-install-recommends \
#    somepackage
WORKDIR /work

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY setup.py .
COPY src/ src/
RUN pip install --no-cache-dir --use-feature=in-tree-build -e .

FROM base as test
COPY requirements-dev.txt .
RUN pip install  --no-cache-dir -r requirements-dev.txt
COPY tests/ tests/
CMD ["pytest"]

FROM base as prod
CMD ["python"]