default: cv

data.bin: data.toml data.py
	@python data.py data.toml data.bin ${CVKEY}

template.html: template.jade
	pyjade -c jinja template.jade template.html

cv: data.py data.bin template.html
	python render.py

clean:
	rm -rf cv.html cv.pdf template.html data.bin
