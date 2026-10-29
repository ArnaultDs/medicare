FROM apache/airflow:3.3.0-python3.12

# Optionnel : forcer une version précise de uv plutôt que celle de l'image
# COPY --from=ghcr.io/astral-sh/uv:0.x /uv /uvx /bin/

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

# 1. venv dbt isolé, placé AVANT le COPY du code pour profiter du cache de layer
RUN uv venv /home/airflow/dbt-venv \
 && uv pip install --no-cache \
      --python /home/airflow/dbt-venv/bin/python \
      "dbt-core<1.12" dbt-postgres

# 2. Ton package + Airflow, sous contraintes officielles
COPY --chown=airflow:root pyproject.toml README.md ./
COPY --chown=airflow:root src/ ./src/

RUN uv pip install --no-cache \
      "apache-airflow==${AIRFLOW_VERSION}" . \
      --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.12.txt"