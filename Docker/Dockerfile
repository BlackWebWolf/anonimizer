FROM postgres:9.6

RUN apt-get update && apt-get install python-dev libpq-dev python-pip -y && pip install psycopg2 Faker

CMD ["postgres"]