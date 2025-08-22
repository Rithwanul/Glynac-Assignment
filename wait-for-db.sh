#!/bin/sh
# wait-for-db.sh

host="$1"
shift
cmd="$@"

echo "Waiting for database at $host..."

# Extract hostname and port
DB_HOST=$(echo $host | cut -d':' -f1)
DB_PORT=$(echo $host | cut -d':' -f2)

until PGPASSWORD="$DATABASE_PASSWORD" psql -h "$DB_HOST" -p "$DB_PORT" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q' >/dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Postgres is up - executing command"
exec "$@"

