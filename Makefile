install:
	poetry install

#test:
#	poetry run pytest
#
#test-coverage:
#	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 brain_games
selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime