brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install: # python3 -m pip install --user dist/*.whl
	python3 -m pip install dist/*.whl

uninstall-hexlet:
	pip uninstall hexlet_code -y

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression
