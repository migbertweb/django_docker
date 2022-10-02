#!/bin/sh

if [ "$DATABASE" = "mariadb" ]
then
    echo "Waiting for Mariadb o mysql..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "MariaDB o MySql started"
fi

 python manage.py flush --no-input
 python manage.py migrate

exec "$@"

