export POSTGRES_DB_LOGIN='user_service_user'
export POSTGRES_DB_PASSWORD='user_service_pass'
export POSTGRES_DB_HOST='localhost'
export POSTGRES_DB_PORT=5433
export POSTGRES_DB_NAME='user_service_database'
export SQLALCHEMY_ECHO=0
export SQLALCHEMY_POOL_SIZE=10

export POSTGRESQL_URL="postgres://${POSTGRES_DB_LOGIN}:${POSTGRES_DB_PASSWORD}@${POSTGRES_DB_HOST}:${POSTGRES_DB_PORT}/${POSTGRES_DB_NAME}?sslmode=disable"

export PYTHONPATH=$PWD:$PWD/src:$PWD/src/

export APP_HOST=0.0.0.0
export APP_PORT=8002

export LOGGING_LEVEL=20