uvicorn main:app --host 127.0.0.1 --port 3003 --reload


Make migration
alembic revision --autogenerate -m 'initial_migration'

Made migration
alembic upgrade head


