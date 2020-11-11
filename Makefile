all: db-upgrade

db-migrate:
	alembic revision --autogenerate

db-upgrade:
	alembic upgrade head

db-downgrade:
	alembic downgrade -1