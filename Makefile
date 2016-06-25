default: cv
cv.json: cvdb.py
	python cvdb.py
cv: cv.json template.jade
	pyjade -c jinja template.jade template.html
	python render.py
