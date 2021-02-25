fresh-install: venv pip-install

update-packages:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

venv:
	mkdir -p ~/virtualenvs
	virtualenv -p /usr/bin/python3 ~/virtualenvs/hacktech-py3
	echo "# Virtualenv" >> ~/.profile
	echo "source ~/virtualenvs/hacktech-py3/bin/activate" >> ~/.profile

pip-install:
	. ~/virtualenvs/hacktech-py3/bin/activate; \
	pip3 install -r requirements.txt

lint:
	yapf -i -r .

test: init-test-db
	python3 -m pytest .

init-test-db:
	mysql -u hacktech_test --password= < sql/reset.sql
