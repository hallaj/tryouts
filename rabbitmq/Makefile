#!/usr/bin/env make
# -*- makefile -*-

down:
	docker-compose down

start:
	docker-compose up -d
	sleep 10
	docker-compose exec -T postgres psql -Upostgres -c 'CREATE DATABASE master'
	docker-compose exec -T postgres psql -Upostgres -c 'CREATE DATABASE node'
	docker-compose exec -T rabbitmq rabbitmqctl add_user admin admin
	docker-compose exec -T rabbitmq rabbitmqctl set_user_tags admin administrator
	docker-compose exec -T rabbitmq rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
	docker-compose exec -T master python /srv/master.py bootstrap
	docker-compose exec -T node python /srv/node.py bootstrap
	docker-compose exec -T node circusd --daemon /srv/node/circus/circus.ini
