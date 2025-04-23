run:
	poetry run uvicorn main:app --reload --env-file .local.env

install:
	@echo "Installing dependency $(LIB)"
	poetry add $(LIB)

delete:
	poetry remove $(LIB)

update:
	poetry update $(LIB)
