FROM mysql:8.0

# Salin konfigurasi custom dan SQL init
COPY ./my.conf /etc/mysql/conf.d/my.cnf
COPY ./sql-init/ /docker-entrypoint-initdb.d/

# Atur permission agar bisa dibaca
RUN chmod 644 /etc/mysql/conf.d/my.cnf
