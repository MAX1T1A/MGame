export POSTGRES_DB_LOGIN='core_service_user'
export POSTGRES_DB_PASSWORD='core_service_pass'
export POSTGRES_DB_HOST='localhost'
export POSTGRES_DB_PORT=5432
export POSTGRES_DB_NAME='core_service_database'
export SQLALCHEMY_ECHO=0
export SQLALCHEMY_POOL_SIZE=10

export POSTGRESQL_URL="postgres://${POSTGRES_DB_LOGIN}:${POSTGRES_DB_PASSWORD}@${POSTGRES_DB_HOST}:${POSTGRES_DB_PORT}/${POSTGRES_DB_NAME}?sslmode=disable"

export REDIS_URL="redis://localhost:6379/0"

export PYTHONPATH=$PWD:$PWD/src:$PWD/src/

export APP_HOST=0.0.0.0
export APP_PORT=8001

export LOGGING_LEVEL=10