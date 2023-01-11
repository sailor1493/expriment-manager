srcs=experiment/
tests=test/

typehint:
	mypy ${srcs}

style:
	black ${srcs} ${tests}

lint:
	pylint ${srcs}

test:
	python3 -m unittest discover ${tests} -v

checklist: style typehint lint test

requirements:
	pip install -r requirements.txt

.PHONY: typehint style lint test checklist install