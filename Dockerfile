FROM apache/airflow:2.10.5
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
          gcc g++ \
          python3-dev default-libmysqlclient-dev build-essential pkg-config \
          libldap2-dev libsasl2-dev slapd ldap-utils tox lcov valgrind \
          heimdal-dev \
          libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow
# RUN python -m pip install --upgrade pip
# RUN pip install --upgrade setuptools
# RUN pip install apache-airflow==2.8.4 \
#     --constraint \
#     "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.4/constraints-3.10.txt"
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip uninstall -y argparse

